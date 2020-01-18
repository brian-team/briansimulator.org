<html><body><p>We have just released <a href="https://neuralensemble.org/trac/brian/wiki/Downloads">Brian 1.2</a>.

The major feature of this release is the model fitting toolbox, designed for automatic fitting of spiking neural models to recorded data. The toolbox is capable of using multiple CPUs or GPUs, across multiple machines. For example, in our lab we use 3 computers with 2 GPUs each to get a 300x speed increase compared to using a single CPU.

Other features of this release include some support for real time plotting as the simulation runs and some important bug fixes. See below for the complete list of changes.

With this release, we are moving away from the old Sourceforge site to the new <a href="https://neuralensemble.org/trac/brian/wiki">Brian Trac</a> kindly hosted by <a href="http://www.neuralensemble.org/">Neural Ensemble</a>. We have also been working on our release tools, making it much easier to produce new releases. We now plan to do fairly frequent 'quick releases' which will be less thoroughly tested, but useful for those who want the latest features without having to much around with the SVN version.

Major features:
</p><ul>
	<li>Model fitting toolbox (library.modelfitting)</li>
</ul>
Minor features:
<ul>
	<li>New real-time ``refresh=`` options added to plotting functions</li>
	<li>Gamma factor in utils.statistics</li>
	<li>New RegularClock object</li>
	<li>Added brian_sample_run function to test installation in place of nose tests</li>
</ul>
Improvements:
<ul>
	<li>Speed improvements to monitors and plotting functions</li>
	<li>Sparse matrix support improved, should work with scipy versions up to 0.7.1</li>
	<li>Various improvements to brian.hears (still experimental though)</li>
	<li>Parameters now picklable</li>
	<li>Made Equations picklable</li>
</ul>
Bug fixes:
<ul>
	<li>Fixed major bug with subgroups and connections (announced on webpage)</li>
	<li>Fixed major bug with multiple clocks (announced on webpage)</li>
	<li>No warnings with Python 2.6</li>
	<li>Minor bugfix to TimedArray caused by floating point comparisons</li>
	<li>Bugfix: refractory neurons could fire in very extreme circumstances</li>
	<li>Fixed bug with DelayConnection not setting max_delay</li>
	<li>Fixed bug with STP</li>
	<li>Fixed bug with weight=lambda i,j:rand()</li>
</ul>
New examples:
<ul>
	<li>New multiprocessing examples</li>
	<li>Added polychronisation example</li>
	<li>Added modelfitting examples</li>
	<li>Added examples of TimedArray and linked_var</li>
	<li>Added examples of using derived classes with Brian</li>
	<li>Realtime plotting example</li>
</ul></body></html>