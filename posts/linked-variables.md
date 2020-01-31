<html><body><p>Please see the entry on <a href="/posts/the-idea/">the idea</a> of this development blog.

One thing we end up doing very often in Brian in our code, is copying the values of a variable in one group to the values of a variable in another group. That is, a variable from one group should essentially be defined as the same as the variable from another group. This comes up in models of the auditory system we're working on, because we use one NeuronGroup to represent the displacement of hair cells in the cochlea, and a separate NeuronGroup to represent the auditory nerve fibres which receive graded rather than spiking inputs from them. In general, the same thing might be useful in any case where there is a graded rather than spiking connection between two NeuronGroups. What we were doing was this:

[python]
haircells = NeuronGroup(...)
nervefibres = NeuronGroup(...)
@network_operation(when='start')
def graded_connection():
    nervefibres.input = haircells.output
[/python]

This works fine, but generally we think using network operations in this technical sort of a way is not very intuitive for most users, so we thought about a way of doing this automatically with a nice syntax. We came up with this:

[python]
nervefibres.input = linked_var(haircells, 'output')
[/python]

The practical effect of this is exactly the same as the code above, but the syntax is much nicer. Behind the scenes, the function linked_var creates a LinkedVar class instance which is recognised by the __setattr__ method of the NeuronGroup, which creates a network operation to do the copy, but you didn't want to know that.

The question is, what should the syntax be? At the moment, we've gone with:

[python]
linked_var(source, var, func, when, clock)
[/python]

The func, when and clock arguments are optional. The func argument allows you to pass the value of the variable in the source group through a function. For example, in the auditory system you do half wave rectification and logarithmic compression. The when argument tells it when to do the copy operation, at the start of the simulation loop by default, and the clock tells it what schedule to update on, by default it uses the target group's clock. Is this a nice syntax? Is there anything else this should be able to do?</p></body></html>
