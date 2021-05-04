<!--
.. title: Bug hunt episode 1: Broken LaTeX output for equations
.. slug: bug-hunt-episode-1-broken-latex-output-for-equations
.. date: 2021-05-05
.. tags: Development, bug-hunt
.. category: article
.. has_math: true
-->

This article starts a new series of blog posts about "bug hunts". In these articles, I will go through a recent bug in Brian (or one of its dependencies) and describe all the steps I used to find the source of the bug and how I fixed it. I will try to not only focus on the Brian-side of things, but also show some general tools like `git bisect` or "monkey patching" that can be helpful to find the source of these nasty critters (no actual bugs were harmed during the making of this blog post).

Let's start! Today's bug will be about equations, and more specifically about their LaTeX representation. As most of you probably know, Brian can represent equations, quantities, etc. in LaTeX. This representation can then either be included in a LaTeX document or directly rendered for example as the output in [jupyter notebooks](https://jupyter.org/).

<!-- TEASER_END -->

## Context

We don't document this feature particularly well, but is mentioned in our [development documentation](https://brian2.readthedocs.io/en/stable/developer/guidelines/representation.html?latex-representations-with-sympy#latex-representations-with-sympy) and in our [2014 paper](https://www.frontiersin.org/articles/10.3389/fninf.2014.00006/full#h5). Taking the example from that paper, our extension of [sympy](https://www.sympy.org/en/index.html)'s LaTeX printing facilities makes it possible to convert an `Equations` object to LaTeX markup:

```Python
eqs = Equations('''dv/dt = (g_L*(E_L-v) +
                            g_s*(E_s-v))/tau_m : volt
                   dg_s/dt = -g_s/tau_s : siemens''')
print(sympy.latex(eqs))
```
Output:
```latex
\begin{align*}\frac{\mathrm{d}v}{\mathrm{d}t} &= \frac{g_{L} \left(E_{L} - v\right) + g_{s} \left(E_{s} - v\right)}{\tau_{m}} && \text{(unit of $v$: $\mathrm{V}$)}\\
\frac{\mathrm{d}g_{s}}{\mathrm{d}t} &= - \frac{g_{s}}{\tau_{s}} && \text{(unit of $g_{s}$: $\mathrm{S}$)}\end{align*}
```

Included in a LaTeX document (or in a Markdown document that supports LaTeX equations like this blog post), this is rendered as:

<div><!-- to avoid that markdown replaces stars etc. -->
\begin{alignat}{4}
    \frac{\mathrm{d}v}{\mathrm{d}t} &= \frac{g_{L} \left(E_{L} - v\right) + g_{s} \left(E_{s} - v\right)}{\tau_{m}} && \text{(unit of $v$: $\mathrm{V}$)}\\
    \frac{\mathrm{d}g_{s}}{\mathrm{d}t} &= - \frac{g_{s}}{\tau_{s}} && \text{(unit of $g_{s}$: $\mathrm{S}$)}
\end{alignat}
</div>
Which looks kind of nice, in particular note the subscripts and the conversion of `tau` to $\tau$.

## The bug

Now, a couple of days ago user Sebastian Schmitt (`schmitts`) reported on our [discussion forum](https://brian.discourse.group/t/latex-representation-of-equations/376) that this feature seems to be broken. He helpfully provided a simple example demonstrating the issue (always appreciated!):
```Python
from brian2 import *
from sympy import latex
G = NeuronGroup(10, 'dv/dt = -v/(10*ms) : volt')
print(latex(G.equations))
```
Output:
```latex
\begin{align*}\mathtt{\text{\textbackslashfrac\{\textbackslashmathrm\{d\}v\}\{\textbackslashmathrm\{d\}t\}}} &= - \frac{v}{10 ms} && \text{(unit of $v$: $\mathrm{V}$)}\end{align*}
```

Which does not look right at all when rendered:
<div>
\begin{alignat}{4}\mathtt{\text{\textbackslashfrac\{\textbackslashmathrm\{d\}v\}\{\textbackslashmathrm\{d\}t\}}} &= - \frac{v}{10 ms} && \text{(unit of $v$: $\mathrm{V}$)}\end{alignat}
</div>
## The hunt

### Going down Brian's history

I confirmed the problem on my machine with the latest development version of Brian, and opened an [issue on github](https://github.com/brian-team/brian2/issues/1296). Since I was sure that this worked previously (otherwise we wouldn't have put it in the 2014 paper {{% emoji winking_face %}} ), I marked the bug as a *regression*. I therefore checked out previous releases of Brian to see whether the bug still occured. The problem was still there with version 2.3.0.1, but testing earlier versions got a bit tedious, since I could not run them directly from the source code on Python 3. I therefore switched to a Python 2 environment and checked out version 2.1.3.1, released in 2018. Lo and behold, this version did not seem to be affected by the bug. Just to make sure, I did a quick check whether the 2.3.0.1 version (the newest version of Brian that is still compatible with Python 2, see below) would show the error as I confirmed earlier; well, it didn't. So how come that this issue appears under Python 3 but not with Python 2, when using the same version of Brian? In this case, an actual dependence on the Python version seemed rather unlikely, but of course the Python version wasn't the only difference between the two environments that I used for testing – a number of packages were installed with different versions. A quick check with `conda list` (I am using [conda environments](https://conda.io) on my system) revealed: `sympy` was installed with version 1.5.1 in the Python 2 environment, and with version 1.8 in the newer Python 3 environment. Since our LaTeX output builds on `sympy`, this seemed to be the probable cause for the difference, and downgrading `sympy` indeed made the issue disappear.

!!! note
    Checking older versions of Brian can sometimes be tricky due to the Python 2 → 3 transition.
    Versions up to **2.2.2.1** used the [`2to3.py`](https://docs.python.org/3/library/2to3.html) tool to
    translate from Python 2 to Python 3. This means that code runs directly from the source directory only under
    Python 2, running it with Python 3 requires first installing it (which will run `2to3.py` to translate the 
    code). Version **2.3** got rid of this limitation, and has code that is both compatible with Python 2 and 
    Python 3 (via the [`future`](https://pypi.org/project/future/) package. This means that you can run it without 
    any installation on both Python versions. Finally, since version **2.4**, Brian is "Python 3-only" and no 
    longer has a compatibility layer for Python 2.


### What changed in sympy?

Now, what and when changed in `sympy` that broke our LaTeX support? To investigate further, I removed the installed `sympy` package and instead cloned their [development repository](https://github.com/sympy/sympy/) from github:
```console
$ conda remove --force sympy
$ git clone git@github.com:sympy/sympy.git
```
Cloning the repository takes a moment (the repository contains an impressive number of 46,784 commits!), but then it gives us access to the full history of the `sympy` project. As the next step, I installed it in "development mode" to make it possible to easily switch its version without having to install the package over and over again:
```console
$ pip install -e .
```

As most repositories do, `sympy` tags its releases and a `git tag` shows that it prefixes its release tag names with `sympy-...`. This gives us everything we need to run the amazing `git bisect` command which lets you pin-point the exact commit that introduced a regression. In this case, I start it with:
```console
$ git bisect start sympy-1.8 sympy-1.5.1
Already on 'master'
Your branch is up to date with 'origin/master'.
Bisecting: a merge base must be tested
[c6a18db2095aeed3f2820d620d817ebc3f1ccacd] Don't allow expressions to compare equal to strings
```
(From my previous tests I know that version 1.8 is affected by the problem, while version 1.5.1 is not.)

!!! note
    As the name suggests, `git bisect` runs a [bisection algorithm](https://en.wikipedia.org/wiki/Bisection_(software_engineering)). This means with each response it cuts the the number of commits to check in half – the total number of commits to check therefore only grows logarithmically with the number of total commits. Below, only 14 verifications were necessary to find the relevant commit out of more than 3000!

Now I could test each version manually and report back to `git` whether the version is "bad" or "good" (`git bisect bad` or `git bisect good`), i.e. whether it reproduced the problem or not. When you have to check many revisions, and when it is easy to verify each revision with an automatic test, there is a nice alternative to this manual approach. Taking the initial test script provided by `schmitts`, I extend it so that it tests for the presence of the `textbackslash` string (which shouldn't be there):
```Python
from brian2 import *
from sympy import latex

G = NeuronGroup(10, 'dv/dt = -v/(10*ms) : volt')
assert 'textbackslash' not in latex(G.equations)
```
Running this script will now either end quietly (and with an [exit code](https://en.wikipedia.org/wiki/Exit_status) 0), or fail with an `AssertionError` if the problem is present. After storing the script as `/tmp/sympy_latex.py`, I can now hand off the testing to `git bisect` which will go through all the commits in a smart way to find the first commit introducing the problem:
```console
$ git bisect run python /tmp/sympy_latex.py
```
This leads to quite a bit of output:
<details>
<summary>Full output</summary>
<pre>
running python /tmp/sympy_latex.py
Bisecting: 3205 revisions left to test after this (roughly 12 steps)
[de62108d34a1265cc1b2b9c5155d6070b842b672] Merge pull request #19508 from sachin-4099/gsoc#6
running python /tmp/sympy_latex.py
Bisecting: 1602 revisions left to test after this (roughly 11 steps)
[d3e5f14c5241b9da96560c4deffef9eaf4991228] Made parts of boolalg faster and a bit more pythonic
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_ikr3y3p0.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_u82neiv1.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 801 revisions left to test after this (roughly 10 steps)
[737a81874003f4a7169d266976a90cbd5dfaf2b4] TST ADD check minimal polynomials of problematic expression computed with both methods
running python /tmp/sympy_latex.py
Bisecting: 407 revisions left to test after this (roughly 9 steps)
[a8207569d13fad973bf9afb2772bd85ea6fa1c6e] Update array_derivatives.py
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_7g1_4r8w.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_ce1dkbau.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 196 revisions left to test after this (roughly 8 steps)
[87c9ea827f4b1b6cc34a7c707de1fd5d9819cb46] Merge pull request #19944 from eric-wieser/allow-custom-printers
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_t0clxwav.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_yvu9jtqi.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 96 revisions left to test after this (roughly 7 steps)
[87cca59f3507e1052631da0819edd0cfa1baadc0] Merge pull request #19742 from bjodah/logaddexp
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_tpz1qnjv.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_2dj31z0l.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 48 revisions left to test after this (roughly 6 steps)
[044c6e4c9d73d56ec862f060a87314c269d2e050] Merge pull request #19805 from goddus/14037_test
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_5lpmsekz.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_8jf447vd.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 29 revisions left to test after this (roughly 5 steps)
[3d6b5a44dff651642cb480797b0e265c0bf28357] Merge pull request #19713 from sylee957/fix_nested_frac_field
running python /tmp/sympy_latex.py
Bisecting: 14 revisions left to test after this (roughly 4 steps)
[36897bfd792170158ab762c908329ce688b0a4d0] Merge pull request #19753 from Soumi7/special
running python /tmp/sympy_latex.py
Bisecting: 8 revisions left to test after this (roughly 3 steps)
[a6e4cc52d3122996e4b0db96955f3c9cae0efd64] Merge pull request #19611 from eric-wieser/fix-latex-default
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_ptntb08b.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_fi72yrc1.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 2 revisions left to test after this (roughly 2 steps)
[d8941c4642f9974cfcb615a48934a0c5dbb4fe3a] Tweak documentation
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_1yuffecs.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_nt_tfg6o.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 0 revisions left to test after this (roughly 1 step)
[a4c7ebc6cb4de1fc9b36a63e78c151de38575021] Add a versionchanged directive
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_bxugu6c7.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_xs531o8q.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[27d64a4a644093b8f8a38a77466680302d2b4ee2] printing: Show unsupported types in monospace font
running python /tmp/sympy_latex.py
ERROR      Brian 2 encountered an unexpected error. If you think this is a bug in Brian 2, please report this issue either to the discourse forum at <http://brian.discourse.group/>, or to the issue tracker at <https://github.com/brian-team/brian2/issues>. Please include this file with debug information in your report: /tmp/brian_debug_6l75fq6r.log  Additionally, you can also include a copy of the script that was run, available at: /tmp/brian_script_718wjgs2.py Thanks! [brian2]
Traceback (most recent call last):
  File "/tmp/sympy_latex.py", line 6, in <module>
    assert 'textbackslash' not in latex(G.equations)
AssertionError
</pre>
</details>

and finally gives us the information we were looking for:

```console
27d64a4a644093b8f8a38a77466680302d2b4ee2 is the first bad commit
commit 27d64a4a644093b8f8a38a77466680302d2b4ee2
Author: Eric Wieser <wieser.eric@gmail.com>
Date:   Mon Jun 22 13:06:12 2020 +0100

    printing: Show unsupported types in monospace font

 sympy/printing/latex.py            | 41 +++++++++++++++++++++++++++++++-------
 sympy/printing/tests/test_latex.py | 30 ++++++++++++++++++++++++++--
 2 files changed, 62 insertions(+), 9 deletions(-)
bisect run success
```
This looks indeed very relevant, and the change in the [referenced commit](https://github.com/sympy/sympy/commit/27d64a4a644093b8f8a38a77466680302d2b4ee2) introduces the strange `\textbackslash` we were seeing.

Does this mean we have found a bug in `sympy`, or is there something to fix in Brian?

### Getting to the bottom of it
When I opened the github issue, I mentioned that converting a single equation (instead of the full `Equations` object) could be used as a workaround. Looking more closely, it turns out that this already gives incorrect output:
```python
print('$$' + latex(G.equations['v']) + '$$')
```
prints:
```latex
$$\frac{\mathrm{d}\mathtt{\text{v}}}{\mathrm{d}t} = - \frac{v}{10 ms}$$
```
While this doesn't look *that* bad (no weird `\textbackslash` for example), it wraps the $v$ on the left-hand side in the wrong way, making it use a typewriter font instead of the italics normally used for variables:
<div>
$$
\frac{\mathrm{d}\mathtt{\text{v}}}{\mathrm{d}t} = - \frac{v}{10 ms}
$$
</div>

Why does it correctly display $v$ on the right-hand side, but not on the left-hand side? The conversion to LaTeX is handled in the function [`SingleEquations._latex`](https://github.com/brian-team/brian2/blob/a0167fc35a585a0b58aa8cf28889a0e03a520696/brian2/equations/equations.py#L459), which currently looks like this:
```Python
    def _latex(self, *args):
        if self.type == DIFFERENTIAL_EQUATION:
            return (r'\frac{\mathrm{d}' + sympy.latex(self.varname) + r'}{\mathrm{d}t} = ' +
                    sympy.latex(str_to_sympy(self.expr.code)))
        elif self.type == SUBEXPRESSION:
            return (sympy.latex(self.varname) + ' = ' +
                    sympy.latex(str_to_sympy(self.expr.code)))
        elif self.type == PARAMETER:
            return sympy.latex(self.varname)
```
What is the difference between the left-hand side and the right-hand side that could explain the different rendering of the variable name? It turns out that for the right-hand side, we call `sympy.latex` on the result of the [`str_to_sympy`](https://brian2.readthedocs.io/en/stable/reference/brian2.parsing.sympytools.str_to_sympy.html) function, i.e. on a `sympy` object; in contrast, on the left-hand side, we call `sympy.latex` on a *string* (`self.varname`). Well, it is finally time to look at `sympy`'s documentation to see whether it has to say anything about that... indeed it does! Somewhat hidden at the end of the [documentation for `sympy.latex`](https://docs.sympy.org/latest/modules/printing.html#sympy.printing.latex.latex) we find the following sentence:

> *Changed in version 1.7.0:* Unsupported types no longer have their str representation treated as valid latex.

Ha! Apparently, until version 1.7, `sympy` was happily accepting simple strings as input to `sympy.latex` and simply expected them to be valid LaTeX code. Now, it instead tries to display them verbatim (replacing backslashes by `\textbackslash`, etc.) and in a typewriter font. So how can we fix this? Instead of calling `sympy.latex(self.varname)`, we call `sympy.latex(sympy.Symbol(self.varname))`, i.e. call `sympy.latex` on a `sympy` object instead of a pure string. What does `sympy.latex(sympy.Symbol(self.varname))` return if `self.varname` is `'v'`? Well, it simply returns `'v'`... Doesn't this mean we could simply use `self.varname` directly? We could, but we'd lose some of `sympy`'s features, e.g. `tau` would no longer be converted to `\tau` (i.e. $\tau$).

Now, how can we check that we are not using `sympy.latex` directly on strings elsewhere in the code? Of course we could search for calls to `latex` in the source code and verify them manually, but there's another neat trick we can use, so called ["monkey patching"](https://en.wikipedia.org/wiki/Monkey_patch).

I am going to run Brian's test suite, or at least the "codegen-independent" part, i.e. the part that does not test the full code generation machinery. Converting equations to LaTeX belongs into this category. However, before running this test I will "monkey patch" the `sympy.latex` function so that it fails if it gets called for a string – otherwise it does the same thing as the original function. Note that I have to do this before importing `brian2`, because otherwise `brian2` would important the original `sympy.latex` function before I can patch it. We also need to switch off [pytest](https://docs.pytest.org/)'s parallel testing, because otherwise tests will be executed in independent processes that do not make use of our carefully patched function.

Here's the patch and the test run:
```Python
from sympy import latex as _orig_latex
import sympy
def latex(obj, *args, **kwds):
    assert not isinstance(obj, str)
    return _orig_latex(obj, *args, **kwds)
sympy.latex = latex
import brian2
brian2.test([])  # no code generation targets are tested
```

Two of the tests fails and point us to another use of `sympy.latex` with a string in [`Equations._latex`](https://github.com/brian-team/brian2/blob/a0167fc35a585a0b58aa8cf28889a0e03a520696/brian2/equations/equations.py#L1047):
```Python
            # ...
            varname = sympy.Symbol(eq.varname)
            if eq.type == DIFFERENTIAL_EQUATION:
                lhs = r'\frac{\mathrm{d}' + sympy.latex(varname) + r'}{\mathrm{d}t}'
            else:
                # Normal equation or parameter
                lhs = varname
            # ...
            if eq.type == PARAMETER:
                eq_latex = r'%s &&& \text{(unit: $%s$%s)}' % (sympy.latex(lhs),                            
                                                              sympy.latex(get_unit(eq.dim)),
                                                              flag_str)
            else:
                eq_latex = r'%s &= %s && \text{(unit of $%s$: $%s$%s)}' % (sympy.latex(lhs), # ← PROBLEM
                                                                           sympy.latex(rhs),
                                                                           sympy.latex(varname),
                                                                           sympy.latex(get_unit(eq.dim)),
                                                                           flag_str)
            equations.append(eq_latex)

```
In the marked line above, we call `sympy.latex(lhs)`, but `lhs` is a string, not a sympy object (note that a couple of lines earlier, the `lhs` refers to `varname`, which despites its somewhat confusing name is a `sympy.Symbol` – this use is therefore correct). Including `lhs` as it is, instead of wrapping it with `sympy.latex` should therefore fix the issue.

### Final tests and commiting things
A manual test with the example from the beginning shows that it now prints
```latex
\begin{align*}\frac{\mathrm{d}v}{\mathrm{d}t} &= - \frac{v}{10 ms} && \text{(unit of $v$: $\mathrm{V}$)}\end{align*}
```
which renders correctly:
<div>
\begin{alignat}{4}
\frac{\mathrm{d}v}{\mathrm{d}t} &= - \frac{v}{10 ms} && \text{(unit of $v$: $\mathrm{V}$)}
\end{alignat}
</div>

Before commiting the fix, however, we should also make sure that this issue does not reappear in the future, i.e. we need a test. A good test for a bug should of course fail before applying the fix, and no longer fail afterwards. I already fixed the issue in the code, so what is the easiest way to make sure that it fails without these changes? There are several ways to do this, but in this case a simple solution is to run
```console
$ git stash
```
This resets all changes in the repository, but stores them locally. We can now write a test and make sure that it fails (because our repository does not have the fix anymore). The LaTeX output is currently not tested very well (but we don't want tests to fail due to small inconsequential layout changes, either), but for the moment very simple test should be enough. To make sure that the current issue is fixed, I simply add
```Python
assert 'textbackslash' not in func(G)  # for LaTeX, see #1296
#...
assert 'textbackslash' not in func(G.equations)
```
to the [`test_repr` test in `test_neurongroup.py`](https://github.com/brian-team/brian2/blob/a0167fc35a585a0b58aa8cf28889a0e03a520696/brian2/tests/test_neurongroup.py#L1396).

As expected, this fails in the current codebase, and after getting the fixes back from the "stash" with
```console
$ git stash pop
```
the test successfully passes.

This concludes everything. I finish by committing the changes in a new branch and open a [pull request](https://github.com/brian-team/brian2/pull/1299) so that they can be merged into the main code base.

## Final remarks

This was a small bug, but also quite typical in many ways: some "minor" feature of Brian (i.e. not something completely obvious that would get noticed by out users, us and our test suite immediately) used to work but no longer does. A user reported the issue, and we had to figure out whether we broke something in Brian, or whether one of our dependencies introduced a bug. The `git bisect` tool is great for figuring things like this out; here I applied it to `sympy` but in other situations I would have applied it to Brian's code base itself. The final outcome also was rather typical: Brian did something (arguably?) wrong, but in a way that worked fine with earlier versions of a dependency, in this case `sympy`. And in the end, the fixes were almost trivial, but finding them wasn't obvious from the start!

Hope that you learned a thing or two from reading this blog post, and maybe it motivates to fix a bug in Brian yourself! Comments very welcome, feel free to reach out on [twitter](https://twitter.com/briansimulator) or on the [discussion forum](https://brian.discourse.group).
