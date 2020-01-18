<html><body><p>We have just released <a href="https://neuralensemble.org/trac/brian/wiki/Downloads">Brian 1.2.1</a>.

This is mostly a bug fixing release, and minor new features. One highlight is the new remote control system which allows you to interact with a Brian script as it is running - e.g. changing parameter values, plotting intermediate results, etc. Also, GPU support on 64 bit and Linux machines is now much better.

Major features:

* New remote controlling of running Brian scripts via RemoteControlServer
and RemoteControlClient.

Minor features:

* New module tools.io
* weight and sparseness can now both be functions in connect_random
* New StateHistogramMonitor object
* clear now has a new keyword all which allows you to destroy all Brian
objects regardless of whether or not they would be found by MagicNetwork.
In addition, garbage collection is called after a clear.
* New method StateMonitor.insert_spikes to have spikes on voltage traces.

Improvements

* The sparseness keyword in connect_random can be a function
* Added 'wmin' to STDP
* You can now access STDP internal variables, e.g. stdp.A_pre, and monitor
them by doing e.g. StateMonitor(stdp.pre_group, 'A_pre')
* STDP now supports nonlinear equations and parameters
* refractory can now be a vector (see docstring for NeuronGroup) for constant
resets.
* modelfitting now uses playdoh library
* C++ compiled code is now much faster thanks to adding -ffast-math switch to
gcc, and there is an option which allows you to set your own
compiler switches, for example -march=native on gcc 4.2+.
* SpikeGeneratorGroup now has a spiketimes attribute to reset the list of
spike times.
* StateMonitor now caches values in an array, improving speed for M[i] operation
and resolving ticket #53

Bug fixes

* Sparse matrices with some versions of scipy
* Weave now works on 64 bit platforms with 64 bit Python
* Fixed bug introduced in 1.2.0 where dense DelayConnection structures would
not propagate any spikes
* Fixed bug where connect* functions on DelayConnection didn't work with
subgroups but only with the whole group.
* Fixed bug with linked_var from subgroups not working
* Fixed bug with adding Equations objects together using a shared base equation
(ticket #9 on the trac)
* unit_checking=False now works (didn't do anything before)
* Fixed bug with using Equations object twice (for two different NeuronGroups)
* Fixed unit checking bug and ZeroDivisionError (ticket #38)
* Fixed rare problems with spikes being lost due to wrong size of SpikeContainer,
it now dynamically adapts to the number of spikes.
* Fixed ticket #5, ionic_currents did not work with units off
* Fixed ticket #6, Current+MembraneEquation now works
* Fixed bug in modelfitting : the fitness was not computed right with CPUs.
* Fixed bug in modelfitting with random seeds on Unix systems.
* brian.hears.filtering now works correctly on 64 bit systems

Removed features

* Model has now been removed from Brian (it was deprecated in 1.1).</p></body></html>