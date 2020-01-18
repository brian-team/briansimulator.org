<html><body><p>We recently found a bug that may silently cause problems with many simulations. The bug causes problems in the following situation:
</p><ul>
	<li>You create a NeuronGroup</li>
	<li>You create a subgroup of that group</li>
	<li>You create a Connection from that subgroup</li>
	<li>The Connection has delays</li>
</ul>
In this case, the SpikeContainer object would be improperly initialised and many spikes may be lost. The latest development version fixes this. See <a href="http://neuralensemble.org/trac/brian/ticket/33">ticket #33</a> on our trac.

If you have code running on an older version and think your code might be affected, please get in contact on the <a href="mailto:briansupport@googlegroups.com">briansupport@googlegroups.com</a> list.</body></html>