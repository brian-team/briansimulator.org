<!--
.. title: The Brian Simulator
.. slug: index
.. date: 2020-01-17 15:03:57 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. hidetitle: True
-->

<div class="module features-module container-fluid mb-2 p-4">
      <h4 class="pb-2">Why use Brian?</h4>
      {{% examples "examples" %}}
</div>

<!--
<div class="module features-module container-fluid mb-2 p-4">
    <div class="row">
        <div class="col-md-12">
        <h2 class="module-header">Why use Brian?</h2>
        </div>
    </div>
    <div class="row">
        <div class="col-md-4 py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fas fa-square-root-alt"></i> Equation-based syntax</h3>
            <p>Brian's syntax is close to model descriptions in a scientific article.</p>
            </div>
        </div>
        </div>
        <div class="col-md-4  py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fa fa-balance-scale"></i> Physical units</h3>
            <p>Quantities use physical units (e.g. mV or &micro;&#8486;), and Brian checks
            the consistency of units to avoid errors.</p>
            </div>
        </div>
        </div>
        <div class="col-md-4 py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fa fa-screwdriver"></i> Flexibility</h3>
            <p>A large variety of neuron and synapse model can be used, as long as they can
            be described by equations.</p>
            </div>
        </div>
        </div>
        <div class="col-md-4 py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fas fa-tachometer-alt"></i> Performance</h3>
            <p>Model descriptions are translated into low-level code (e.g. C++), and
            therefore run fast.</p>
            </div>
        </div>
        </div>
        <div class="col-md-4 py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fas fa-history"></i> Stable development</h3>
            <p>The first version of Brian has been developed in 2007; Brian 2 has been
            developed since 2014, with a new release about every 6 months.</p>
            </div>
        </div>
        </div>
        <div class="col-md-4 py-2">
        <div class="card h-100">
            <div class="card-body">
            <h3><i class="fas fa-globe-europe"></i> Widely used</h3>
            <p>Used all over the world, for research and teaching (see e.g. the book
            <a href="https://neuronaldynamics.epfl.ch/"><i class="fa fa-book"></i>&nbsp; Neuronal dynamics</a> by W. Gerstner et al.).</p>
            </div>
        </div>
        </div>
    </div>
</div>
-->

<div class="container-fluid mb-2 p-4 border-blue">
    <div class="row">
        <div class="col-md-8">
            <!--<h3><i class="fa fa-download"></i> Download and installation</h3>-->
            <h3><i class="fab fa-linux"></i> <i class="fab fa-windows"></i> <i class="fab fa-apple"></i> Download and installation</h3>
            <p><code><i class="fa fa-chevron-right"></i> <a href="https://www.anaconda.com/distribution/">conda</a> install -c conda-forge brian2</code><br/>
            or<br/>
            <code><i class="fa fa-chevron-right"></i> pip install brian2</code></p>
            <p>For more details, see the <a href="https://brian2.readthedocs.io/en/stable/introduction/install.html">installation instructions in the documentation</a>.</p>
            <div>Source code available on <a href="https://github.com/brian-team/brian2"><i class="fab fa-github"></i> GitHub</a>.</div>
        </div>
        <div class="col-md-4">
            <h3><i class="fa fa-graduation-cap"></i> Getting started</h3>
            <a href="https://mybinder.org/v2/gh/brian-team/brian2-binder/master?filepath=demo.ipynb" target="_blank"><h4>Try in the browser</h4></a>
            <a href="getting-started/index.html"><h4>Beginners guide</h4></a>
            <a href="https://brian2.readthedocs.io/en/stable/resources/tutorials/index.html"><h4>Tutorials</h4></a>
            <a href="https://brian2.readthedocs.io/en/stable/examples/index.html"><h4>Examples</h4></a>
            <a href="https://brian2.readthedocs.io"><h4>Documentation</h4></a>
        </div>
    </div>
</div>

<div class="container-fluid p-4">
    <div class="row">
        <div class="col-md-4">
            <a href="/categories/news/index.html"><h3><i class="fa fa-newspaper"></i> News</h3></a>
            {{% post-list start="0" stop="4" tags="News" %}}{{% /post-list %}}
        </div>
        <div class="col-md-4">
             <a href="/categories/blog/index.html"><h3><i class="fas fa-scroll"></i> Articles</h3></a>
            {{% post-list start="0" stop="4" tags="articles" %}}{{% /post-list %}}
        </div>
         <div class="col-md-4 d-none d-sm-block">
            <a href="https://twitter.com/briansimulator"><h3><i class="fab fa-twitter"></i> Twitter</h3></a>
            <a class="twitter-timeline" data-width="auto" data-dnt="true" data-tweet-limit="2" data-chrome="noborders noheader nofooter noscrollbar" data-dnt="true" href="https://twitter.com/briansimulator?ref_src=twsrc%5Etfw">Tweets by briansimulator</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        </div>
        <div class="col-md-4 d-block d-sm-none">
        <a href="https://twitter.com/briansimulator"><h3><i class="fab fa-twitter"></i> Twitter</h3></a>
        </div>
    </div>
</div>
<div class="container-fluid p-4">
    <div class="row">
        <div class="col-md-4">
            <h3><i class='fa fa-globe'></i> Community</h3>
            <a href="https://groups.google.com/forum/#!forum/briansupport">
                <h4>Support forum</h4>
            </a>
            <h4><a href="/papers-using-brian">Papers using Brian</a></h4>
            <h4><a href="/ecosystem">Software ecosystem</a></h4>
            <h4>
                <a href="https://senselab.med.yale.edu/ModelDB/ModelList?id=231240&allsimu=true">Models</a> (and
                <a href="https://senselab.med.yale.edu/ModelDB/ModelList?id=113733&allsimu=true">older ones</a>)
            </h4>
            <a href="/contribute/index.html">
                <h4>How to contribute</h4>
            </a>
        </div>
        <div class="col-md-4">
            <h3><i class="fa fa-tools"></i> Material</h3>
            <a href="publications/index.html">
                <h4>Our papers</h4>
            </a>
            <a href="cite/index.html">
                <h4>How to cite us</h4>
            </a>
            <a href="https://github.com/brian-team/brian-material/tree/master/logos">
                <h4>Download logos</h4>
            </a>
        </div>
        <div class="col-md-4">
            <h3><i class="fa fa-users"></i> Team</h3>
            <ul class="list-unstyled">
                <li><a href="http://romainbrette.fr">Romain Brette</a><br/><span class="text-muted">Institut de la Vision, INSERM, Paris</span></li>
                <li><a href="http://neural-reckoning.org/">Dan Goodman</a><br/><span class="text-muted">Imperial College London</span></li>
                <li>Marcel Stimberg<br/><span class="text-muted">Institut de la Vision, Sorbonne University, Paris</span></li>
            </ul>
        </div>
    </div>
    <div class="row">
        <div class="col-md-12">
            <p>
                For a full list of contributors, see the
                <a href="https://github.com/brian-team/brian2/blob/master/AUTHORS">AUTHORS file</a> in the repository.
                All contributions (not only in the form of code) are listed in the
                <a href="https://brian2.readthedocs.io/en/stable/introduction/release_notes.html">release notes</a>.
            </p>
        </div>
    </div>
</div>
