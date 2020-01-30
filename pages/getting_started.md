<!--
.. title: Getting started
.. slug: getting-started
.. date: 2020-01-17 17:15:00 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

We present our easy, six step programme for learning how to model spiking neural networks with Brian.

<a href="https://neuronaldynamics.epfl.ch/">
<img src="https://neuronaldynamics.epfl.ch/img/cover.jpg" class="img-fluid float-right d-none d-md-block ml-4" width="100px"/>
</a>

## 1. Learn computational neuroscience

If you're not already familiar with computational neuroscience, we would recommend you get started with some of these
freely available online resources:

* [Neuronal Dynamics (Gerstner et al.)](https://neuronaldynamics.epfl.ch/). Uses Python and Brian for exercises.
  Associated [EPFL course](https://courseware.epfl.ch/courses/course-v1:EPFL+BIO_465.b+2019_1/about) and
  [videos](https://lcnwww.epfl.ch/gerstner/NeuronalDynamics-MOOCall.html).
* [INCF Training Space](https://training.incf.org/) has a number of courses on computational neuroscience.

## 2. Try Brian in the browser

Before you start, you can
<a href="https://mybinder.org/v2/gh/brian-team/brian2-binder/master?filepath=demo.ipynb" target="_blank">try a demo</a>
of Brian in the browser without installing anything. Note that this page uses the [mybinder.org](https://mybinder.org/)
service, and may take a few moments to load.

## 3. Download and learn Python

If you haven't used Python before, we recommend using the 
[Anaconda Python distribution](https://www.anaconda.com/distribution/).

And some options for learning Python:

* [Python for Beginners](https://www.python.org/about/gettingstarted/) is a general introduction to installing
  and learning Python.
* [Scipy Lecture Notes](https://scipy-lectures.org/index.html) is an introduction oriented towards Python for science.
  It's a bit more technical than the general introduction, but probably more relevant and includes a discussion of
  useful tools and environments.

## 4. Download and install Brian

If you've installed the Anaconda distribution above, installing Brian is as simple as:

```console
conda install -c conda-forge brian2
```
    
On other Python distributions, you can try:

```console
pip install brian2
```
    
See our [detailed installation documentation](https://brian2.readthedocs.io/en/stable/introduction/install.html) for
more information.

Finally, check out various ways of
[running Brian scripts](https://brian2.readthedocs.io/en/stable/introduction/scripts.html), including interactive
noteboks, integrated development environments and command line.

## 5. Follow the tutorials

Our [tutorials](https://brian2.readthedocs.io/en/stable/resources/tutorials/index.html) are designed for learning the
basics of Brian. The easiest way to use them is to click the <img src="https://static.mybinder.org/badge.svg"/> button
and run them interactively in the browser.

## 6. Next steps

Once you understand the basics, here are a few ideas for how to get to grips with more advanced features of Brian:

* Look at some of the [examples](https://brian2.readthedocs.io/en/stable/examples/index.html) for ideas of features
  you can use.
* Read through some of our [articles on Brian](/blog).
* Have a look at some published code ([here](https://senselab.med.yale.edu/ModelDB/ModelList?id=231240&allsimu=true) and
  [here](https://senselab.med.yale.edu/ModelDB/ModelList?id=113733&allsimu=true)). Note that some of these examples are
  for older versions of Brian.
* Read the [user's guide](https://brian2.readthedocs.io/en/stable/user/index.html). Every feature of Brian is covered,
  but it might be a bit overwhelming to try to read from beginning to end.
* Once you've mastered all that, try reading the
  [advanced guide](https://brian2.readthedocs.io/en/stable/advanced/index.html).