<html><body><p>We just added a new feature for building sparse connections: the sparseness keyword now accepts functions in the same way as the weight keyword, e.g.:

[python]
myconnection.connect_random(group1,group2,0.1,weight=1*nS,sparseness=exp(-abs(i-j)*.1))
[/python]

makes random synapses between neurons with a distance-dependent probability (assuming the neurons are topographically arranged, with a linear topology).</p></body></html>