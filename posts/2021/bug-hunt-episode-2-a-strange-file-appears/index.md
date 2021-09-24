<!--
.. title: Bug hunt episode 2: a strange file appears
.. slug: bug-hunt-episode-2-a-strange-file-appears
.. date: 2021-09-23
.. tags: Development, bug-hunt
.. category: article
-->

This is the second article in the ["bug hunt" series](https://briansimulator.org/tags/bug-hunt/). In these articles, I go through a recent bug in Brian (or one of its dependencies) and describe all the steps I used to find the source of the bug and how I fixed it.

Today's bug is about a strangely named file that seemingly appears out of nowhere when running Brian simulations. The final fix for the bug will turn out to be a single character change in the Brian code base 😀!

<!-- TEASER_END -->

## The bug

I recently noticed that I had a strange file in many directories on my computers. Since it only seemed to appear in directories from which I ran Brian simulations, it was pretty clear that this had something to do with Brian. The name of the file: `-.o`. Now, files ending on `.o` are usually [object files](https://en.wikipedia.org/wiki/Object_file), i.e. the machine code output of a compiler. Such files are not executable by themselves, but can be [linked](https://en.wikipedia.org/wiki/Linker_(computing)) together to form an executable file or a library. Now, of course any file could be named `something.o`, but the `file` utility (note that I am using Linux) confirms that it is an "ELF 64-bit LSB relocatable", which refers to the [standard Unix format for object files](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format). Since we use C++ code generation in Brian (either via Cython in runtime mode, or directly in standalone mode), it seems reasonable to assume that the file gets created somewhere during that process.

!!! note
    If you encounter a file named `-.o`, you can of course easily delete it using a graphical file explorer.
    On the other hand, it can be surprisingly tricky when using the command line.
    For example, simply using the standard Unix command `rm -.o` will fail with an error message about an "unknown option '.'" – most Unix tools interpret the hyphen "`-`" as the beginning of a command line option, and "`.`" is not such an option.
    Now, if you have been using the Unix command line for some time you know that the way to deal with "special characters" is to use quotation marks or to "escape" the special characters with a backslash `\`.
    For example, if you have a file named `my file.txt` (i.e. with a space in the file name), you need to delete it using either `rm "my file.txt"` or `rm my\ file.txt`, since a simple `rm my file.txt` would be interpreted as a request to delete the two files `my` and `file.txt`.
    It might come as a surprise that this does not work here, `rm "-.o"` still fails with the same error message (if you are interested in the details, you can write a small Python script that deals with its own command line arguments stored in `sys.argv` and see what it does for different inputs).
    The solution to deal with the issue here is slightly different: you either have to refer to the file without having its name start with a hyphen, or you have to make clear to `rm` that you do not want to pass additional command line arguments.
    The first approach is the most universal: instead of using `rm -.o` you can refer to the file as e.g. `rm ./-.o`.
    The `./` part simply means "in the current directory" and is usually redundant, but here it helps us avoid a name that starts with a hyphen.
    The second approach is to explicitly tell `rm` to not expect further command line arguments by using an empty argument `--`, i.e. to call `rm -- -.o`.
    This works for many Unix command line tools, not only for `rm`.


## The hunt

### Reproducing the issue

The first step of fixing an issue is making sure to be able to reproduce it. I first ran the Brian test suite (after deleting the existing `-.o` file in my directory), and confirmed that after the run the mystery file had reappeared. By construction, the test suite is of course running all (or at least most) of Brian's functionality, so something more narrow in scope (and taking less time to run) would be more useful. I noticed that I had another `-.o` file in our examples directory, so I made an educated guess that running at least one of the examples would trigger the file generation. I tested a few of them and it turned out that not all of them make the file appear. For example, running the [`CUBA.py` example](https://brian2.readthedocs.io/en/stable/examples/CUBA.html)  would *not* create a new file, but running the [`COBAHH.py` example](https://brian2.readthedocs.io/en/stable/examples/COBAHH.html) would. Evaluating this systematically for all examples might potentially give us a hint to where the issue comes from, but would also take a bit of time. For now, having the *COBAHH* example to reproduce the issue is enough.

### Hstorical research

Since I am sure that this bug hasn't been around forever, the next step is to find out when the problem has been introduced. A quick check with version `2.3.0.2` indeed shows that it can run the *COBAHH* example without generating the `-.o` file. As in the [last bug hunt](link://slug/bug-hunt-episode-1-broken-latex-output-for-equations), I then used git's *bisect* mechanism to quickly find the commit introducing the problem. This led me to commit [628ff2cddf6b90](https://github.com/brian-team/brian2/commit/628ff2cddf6b90e32a5e360fd48d99ce9f6fc355):

```
commit 628ff2cddf6b90e32a5e360fd48d99ce9f6fc355
Author: Marcel Stimberg <marcel.stimberg@inserm.fr>
Date:   Fri Jul 3 16:55:56 2020 +0200

    Do not turn integers into floats in sympy
    
    Closes #1199, closes #812
```

How this could lead to a spurious file appearing is certainly not obvious. I therefore double checked, but indeed: before that commit, the *COBAHH* example does not generate any file, but after the commit it consistently does. The changes in the commit do not seem to have anything to do with files or compilation, though. Ignoring the change in a [doctest]([doctest — Test interactive Python examples &#8212; Python 3.9.7 documentation](https://docs.python.org/3/library/doctest.html)), the main change is given as:

```diff
diff --git a/brian2/parsing/rendering.py b/brian2/parsing/rendering.py
index 76fa3107..e0186a94 100644
--- a/brian2/parsing/rendering.py
+++ b/brian2/parsing/rendering.py
@@ -1,5 +1,5 @@
-
 import ast
+import numbers
 
 import sympy
 
@@ -265,7 +265,10 @@ def render_NameConstant(self, node):
             return str(node.value)
 
     def render_Num(self, node):
-        return sympy.Float(node.n)
+        if isinstance(node.n, numbers.Integral):
+            return sympy.Integer(node.n)
+        else:
+            return sympy.Float(node.n)
 
     def render_BinOp(self, node):
         op_name = node.op.__class__.__name__
```

This was not as helpful as expected, let us therefore try a different approach.

### Step-by-step debugging

At some point during the example run, the `-.o` file gets created – but when exactly? A quick check with statements checking `os.path.exists('-.o')` in the example file makes it clear that it happens during the `run` statement (which also includes the code generation and compilation), but I wouldn't want to sprinkle such checks all over Brian's code base. Instead, I turn to a tool that was made for that job, the *debugger* (who would have thought it could be useful for debugging!). Python comes with the built-in debugging tool [`pdb`]([pdb — The Python Debugger &#8212; Python 3.9.7 documentation](https://docs.python.org/3/library/pdb.html)), but using a "graphical" debugger integrated in the IDE is much more convenient. In my case, I use the [PyCharm IDE]([PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)) and its [debugger]([Debugging with PyCharm | PyCharm](https://www.jetbrains.com/help/pycharm/debugging-python-code.html)). Using a combination of breakpoints and stepping through the code, I can now figure out exactly when and where the file gets created. This process does take a while, since either I have to step through each and every line of code (and there are many of them), or I will step over big chunks at a time, but then I will have to run everything again with more fine-grained stepping/breakpoints.

Using the latter approach, I find that the code is generated during the `before_run` period, and more specifically during the `before_run` code of the `StateUpdater`. This could explain why the *COBAHH* example shows the issue but *CUBA* does not – the two examples use different numerical integration methods (the purpose of the `StateUpdater`). Drilling further down, I find that the code is generated during the code generation process, and more specifically when target-code implementations of the mathematical functions are added. The function that triggers the file generation is `exprel` ($\mathrm{exprel}(x) = \frac{\exp(x) - 1}{x}$ with improved accuracy and defined for $x=0$). What is special about this function? The `exprel` function internally uses the C function `expm1` ($\mathrm{expm1}(x) = \exp(x) - 1$), but this function has only been added to the C standard with [C99]([C99 - Wikipedia](https://en.wikipedia.org/wiki/C99)). As the name suggests, this standard is from 1999, but compilers have been slow implementing all of its features. For example, Microsoft's Visual Studio compiler only started adding support with Visual Studio 2013! To make sure the compiler used to compile the Brian model supports C99, we have a function `compiler_supports_c99` (in [`brian2.codegen.cpp_prefs`](https://github.com/brian-team/brian2/blob/master/brian2/codegen/cpp_prefs.py)), which verifies that the compiler is recent enough.

On Unix, this test runs the following command:

```bash
echo "#if (__STDC_VERSION__ < 199901L)\n#error\n#endif" | cc -xc -c - > /dev/null 2>&1
```

This tests preprocessor macros stating the standards support of the compiler, and raises an error if it is too old. Now, this command actually tries hard *not* to generate any file! Usually, you'd write the preprocessor macros to a `.c` file and run the compiler on this file. Instead, the code is printed to the standard output using `echo`, and then ["piped"]([Pipeline (Unix) - Wikipedia](https://en.wikipedia.org/wiki/Pipeline_(Unix))) into the `cc` compiler that is asked to take its input from `stdin` by using the special filename `-`. This does work and the test is performed correctly; the `-c` option tells the compiler to only compile things and not to bother with linking into an executable. But using `-c` here actually turns out to be the issue! As the [documentation](https://gcc.gnu.org/onlinedocs/gcc/Overall-Options.html#Overall-Options) states, "The ultimate output is in the form of an object file for each source file." Our "source file" in this case is named `-` (even though it is not an actual file), and the resulting object file is therefore named  – you guessed it – `-.o`!

Once we have identified the problem, the fix is trivial: to perform the check, we do not actually have to run the compiler's compilation step at all. The check only uses the preprocessor, so we can replace `-c` by `-E` which will happily print out everything to `stdout` instead of creating a new file. Problem solved by changing a single character in the code!

### Did `git bisect` lie to us?

We found the source of the bug and a simple fix. But what about that commit we identified earlier using `git bisect` – this does not seem to have to do anything with the issue, the erroneous `compiler_supports_c99` check had been in the code much longer!

When we look at the generated code of the *COBAHH* model before the commit in question, we see that it does not contain any call to `exprel`, but only to `exp`. This explains why it does not trigger the issue (if there is no reference to `exprel`, there is no need to check for C99 compatibility), but how can the code *not* refer to `exprel` when the equations clearly do? And what does this have to do with the fact whether number literals (e.g. the `13` in `exprel(13*mV - v)`) are interpreted as floating point numbers or integers?

The answer lies in the mathematical transformations we perform for the equations, e.g. to apply the numerical integration algorithm. To do these kind of operations, we use the [SymPy package](https://www.sympy.org) which has powerful facilities for symbolic handling of equations. When we use it to transform the equations, it can do all kind of operations that (at least potentially) simplify the equations without changing their meaning. For example, using the definition of $\mathrm{exprel}$ shown earlier, we could transform it in the following way when it gets applied to the argument $x - y$;

$$
\mathrm{exprel}(x - y) = \frac{\exp(x-y) - 1}{x - y} = \frac{\frac{\exp(x)}{\exp(y)} -1}{x -y}
$$

Admittedly, this does not really *simplify* things here, but if one of the variables is in fact a constant, e.g. $x = 2$, we could evaluate this value once and use it in the equations, i.e:

$$
\dots = \frac{\frac{7.389056099}{\exp(y)}-1}{2 - y}
$$

It turns out, *SymPy* will do these kind of transformations only when the numerical value (the $2$ in this example) is a floating point number, but not when it is an integer. This is understandable, since floating point numbers are not "ideal" numbers due to their limited precision, so something like $7.389056099 \approx \exp(2)$ is only *approximately* true:

```py
>>> import sympy
>>> sympy.exp(2)
exp(2)
>>> sympy.exp(2.0)
7.38905609893065
```

This explains why earlier versions of Brian (where all number literals were interpreted as floating point numbers) sometimes got rid of `exprel` during the mathematical transformation of equations, whereas newer versions (which kept integer literals as integers) do not touch them. Removing the call to `exprel` and replacing it by variants of `exp` is actually not what we want, even if the two formulations are "mathematically equivalent". The main reason for using `exprel` in the first place is to gain accuracy and to make the function more robust for a close-to-zero argument – replacing it will remove all these advantages. But this will be a discussion for another time, which you are more than welcome to follow in this [github issue](https://github.com/brian-team/brian2/issues/1350) 😀.

## Final remarks

Yet another time, the fix for an issue turned out to be trivial (a one character change!), but finding the issue was not straightforward at all. The bug also nicely demonstrated how things can be connected in unexpected ways in a complex software project: a change in the handling of integer literals in equations leads to differences in the treatment by *SymPy* which then leads to differences in the generated code and finally triggers a compiler check that wasn't triggered before.

Hope that you learned a thing or two from reading this blog post, and maybe it motivates you to fix a bug in Brian yourself! Comments very welcome, feel free to reach out on [twitter](https://twitter.com/briansimulator) or on the [discussion forum](https://brian.discourse.group).


