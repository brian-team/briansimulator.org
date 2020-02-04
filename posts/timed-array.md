<html><body><p>Please see the entry on <a href="https://briansimulator.org/2009/05/27/the-idea/">the idea</a> of this development blog.

One annoying thing that crops up often in writing programs for Brian, is that you have some set of equations with a parameter which varies over time according to the values in some array. Supposing that I was an array of length N with values sampled at intervals dt, you would like to be able to write an equation like:

[python]
I = randn(N)
eqs = '''
dV/dt = (-V+I(t))/tau : 1
'''
[/python]
One way of solving the problem is to use a network operation, like so:

[python]
I = randn(N)
eqs = '''
dV/dt = -(V+J)/tau : 1
J : 1
'''
G = NeuronGroup(m, eqs, ...)
@network_operation
def update_J(clk):
    i = int(clk.t/clk.dt)
    G.J = I[i]
[/python]
This works, but it's not terribly intuitive. The new TimedArray class allows you to do both of these things. The first could be written like so:

[python]
I = TimedArray(randn(N))
eqs = '''
dV/dt = (-V+I(t))/tau : 1
'''
[/python]
The second like so:

[python]
I = randn(N)
eqs = '''
dV/dt = -(V+J)/tau : 1
J : 1
'''
G = NeuronGroup(m, eqs, ...)
G.J = TimedArray(I)
[/python]
Behind the scenes, the first one works by adding a __call__ method to numpy arrays which interpolates. The second one works by adding a network operation to the network. The first breaks linearity and so nonlinear solvers are always used, so if your equations are linear, the second is probably better to use.

TimedArray has several options, including the use of evenly sampled grid points based on a start time and dt (given by a clock by default), or a fixed array of times which needn't be evenly sampled. For example to turn a signal on between 1 second and 1.1 second you could do:

[python]
times = [0*second, 1*second, 1.1*second]
values = [0, 1, 0]
x = TimedArray(values, times)
[/python]
The TimedArray class is defined in the module timedarray. Take a look at the documentation, try some examples, and let us know what you think.</p></body></html>
