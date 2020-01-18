<html><body><p>We are seeking collaborators to help us with the Brian project. If you are interested in joining the educational team (writing tutorials and examples), the testing team (writing tests and benchmarking) or the development team (working on job scheduling and visualization modules, developing the library), please contact us by <a href="mailto:romain@briansimulator.org">email</a>. You should also have a look at our <a href="http://groups.google.fr/group/brian-development">developers mailing list</a>.

<strong>Educational team</strong>
</p><ul>
	<li>Write tutorials.</li>
	<li>Write examples. We are especially interested in examples adapted from published papers.</li>
</ul>
<strong>Testing team</strong>

The testing team consists of testers and profilers:
<ul>
	<li><em>Tester</em>: write tests that verify that all components of Brian work as expected. The package currently contains a number of tests that we run regularly to make sure that we haven't broken anything. This is extremely important to make Brian reliable.</li>
	<li><em>Profiler</em>: write benchmarks to evaluate Brian's speed. We are particularly interested in finding the efficiency bottlenecks that we should be working on.</li>
</ul>
<strong>Development team</strong>

There are several projects for which we welcome contributors:
<ul>
	<li><em>Parallel computing: </em>this is a major project within Brian.     We are currently considering 4 subtasks:
<ul>
	<li>Job scheduling: currently, Brian can run independent simulations on multiple processors and computers by using parallelpython, but it is limited. We would like to make this type of distributed simulations simple. This might simply involve using existing (free) tools such as <a href="http://www.cs.wisc.edu/condor/">Condor</a> and writing specific tutorials and usage examples.</li>
	<li>GPU computing: we have started working on using the GPU as a coprocessor to run the state updates in Brian simulations, which could result in considerable speed-ups. We are welcoming collaborators on this project. Have a look at our <a href="http://groups.google.fr/group/brian-on-gpu">mailing list on GPU development </a>if you are interested.</li>
	<li>Multicore and cluster computing: we have not developed this aspect yet, but please send us an email if you are interested in helping us.</li>
</ul>
</li>
	<li><em>Library:</em>we would like to include a library of ionic channels; any other type of predefined models would be welcome too.</li>
	<li><em>Plotting and visualisation:</em> currently, Brian relies almost entirely on Pylab for the graphics. We would like to develop more specific tools, both for creating publication-ready figures/movies and for online visualisation (visualising model activity as the simulation runs).</li>
	<li><em>Analysis:</em> Brian currently includes a module for simple spike train statistics. It would be good to have more analysis functions (for example porting the <a href="http://neuroanalysis.org/toolkit/releases/1.0g/">Spike Train Analysis Toolkit</a>).</li>
	<li><em>C++ code: </em>we are considering writing some of the key classes (such as connection structures) in C++ to increase Brian's speed. This could use SWIG for example.</li>
	<li><em>Error catching:</em> errors in Brian scripts can sometimes be mysterious. The idea here is to write more useful error messages, possibly by defining new exception types and catching errors at relevant points in the code.</li>
</ul></body></html>