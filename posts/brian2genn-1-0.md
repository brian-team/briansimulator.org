<html><body><p>We are proud to announce the release of <strong>Brian2GeNN</strong>, the Brian 2 interface to the <a href="http://genn-team.github.io/genn/">GPU-enhanced Neuronal Network (GeNN)</a> simulator. With this interface, a Brian 2 script (as long as it only uses <a href="http://brian2genn.readthedocs.io/en/latest/introduction/exclusions.html">supported features</a>) can benefit from the potential performance benefits of a GPU by adding just two lines to the start of the script:
<code>
import brian2genn
set_device('genn')
</code>

Brian2GeNN can be installed from the same Anaconda repository channel as Brian itself:

<code>conda install -c brian-team brian2genn</code>

This installation method will also include the GeNN simulator, while an installation from PyPI (via <code>pip install brian2genn</code>) will require a manual installation of GeNN. See the <a href="http://brian2genn.readthedocs.io">documentation (http://brian2genn.readthedocs.io)</a> for more details.

Note that in all cases, users need a CUDA-capable NVIDIA GPU and a manual installation of the CUDA SDK.

The actual performance benefits of using a GPU to run the simulation depend strongly on the details of the model but can be significant. With the Brian2GeNN package, we hope to make it as easy as possible for users to try it out for themselves.

In case you run into problems with the installation of the package or with its use, please contact us at brian-development@googlegroups.com or open an issue on the <a href="https://github.com/brian-team/brian2genn/issues">Brian2GeNN bug tracker</a>.</p></body></html>