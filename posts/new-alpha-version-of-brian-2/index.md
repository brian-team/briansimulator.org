<html><body><p>We are happy to announce another alpha release of Brian2 (version number 2.0a8). A significant amount of internal refactoring work has been done since the previous release and many bugs (in particular related to the new "standalone" mode) have been fixed. The release also adds the following user-visible changes:</p>

<ul>
<li>The definition of variable namespaces is now finalized and follows a consistent approach, see <a href="http://brian2.readthedocs.org/en/latest/user/equations.html#external-variables-and-functions">the documentation</a> for details</li>
<li>A variable marked as "unless refractory" in the equations is now completely clamped during refractoriness, i.e. it also ignores synaptic input, for example</li>
<li>Pre-defined constants (e.g. "e" or "pi") are now correctly understood in the symbolic analysis of equations</li>
<li>Parameters and subexpressions can be declared as "scalar", meaning that they should be stored/calculated as a single value for a whole group</li>
<li>Exact integration can now take place even for equations referring to a TimedArray, if the timestep of the TimedArray is a multiple of the simulation timestep</li>
<li>The internal calculation of TimedArray values is now more robust. The new approach entails a change in the semantics of TimedArray when its timestep is bigger than the simulation timestep. For more details see <a href="http://brian2.readthedocs.org/en/latest/user/input.html#timed-arrays">the documentation</a></li>
<li>Performance improvement for the Python-based SpikeQueue</li>
</ul>
<p>Brian 2 is stabilizing and can already be used for quite a variety of network simulations. We ported a rather complex example from Brian 1 (<code>synapses_barrelcortex.py</code>) that shows a lot of Brian2's features in use.</p>

<p>As always, please report any comments to the <a href="http://groups.google.com/group/brian-development/">brian-development mailing list</a> or open an issue on the <a href="https://github.com/brian-team/brian2/issues">github repository</a>.</p>

<h2>How to get Brian2?</h2>

<p>Brian2 is available on the <a href="https://pypi.python.org/pypi/Brian2">python package index</a>, therefore  you can install it using easy_install or pip:</p>
<code>
    easy_install brian2
    pip install brian 2  # for older versions of pip
    pip install --pre brian2  # for newer versions of pip
</code>
Alternatively, you can directly download the package from the package index and install it yourself using <code>python setup.py install</code> (if you are using Python 2.x, simply running it from the source directory also works).

<p>Finally, you can also clone the git repository at:<br>
<a href="https://github.com/brian-team/brian2">https://github.com/brian-team/brian2</a></p>

<p>Note that the package is called brian2, not brian, therefore it does not interfere with an existing Brian installation and trying out Brian2 will not affect your existing Brian simulations.</p>

<h2>Documentation</h2>
<p>You can find documentation for Brian2 at readthedocs: <a href="http://brian2.readthedocs.org">http://brian2.readthedocs.org</a></p>
    
<p>Note that the user documentation is still quite incomplete, you'll find a lot of information in the reference documentation, though.</p></body></html>