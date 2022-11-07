<!--
.. title: Software ecosystem
.. slug: ecosystem
.. type: text
-->

Below is a list of packages that build on Brian, either from us, colleagues we've worked with, or entirely separate
groups. If you have written a package using Brian and it's not listed here, let us know!

## Brian team

<ul class="list-group list-group-flush">
    <li class="list-group-item">
        <h3><a href="http://brian2cuda.readthedocs.io/">brian2cuda</a></h3>
        Brian 2 device that generates CUDA code for simulations on GPUs. Supports all features that are supported
        by the C++ standalone device, and can accelerate simulations by orders of magnitudes
        (<a href="https://www.frontiersin.org/articles/10.3389/fninf.2022.883700/full">Brian2CUDA paper</a>).
    </li>
    <li class="list-group-item">
        <h3><a href="http://brian2genn.readthedocs.io/">brian2genn</a></h3>
        Brian 2 frontend to the
        <a href="http://genn-team.github.io/genn/">GPU-enhanced neural network simulator (GeNN)</a>. Allows you to
        run Brian models on GPU up to 400x faster
        (<a href="https://www.nature.com/articles/s41598-019-54957-7">Brian2GeNN paper</a>).
    </li>
    <li class="list-group-item">
        <h3><a href="https://brian2modelfitting.readthedocs.io/en/stable/">brian2modelfitting</a></h3>
        Model Fitting Toolbox for Brian 2 simulator, to allow the user to find the best fit of the parameters for
        recorded traces and spike trains.
    </li> 
    <li class="list-group-item">
        <h3><a href="https://brian2hears.readthedocs.io/en/stable/">brian2hears</a></h3>
        Brian hears is an auditory modelling library for Python.
    </li> 
    <li class="list-group-item">
        <h3><a href="https://brian2tools.readthedocs.io/en/stable/">brian2tools</a></h3>
        The brian2tools package is a collection of useful tools for the Brian 2 simulator.
    </li> 
</ul>

<p>&nbsp;</p>

## Third party packages

<ul class="list-group list-group-flush">
    <li class="list-group-item">
        <h3><a href="https://github.com/EPFL-LCN/neuronaldynamics-exercises">Neuronal Dynamics Exercises</a></h3>
        This repository contains python exercises accompanying the book
        <a href="http://neuronaldynamics.epfl.ch/">Neuronal Dynamics</a> by Wulfram Gerstner, Werner M. Kistler,
        Richard Naud and Liam Paninski. 
    </li>
    <li class="list-group-item"> 
        <h3><a href="https://github.com/ProjectPyRhO/PyRhO">PyRhO</a></h3>
        A virtual optogenetics laboratory (<a href="http://journal.frontiersin.org/article/10.3389/fninf.2016.00008/full">paper</a>).
    </li>
    <li class="list-group-item">
        <h3><a href="https://cxsystem2.readthedocs.io/en/latest/">CxSystem2</a></h3>
        CxSystem2 is a simulation framework for cortical networks, which operates on personal computers. It is
        implemented in Python on top of the popular Brian2 simulator, and runs on Linux, Windows and MacOS. There is
        also a web-based version available via the Human Brain Project Brain Simulation Platform (BSP).
    </li>
    <li class="list-group-item">
        <h3><a href="https://snntoolbox.readthedocs.io/en/latest/">SNN toolbox</a></h3>
        The SNN conversion toolbox contains functions to transform rate-based artificial neural networks into spiking
        neural networks, and to simulate them. 
    </li>
    <li class="list-group-item">
        <h3><a href="https://github.com/BackyardBrains/NeuroRobot">NeuroRobot</a></h3>
        A neurorobot is a robot controlled by a computer simulation of a biological brain. At Backyard Brains we use
        neurorobots to teach computational neuroscience in high schools. This repository contains all the Matlab and
        Arduino code needed to run our neurorobots. If you haven't got a neurorobot yet, you can still run the
        neurorobot app using only your computer and webcamera. 
    </li>
</ul>

<p>&nbsp;</p>

# Older software (Brian version 1 only)

## Packages

* <a href="http://clones.gforge.inria.fr/"><object style="width: 200px; height: 150px;" width="200" height="150" classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0"><param name="src" value="http://www.youtube.com/v/mM_C-AkVrDQ?fs=1&amp;hl=en_US"><param name="align" value="right"><embed style="width: 200px; height: 150px;" type="application/x-shockwave-flash" width="200" height="150" src="http://www.youtube.com/v/mM_C-AkVrDQ?fs=1&amp;hl=en_US" align="right"></embed></object>CLONES</a>. Closed-Loop Neural Simulations. An open-source interface between Brian and <a href="http://www.sofa-framework.org/">Sofa</a>, a physics engine for biomedical simulation. <span style="font-variant: small-caps;">clones</span> allows you to model animal behaviour through the interaction of neurons, muscles and the environment. The video (<a href="http://www.youtube.com/v/mM_C-AkVrDQ?fs=1&amp;amp;hl=en_US">click for full screen</a>) demonstrates the <span style="font-variant: small-caps;">clones</span> implementation of Jordan Boyle's C. Elegans locomotion model (Boyle, JH. <em>C. elegans locomotion: an integrated approach.</em> PhD thesis, university of Leeds, 2009).
* <a href="http://dana.loria.fr/doc/index.html">DANA</a>. Distributed, Asynchronous, Numerical and Adaptive computing framework. A project designed for rate based models, complementing Brian's focus on spiking models. Partly inspired by and aiming at full integration with Brian.
* <a href="https://neuralensemble.org/PyNN/">PyNN</a>. A simulator-independent package for building neuronal network models. Allows you to write code for a model once using the PyNN API, and then run it without modification on any simulator that PyNN supports (currently <a href="http://www.neuron.yale.edu/neuron/">Neuron</a>, <a href="http://www.nest-initiative.org/?page=Software">NEST</a>, <a href="http://sourceforge.net/projects/pcsim/">PCSIM</a> and Brian).

## Distributions

* <a href="http://www.debian.org">Debian</a>. A GNU/Linux distribution with an extensive coverage of scientific software. Brian in Debian is maintained by <a href="http://neuro.debian.net">NeuroDebian project</a>, which also provides up-to-date releases of neuroscience-related software for <a href="http://neuro.debian.net/pkgs/python-brian.html">recent Debian and Ubuntu releases</a>.
* <a href="https://code.google.com/p/pythonxy/">Python(x,y)</a>. A distribution of Python oriented towards scientific computation, including Brian as a plugin.
* <a href="http://www.sagemath.org/">Sage</a>. A free open-source mathematics software system based on Python, including Brian as an optional extension.
