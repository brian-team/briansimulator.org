<html><body><p>We are very pleased to announce the release of version 2.0 of the Brian neural network simulator.

Brian is a free, open source simulator for spiking neural networks. It is written in the Python programming language and is available on almost all platforms. We believe that a simulator should not only save the time of processors, but also the time of scientists. Brian is therefore designed to be easy to learn and use, highly flexible and easily extensible.

You can learn more about Brian from our <a href="https://briansimulator.org">front page</a>. You can also try out Brian from your web browser, without having to install any software, using our <a href="https://mybinder.org/repo/brian-team/brian2-binder/notebooks/demo.ipynb">interactive demo</a>.
</p><h4>Major new features in 2.0</h4>
<ul>
 	<li>Much more flexible model definitions. The behaviour of all model elements can now be defined by arbitrary equations specified in standard mathematical notation.</li>
 	<li>Code generation as standard. Behind the scenes, Brian automatically generates and compiles C++ code to simulate your model, making it much faster.</li>
 	<li>"Standalone mode". In this mode, Brian generates a complete C++ project tree that implements your model. This can be then be compiled and run entirely independently of Brian. This leads to both highly efficient code, as well as making it much easier to run simulations on non-standard computational hardware, for example on robotics platforms.</li>
 	<li>Multicompartmental modelling.</li>
 	<li>Python 2 and 3 support.</li>
</ul>
That's just a small fraction of the new features in 2.0, take a look at the <a href="https://brian2.readthedocs.io/en/stable/introduction/release_notes.html">full list</a>.
<h4>Upgrading from Brian 1.4</h4>
Brian 2 is a rewrite from scratch, and introduces some backwards incompatible changes. In most cases, these should be relatively simple. We've written a <a href="https://brian2.readthedocs.io/en/stable/introduction/changes.html">detailed guide on how to update your simulations</a>. Note that you can have both Brian 1 and Brian 2 installed simultaneously, so you can switch gradually.
<h4>Thanks</h4>
Brian 2 was written by Marcel Stimberg, Dan Goodman and Romain Brette.

Do please remember to cite Brian if you use it for your research.

We would also like to thank the large number of users (over 40) who contributed code, bug reports, etc.</body></html>
