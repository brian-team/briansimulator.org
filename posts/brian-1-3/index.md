<html><body><p>The 1.3 release of Brian is out!

The major change in this version is the addition of the<a href="http://www.briansimulator.org/docs/hears.html"> Brian.hears package for auditory modelling</a>. This version also includes an update to the toolbox for fitting neural models to electrophysiological recordings (which now uses version 0.3 of the parallel optimization package <a href="http://code.google.com/p/playdoh/">Playdoh</a>), remote control of Brian scripts, and experimental support for code generation for C and GPU. There are also a number of other new features, bug fixes and improvements (full list below).

Brian is also available from the <a href="http://neuro.debian.net/pkgs/python-brian.html">NeuroDebian repository</a>: pre-packaged for all recent Debian and Ubuntu releases.

Brian is being developed by Romain Brette and Dan Goodman. This version also includes contributions by Bertrand Fontaine, Cyrille Rossant, Victor Benichoux and Boris Gourévitch.
</p><h3>New features since 1.2.1</h3>
<h4>Major features</h4>
<ul>
	<li>Added Brian.hears auditory library</li>
</ul>
<h4>Minor features</h4>
<ul>
	<li>Added new brian.tools.datamanager.DataManager, moved from brian.experimental</li>
	<li>reinit(states=False) will now not reset NeuronGroup state variables to 0.</li>
	<li>modelfitting now has support for refractoriness</li>
	<li>New examples in misc: after_potential, non_reliability, reliability,</li>
	<li> van_rossum_metric, remotecontrolserver, remotecontrolclient</li>
	<li>New experimental.neuromorphic package</li>
	<li>Van Rossum metric added</li>
</ul>
<h4>Improvements</h4>
<ul>
	<li>SpikeGeneratorGroup is faster for large number of events ("gather" option).</li>
	<li>Speed improvement for pure Python version of sparse matrix preparation</li>
	<li>Speed improvements for spike propagation weave code (50-100% faster).</li>
	<li>Clocks have been changed and should now behave more predictably. In addition, you can now specify an order attribute for clocks.</li>
	<li>modelfitting is now based on playdoh 0.3</li>
	<li>modelfitting can now use euler/exp.euler or RK2 integration schemes</li>
	<li>Loading AER data is much faster</li>
	<li>Freezing now uses higher precision (used to only use 12sf now uses 17sf)</li>
</ul>
<h4>Bug fixes</h4>
<ul>
	<li>Bug in STDP with small values for wmin/wmax fixed (ticket #63)</li>
	<li>Equations/aliases now work correctly in STDP (ticket #56)</li>
	<li>Bug in sparse matrices introduced in scipy 0.8.0 fixed</li>
	<li>Bug in TimedArray when dt keyword is used now fixed (thanks to Adrien Wohrer for pointing out the bug).</li>
	<li>Units now work correctly in STDP (ticket #60)</li>
	<li>STDP raises an error if operations are reordered (ticket #57)</li>
	<li>linked_var works with static vars (equations) (ticket #68)</li>
	<li>Changing clock.t during a run won't end the run</li>
	<li>Fixed ticket #66 (unit bug)</li>
	<li>Fixed ticket #64 (bug with freeze)</li>
	<li>Can now run a network with no group</li>
	<li>Exception handling now works properly for C version of circular spike container</li>
	<li>ccircular now builds correctly on linux and 64 bit</li>
</ul>
<h4>Internal changes</h4>
<ul>
	<li>brian.connection deprecated and replaced by subpackage brian.connections, making the code structure much more straightforward and setting up for future work on code generation, etc.</li>
</ul></body></html>