<html><body><p>We are happy to announce another alpha release of Brian2 (version number 2.0a7). Major changes introduced since the last release:</p>

<ul>
<li>A workaround that makes Brian2 work with the latest version of sympy (0.7.4) which introduced a bug in their differential equation solver.</li>
<li>A C++ version of the SpikeQueue, the data structure responsible for the spike transmission. This feature needs a working C++ compiler and will lead to a performance gain.</li>
<li>Faster synapse updates in pure numpy/Python for STDP-like rules</li>
<li>A more flexible approach for importing the brian2 package that should allow for different programming styles (see <a href="http://brian2.readthedocs.org/en/latest/introduction/import.html">the documentation</a>).</li>
</ul>
<p>Please report any comments/questions you may have to the <a href="http://groups.google.com/group/brian-development/">brian-development mailing list</a></p>

<h2>How to get Brian2?</h2>
<p>Brian2 is available on the <a href="https://pypi.python.org/pypi/Brian2">python package index</a>, therefore  you can install it using easy_install or pip:</p>
<code>easy_install brian2
pip install brian 2  # older versions of pip
pip install --pre brian2  # newer versions of pip
</code>
<p>Alternatively, you can directly download the package from the package index and install it yourself using <code>python setup.py install</code> (if you are using Python 2.x, simply running it from the source directory also works).</p>
    
<p>Finally, you can also clone the git repository at:<br>
<a href="https://github.com/brian-team/brian2">https://github.com/brian-team/brian2</a></p>

<p>Note that the package is called brian2, not brian, therefore it does not interfere with an existing Brian installation and trying out Brian2 will not affect your existing Brian simulations.</p>

<h2>Documentation</h2>
<p>You can find documentation for Brian2 at readthedocs: <a href="http://brian2.readthedocs.org">http://brian2.readthedocs.org</a></p>
    
<p>Note that the user documentation is still quite incomplete, you'll find a lot of information in the reference documentation, though.</p></body></html>