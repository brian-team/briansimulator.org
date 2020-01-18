<html><body><p>We have just released Brian 1.4.1, available from PyPI using  <strong>pip install -U brian</strong> or <strong>easy_install -U brian</strong>, or from the <a href="http://neuralensemble.org/trac/brian/downloader/download/release/19">NeuralEnsemble server</a>. It will be soon available in the <a href="http://neuro.debian.net/pkgs/python-brian.html">NeuroDebian repositories</a> as well, thanks to the <a href="http://neuro.debian.net/about.html#chap-team">NeuroDebian team</a>.

This is a minor release, but it adds a couple of useful features (including experimental features for the Synapses class) and fixes some important bugs, in particular for users of brian hears. A list of changes can be found below:

Major features:
</p><ul>
	<li>C extensions are compiled by default during installation (with a fallback to the Python version if compilation fails) -- this might lead to a considerable speedup for users who did not compile those extensions manually before. Note that this only includes installations based on running setup.py (including pip and easy_install), not the Windows .exe installer.</li>
</ul>
Minor features:
<ul>
	<li>Convenience methods for the Synapses class, allowing to save and load the connectivity and to convert the weights into a matrix</li>
	<li>A new openmp option to switch on the use of OpenMP pragmas in generated C code</li>
	<li>Brian hears: Two new models, MiddleEar (filtering by the middle ear) and ZhangSynapse (model of the IHC-AN synapse)</li>
	<li>Brian hears: New convenience functions to get reasonable axis ticks for logarithmic axes</li>
</ul>
Improvements:
<ul>
	<li>Brian's documentation is now also available under <a href="http://brian.readthedocs.org">brian.readthedocs.org</a></li>
	<li>ProgressReporter has context manager support (i.e. can be used in "with" statements)</li>
	<li>NeuronGroup and Synapses work with empty model specifications.</li>
	<li>C version of SpikeContainer is now picklable</li>
</ul>
Bug fixes:
<ul>
	<li>Synaptic equations referring to variables in the pre- or postsynaptic group are never considered as being linear (fixes ticket #83)</li>
	<li>Fix issue with static equations in synaptic models (see  <a href="https://groups.google.com/d/msg/briansupport/-/uqxLK_yoqKUJ">https://groups.google.com/d/msg/briansupport/-/uqxLK_yoqKUJ</a> )</li>
	<li>Make LinearStateUpdater pickable, even if array B is "NotImplemented".</li>
	<li>Fixed the bug in which the StateSpikeMonitor didn't record variables defined with a static equation.</li>
	<li>Important bug fixes for brian hears, all users are encouraged to update:</li>
<ul>
	<li>Make sure that LinearFilterbank copies it source and therefore not changes it (when not using weave) (fixes ticket #73)</li>
	<li>Fix some bugs in the TanCarney model</li>
	<li> Fix shifting multi-channel sounds with fractional=True (fixes ticket #80)</li>
</ul>
</ul>
Experimental features:
<ul>
	<li>C version of SpikeQueue (used in the Synapses class), which can lead to a considerable speedup (see "Advanced concepts/Compiled code" for instructions how to use it).</li>
	<li>Delays can be specified as a parameters of the Synapses model and then be changed dynamically.</li>
</ul></body></html>