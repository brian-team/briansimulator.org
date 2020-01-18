<html><body><p>The 1.4 release of Brian is out!

The major change in this version is the addition of a new Synapses class, which allows modeling everything synaptic: gap junctions, probabilistic synapses, nonlinear synapses, plasticity, etc. There are also a number of other new features, bug fixes and improvements (see below).

Brian is being developed by Romain Brette and Dan Goodman. This version also includes contributions by Bertrand Fontaine, Cyrille Rossant, Victor Benichoux, Marcel Stimberg and Jonathan Laudanski.

We take advantage of this announcement to inform Brian users that we are currently discussing the development of Brian 2.0, a rewriting of Brian, intended to be simpler, faster, and to be able to run on external devices (e.g. GPU). We will make an announcement on our <a href="http://groups.google.fr/group/briansupport">mailing list </a>soon, where we will ask for user opinions.

<strong>New features since 1.3.1</strong>

Major features:
</p><ul>
	<li>New Synapses class (plasticity, gap junctions, nonlinear synapses, etc)</li>
</ul>
Minor features:
<ul>
	<li>New AERSpikeMonitor class</li>
	<li>Several updates to library.electrophysiology</li>
</ul>
Improvements:
<ul>
	<li>Units should work better with static code analysers now</li>
	<li>Added Network.remove</li>
	<li>SpikeMonitor has a new .it attribute (returns pair i, t of arrays of spike times)</li>
	<li>Many new examples</li>
</ul>
Bug fixes:
<ul>
	<li>Assigning to a static variable (equation) now raise an error</li>
	<li>Fixed issues for TimedArrays with explicitly set times (fixes ticket #81)</li>
	<li>Fixed bug, repr and str didn't work for Sound</li>
	<li>Fixed bug where tone(array_of_frequencies, ...)</li>
	<li>Fixed SparseConnectionMatrix bug suggested by Owen Mackwood</li>
	<li>Fixed bug in Parameters reported by Jimmy Bonaiuto</li>
	<li>Fixed bug with contained_objects reported by Oleg Sinyavskiy</li>
	<li>Units __repr__ and __str__ fixes</li>
	<li>Sound.spectrum, Sound.pinknoise, brownnoise</li>
	<li>t wasn't available in StringReset and PythonThreshold</li>
</ul>
Deprecated or removed features:
<ul>
	<li>MultipleSpikeGeneratorGroup</li>
	<li>experimental.coincidence_detection</li>
</ul>
Experimental features:
<ul>
	<li>Generating model documentation automatically (experimental.model_documentation)</li>
</ul>
 </body></html>