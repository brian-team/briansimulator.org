<html><body><h2>Modelling of spiking neural networks with Brian</h2>
<p>Tutorial T7 at <a href="http://www.cnsorg.org/cns-2014-quebec-city">CNS 2014</a>, Québec City (<strong>July 26th 2014</strong>)</p>
<p>The tutorial will take place in room 2101 at the <a href="http://www.cnsorg.org/cns-2014-venue">Québec City Conference Center</a>. Please consider installing Brian 2 beforehand, see the instructions <a href="#installation">below</a>.</p>
<h3>Material</h3>
<p>All the material from the tutorial is available in the "2014-CNS-tutorial" folder in the "brian-material" github repository: <a href="https://github.com/brian-team/brian-material">https://github.com/brian-team/brian-material</a></p>

<p>You can clone the repository using git, but you can also download all the material in a single <a href="https://github.com/brian-team/brian-material/archive/master.zip">ZIP file</a>.</p>
<h3>Schedule</h3>
<p>
In the morning sessions, we plan to give an introduction to Brian, no prior knowledge of Brian is necessary. The afternoon sessions will be about more advanced topics and delve a bit into Brian's internals.
</p>
<table><colgroup> <col width="120"> <col width="640"></colgroup>
<tbody>
<tr>
<td>
<p style="text-align: center;" dir="ltr"><strong>Time</strong></p>
</td>
<td>
<p style="text-align: center;" dir="ltr"><strong>Topic</strong></p>
</td>
</tr>
<tr>
<td style="text-align: center;">
<p dir="ltr">9.00 - 9.30</p>
</td>
<td>
<p dir="ltr">Introduction</p>
</td>
</tr>
<td style="text-align: center;">
<p dir="ltr">9.30 - 10.10</p>
</td>
<td>
<p dir="ltr">Core concepts of Brian2</p>
</td>

<tr>
<td>
<p style="text-align: center;" dir="ltr"><em>Coffee break</em></p>
</td>
<td></td>
</tr>
<tr>
<td style="text-align: center;">
<p dir="ltr">10.40 - 12.00</p>
</td>
<td>
<p dir="ltr">Hands-on tutorial</p>
</td>
</tr>
<tr>
<td>
<p style="text-align: center;" dir="ltr"><em>Lunch break</em></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p style="text-align: center;" dir="ltr">13.30 - 13.45</p>
</td>
<td>
<p dir="ltr">Going from Brian 1 to Brian 2</p>
</td>
</tr>
<td>
<p style="text-align: center;" dir="ltr">13.45 - 14.50</p>
</td>
<td>
<p dir="ltr">Advanced Brian 2 (code generation and the new "standalone mode")</p>
</td>

<tr>
<td>
<p style="text-align: center;" dir="ltr"><em>Coffee break</em></p>
</td>
<td></td>
</tr>
<tr>
<td>
<p style="text-align: center;" dir="ltr">15.20 - 16.30</p>
</td>
<td>
<p dir="ltr">Extending Brian 2</p>
</td>
</tr>
<tr>
<td>
<p style="text-align: center;" dir="ltr">19.00 - ...</p>
</td>
<td>
<p dir="ltr">Brian social (place TBA)</p>
</td>
</tr>
</tbody>
</table>

<h3 id="installation">Brian 2 installation</h3>
<p>We recommend that you install Brian 2 before coming to the tutorial. If you already have a working Python installation with the main Brian dependencies (numpy and scipy), you can try to skip directly to the step "Installing Brian 2" .</p>

<p>For setting up a Python environment with the libraries that Brian depends on, we recommend using the <em>Anaconda</em> distribution by <a href="http://continuum.io/">Continuum Analytics</a>. On Windows, an alternative to Anaconda is the <em>Python(x,y)</em> distribution, which is in particular recommended if you want to use the C++ code generation/standalone mode on Windows. Download its installer from <a href="https://code.google.com/p/pythonxy/wiki/Downloads?wl=en">code.google.com/p/pythonxy/wiki/Downloads?wl=en</a>.</p>

<h4>Installing the Anaconda distribution</h4>
<ul>
<li>Download the appropriate installer from here: <a href="http://continuum.io/downloads">continuum.io/downloads</a></li>
<li>Follow the installation instructions on the same package</li>
<li>(Optional) Update the anaconda packages to the latest versions<br>
<code>
  conda update conda
  conda update anaconda
</code></li>
</ul>
<h4>Installing Brian 2</h4>
<ul>
<li>If you have just installed Anaconda as described above, make sure to open a new Terminal/Command Prompt window and make sure that the Anaconda binary directory is in your path (the Anaconda installer automatically takes care of this by default)</li>
<li>Install Brian 2 using<br>
<code>pip install brian2 --pre</code>
</li>
<li>If you already have an older version of Brian 2, use<br>
<code>pip install brian2 --pre --upgrade --no-deps</code>
</li>
</ul>
<h4>Working with Brian 2</h4>
<ul>
<li>The full Anaconda distribution comes with a Matlab-like development environment for Python called <a href="https://code.google.com/p/spyderlib/">Spyder</a>, you can start it by typing <code>spyder</code> in a Terminal. You can also start it using Anaconda's "launcher" application, for more details and other IDEs that you can use, see <a href="http://docs.continuum.io/anaconda/ide_integration.html">docs.continuum.io/anaconda/ide_integration.html</a></li>
<li>You don't necessarily need a full IDE to work with Python/Brian, starting <code>ipython</code> in a terminal window and using any text editor to edit files is good enough.</li>
</ul>
</body></html>