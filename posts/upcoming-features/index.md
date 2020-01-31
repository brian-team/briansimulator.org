<html><body><p>At the moment, we're working on these features for Brian 1.1.3 which should be coming very soon:
</p><ul>
	<li>STDP working with connections with heterogeneous delays.</li>
	<li>A new RecentStateMonitor for storing only the most recent values of a variable.</li>
	<li>A new TimedArray class to make it easier to set the values of a variable in an equation from a precomputed array.</li>
	<li>Progress reporting for simulation runs, with estimates of how long the computation will take.</li>
</ul>
In the medium term, possibly for Brian 1.2, we're working on:
<ul>
	<li>Support for parallel processing with a GPU - the work in progress on this is already available in the experimental subpackage in Brian.</li>
	<li>Support for automatic generation and compilation of C code for nonlinear differential equation solvers.</li>
	<li>A subpackage, "Brian hears", for auditory system modelling, including efficient GPU based filterbank operations.</li>
</ul></body></html>