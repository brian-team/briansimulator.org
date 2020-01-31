<!--
.. title: Download and Install
.. slug: install
.. date: 2020-01-30 17:02:35 UTC
.. type: text
-->

We recommend users to use the
[Anaconda distribution](https://www.anaconda.com/distribution/#download-section).
You can then either install Brian 2 in the Anaconda root environment, or
[create a new environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for Brian 2 which has the advantage that you can update (or not update) the dependencies of Brian 2 independently from the rest of your system. The packages for Brian 2
are in the [conda-forge](https://anaconda.org/conda-forge) channel, to install it
use:

<pre class="code literal-block"><i class="fa fa-chevron-right gp" aria-hidden="true"></i> conda install -c conda-forge brian2</pre>

If you do not want to use the Anaconda distribution you can also install Brian 2
from the [Python Package Index](https://pypi.python.org/pypi/Brian2) with `pip`:

<pre class="code literal-block"><i class="fa fa-chevron-right gp" aria-hidden="true"></i> pip install brian2</pre>

It is highly recommend to make sure that Brian is able to use C++ code generation,
have a look at the [documentation](https://brian2.readthedocs.io/en/stable/introduction/install.html#requirements-for-c-code-generation)
for more details.

## Additional tools
You will most likely also want to install additional tools to work with Brian 2,
in particular Python's plotting library [matplotlib](http://matplotlib.org/)
and the development tools from the [jupyter](http://jupyter.org/) project. To
install them, use the same tool as for the installation of Brian, e.g.:

<pre class="code literal-block"><i class="fa fa-chevron-right gp" aria-hidden="true"></i> conda install matplotlib jupyter</pre>

or
<pre class="code literal-block"><i class="fa fa-chevron-right gp" aria-hidden="true"></i> pip install matplotlib jupyter</pre>

Also have a look at other [Brian-related packages](/ecosystem/).

<div class="d-flex justify-content-end mb-2"><a href="https://github.com/brian-team/brian2"><button type="button" class="btn btn-primary"><i class="fab fa-github" aria-hidden="true"></i> Source code</button></a></div>

