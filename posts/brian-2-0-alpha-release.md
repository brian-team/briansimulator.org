<html><body><p>We are proud to announce the alpha release of Brian2, the successor of Brian, everyone's favourite neural simulator.</p>

<p>This is an alpha release, therefore many features are still missing and there are very likely many bugs. The main reason for this release is to get feedback from users, the only way to make sure that the final version will be as useful to everyone as possible.</p>

<p>This release is the cumulation of work that started more than one year ago, a basic rewrite of Brian that tries to keep and extend the strengths of Brian (ease of use, flexibility) while building it on a new foundation of a code generation framework that will allow for exciting new applications in the future.</p>
<h2>How to get Brian2?</h2>
<p>Brian2 is available on the <a href="https://pypi.python.org/pypi/Brian2">python package index</a>, therefore you can install it using easy_install or pip:</p>
<code>easy_install brian2
pip install --pre brian2</code>

<p>Alternatively, you can directly download the package from the package index and install it yourself using <code>python setup.py install</code> (if you are using Python 2, simply running it from the source directory also works).</p>

<p>Finally, you can also clone the git repository at:
<a href="https://github.com/brian-team/brian2">https://github.com/brian-team/brian2</a></p>

<p>Note that the package is called <b>brian2</b>, not <b>brian</b>, therefore it does not interfere with an existing Brian installation and trying out Brian2 will not affect your existing Brian simulations.</p>
<h2>Documentation</h2>
<p>You can find documentation for Brian2 at readthedocs: <a href="http://brian2.readthedocs.org">http://brian2.readthedocs.org</a></p>

<p>Note that the user documentation is still quite incomplete, you'll find a lot of information in the reference documentation, though.</p>
<h2>Feedback wanted!</h2>
<p>This is an alpha release, so there is still a lot that will change in the next months. However, the syntax is already mostly the way we plan it to be. Please provide feedback if you find something unintuitive or you fail to see how to express something that you could express in Brian1. For the feedback, please use either the <a href="http://groups.google.com/group/brian-development/">brian-development mailing list</a> or the <a href="https://github.com/brian-team/brian2/issues">github issues</a>. Note that the *internal* code (e.g. the interface to the code generation framework) will still change quite a bit.</p>
<h2>Known issues</h2>
<ul>
	<li>Brian hears and the modelfitting toolbox have not yet been ported to Brian2</li>
	<li>Brian2 is not yet optimised for performance. In particular, setting up a simulation or using multiple run statements might appear to be slow because a lot of work is unnecessarily repeated. For the simulation itself, a big performance increase can be often achieved by switching on C++ code generation by using the following in the code: <code>brian_prefs.codegen.target = 'weave'</code></li>
	<li>When using the ipython notebook, importing brian2 makes a lot of debug outputs appear under certain circumstances (<a href="https://github.com/brian-team/brian2/issues/133">#133</a>)</li>
	<li>Many error messages are not yet as helpful as they could be</li>
	<li>Various other known issues can be found in the <a href="https://github.com/brian-team/brian2/issues">issue tracker</a></li>
</ul>
</body></html>