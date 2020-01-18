<!--
.. title: The Brian Simulator
.. slug: index
.. date: 2020-01-17 15:03:57 UTC
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
-->

Brian is a free, open source simulator for spiking neural networks. It is written in the Python programming language and is available on almost all platforms. We believe that a simulator should not only save the time of processors, but also the time of scientists. Brian is therefore designed to be easy to learn and use, highly flexible and easily extensible.

To get an idea of what writing a simulation in Brian looks like, the following code defines a randomly connected network of integrate and fire neurons with exponential inhibitory and excitatory currents, runs the simulation and makes the raster plot on the right.

<div class="container">
  <div class="row">
    <div class="col-sm">
```Python
    from brian2 import *
    eqs = '''
    dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
    dge/dt = -ge/(5*ms) : volt
    dgi/dt = -gi/(10*ms) : volt
    '''
    P = NeuronGroup(4000, eqs, threshold='v > -50*mV', reset='v=-60*mV')
    P.v = -60*mV
    Pe = P[:3200]
    Pi = P[3200:]
    Ce = Synapses(Pe, P, on_pre='ge+=1.62*mV')
    Ce.connect(p=0.02)
    Ci = Synapses(Pi, P, on_pre='gi-=9*mV')
    Ci.connect(p=0.02)
    M = SpikeMonitor(P)
    plt.plot(M.t / ms, M.i, '.', ms=2)
    plt.gca().set(xlabel='time (ms)', ylabel='neuron index')
    plt.show()
```
    </div>
    <div class="col-sm">
    <img src="/plots/rasterplot.png" alt="raster plot" title="raster plot">
    </div>
  </div>
</div>

<hr>

<div class="container">
    <div class="row justify-content-center">
        <div class="col-md-4" align="center">
            <a href="/install/index.html" class="feature-link" title="Install">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-download fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Install</h2>
            </a>
        </div>
        <div class="col-md-4" align="center">
            <a href="getting_started/index.html" class="feature-link" title="Get started">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-graduation-cap fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Get started</h2>
            </a>

        </div>
        <div class="col-md-4" align="center">
            <a href="https://brian2.readthedocs.org" class="feature-link" title="Documentation">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-book fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Documentation</h2>
            </a>
        </div>
    </div>
    <div class="row justify-content-center">
        <div class="col-md-4" align="center">
            <a href="contribute/index.html" class="feature-link" title="Contribute">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fas fa-laptop-code fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Contribute</h2>
            </a>
        </div>
        <div class="col-md-4" align="center">
            <a href="support/index.html" class="feature-link" title="Get help">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-question-circle fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Get help</h2>
            </a>

        </div>
        <div class="col-md-4" align="center">
            <a href="/showcase/index.html" class="feature-link" title="Showcase">
                <div class="feature-icon">
                    <span class="fa-stack fa-3x"><i class="fa fa-circle fa-stack-2x"></i><i class="fa fa-desktop fa-stack-1x fa-inverse"></i></span>
                </div>
                <h2 class="index-feature">Showcase</h2>
            </a>
        </div>
    </div>
</div>

<div class="alert alert-info" role="alert">
  <p>If you use Brian for your research, please cite our introductory paper:</p>
  <p><i class="fa fa-book"></i> Stimberg, M., Brette, R., & Goodman, D. F. (2019). <i>Brian 2, an intuitive and efficient neural simulator</i>. eLife, <b>8</b>, e47314. <a href="https://doi.org/10.7554/eLife.47314">DOI: 10.7554/eLife.47314</a>.</p>
  <p>To quote a specific Brian version, please use the appropriate DOI from <a href="https://zenodo.org/record/3607592">Zenodo</a>.</p>
</div>



Brian was co-authored by and primarily written by <a href="https://romainbrette.fr">Romain Brette</a>, <a href="http://neural-reckoning.org/">Dan Goodman</a>, and Marcel Stimberg.

Additional work has been done by many people, see our <a href="https://brian2.readthedocs.io/en/stable/introduction/release_notes.html">release notes</a> and the <a href="https://github.com/brian-team/brian2/blob/master/AUTHORS">AUTHORS</a> file for a list.
