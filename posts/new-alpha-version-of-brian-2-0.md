<html><body><p>We are happy to announce another alpha release of Brian2 (version number 2.0a5) which adds a new feature for testing: C++ standalone simulations.</p>

<p>Standalone mode is a new addition to Brian2 with no equivalent in Brian1. It takes a simulation script and generates a directory of completely Brian-independent C++ files from it that perform the simulation. This can give significant performance advantages over the standard Brian simulation mode and also allows to do simulations on devices where Brian or one of its dependencies is not available (e.g. on a computing cluster or in robotics applications).</p>

<p>This mode has some restrictions compared to the standard operating mode of Brian, you can find more details in the documentation:<br>
<a href="http://brian2.readthedocs.org/en/latest/user/devices.html">http://brian2.readthedocs.org/en/latest/user/devices.html</a></p>

<p>We are very interested in feedback about how this mode fits with your needs, what restrictions you cannot live with, what additional functionality you'd need, etc. Please report any comments to the <a href="http://groups.google.com/group/brian-development/">brian-development mailing list</a></p>

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