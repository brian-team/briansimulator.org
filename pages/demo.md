<html><body><p>The following are some examples of Brian in action, with the source code on the left and the output on the right. Note that all these examples are for Brian 1, examples for Brian 2 can be found in the <a href="https://brian2.readthedocs.org/en/latest/examples/">documentation</a>.
</p><h3>Random network</h3>
<table border="0" width="100%">
<tbody>
<tr>
<td>

[python]
from brian import *
eqs = '''
dv/dt = (ge+gi-(v+49*mV))/(20*ms) : volt
dge/dt = -ge/(5*ms) : volt
dgi/dt = -gi/(10*ms) : volt
'''
P = NeuronGroup(4000, eqs, threshold=-50*mV, reset=-60*mV)
P.v = -60*mV+10*mV*rand(len(P))
Pe = P.subgroup(3200)
Pi = P.subgroup(800)
Ce = Connection(Pe, P, 'ge', weight=1.62*mV, sparseness=0.02)
Ci = Connection(Pi, P, 'gi', weight=-9*mV, sparseness=0.02)
M = SpikeMonitor(P)
run(1*second)
raster_plot(M)
show()
[/python]

</td>
<td><img class="alignnone wp-image-40" title="rasterplot" src="http://briansimulator.org/WordPress/wp-content/uploads/2009/02/rasterplot.jpg" alt="rasterplot" width="395" height="299"></td>
</tr>
</tbody>
</table>
<h3>Synfire chain</h3>
<table border="0" width="100%">
<tbody>
<tr>
<td>

[python]
from brian import *
# Neuron model parameters
Vr = -70*mV
Vt = -55*mV
taum = 10*ms
taupsp = 0.325*ms
weight = 4.86 * mV
# Neuron model
eqs=Equations('''
dV/dt=(-(V-Vr)+x)*(1./taum) : volt
dx/dt=(-x+y)*(1./taupsp) : volt
dy/dt=-y*(1./taupsp)+25.27*mV/ms+
(39.24*mV/ms**0.5)*xi : volt
''')
# Neuron groups
P = NeuronGroup(N=1000, model=eqs,
threshold=Vt,reset=Vr,refractory=1*ms)
Pinput = PulsePacket(t=50*ms,n=85,sigma=1*ms)
# The network structure
Pgp = [ P.subgroup(100) for i in range(10)]
C = Connection(P,P,'y')
for i in range(9):
C.connect_full(Pgp[i],Pgp[i+1],weight)
Cinput = Connection(Pinput,Pgp[0],'y')
Cinput.connect_full(weight=weight)
# Record the spikes
Mgp = [SpikeMonitor(p) for p in Pgp]
Minput = SpikeMonitor(Pinput)
monitors = [Minput]+Mgp
# Setup the network, and run it
P.V = Vr + rand(len(P)) * (Vt-Vr)
run(100*ms)
# Plot result
raster_plot(showgrouplines=True,*monitors)
show()
[/python]

</td>
<td><img class="alignnone wp-image-50" title="sfc_rasterplot" src="http://briansimulator.org/WordPress/wp-content/uploads/2009/05/sfc_rasterplot.png" alt="sfc_rasterplot" width="400" height="316"></td>
</tr>
</tbody>
</table>
<h3>Network of sparsely connected inhibitory integrate-and-fire neurons</h3>
Dynamics of a network of sparsely connected inhibitory integrate-and-fire neurons. Individual neurons fire irregularly at low rate but the network is in an oscillatory global activity regime where neurons are weakly synchronized.
Reference: Brunel N, Hakim V, <em>Fast Global Oscillations in Networks of Integrate-and-Fire Neurons with Low Firing Rates</em>, Neural Computation 11, 1621–1671 (1999)
<table border="0" width="100%">
<tbody>
<tr>
<td>

[python]
from brian import *
# Network parameters
N = 5000
Vr = 10 * mV
theta = 20 * mV
tau = 20 * ms
delta = 2 * ms
taurefr = 2 * ms
duration = .1 * second
C = 1000
sparseness = float(C)/N
J = .1 * mV
muext = 25 * mV
sigmaext = 1 * mV
# Neuron model
eqs = "dV/dt=(-V+muext+sigmaext*sqrt(tau)*xi)/tau : volt"
group = NeuronGroup(N, eqs, threshold=theta,
reset=Vr, refractory=taurefr)
group.V = Vr
# Connections
conn = Connection(group, group, state='V', delay=delta,
weight=-J, sparseness=sparseness)
# Monitors
M = SpikeMonitor(group)
# Run
run(duration)
# Plot
raster_plot(M)
show()
[/python]

</td>
<td><img class="alignnone wp-image-249" title="Brunel_Hakim_1999" src="http://www.briansimulator.org/WordPress/wp-content/uploads/2009/05/Brunel_Hakim_1999.png" alt="Brunel_Hakim_1999" width="400"></td>
</tr>
</tbody>
</table>
<h3>Topographically connected network</h3>
Topographic map - an example of complicated connections. Two layers of neurons: the first layer is connected randomly to the second one in a
topographical way. The second layer has random lateral connections.
<table border="0" width="100%">
<tbody>
<tr>
<td>

[python]
from brian import *
N=100
tau=10*ms
tau_e=2*ms # AMPA synapse
eqs='''
dv/dt=(I-v)/tau : volt
dI/dt=-I/tau_e : volt
'''
rates=zeros(N)*Hz
rates[N/2-10:N/2+10]=ones(20)*30*Hz
layer1=PoissonGroup(N,rates=rates)
layer2=NeuronGroup(N,model=eqs,threshold=10*mV,reset=0*mV)
topomap=lambda i,j:exp(-abs(i-j)*.1)*3*mV
feedforward=Connection(layer1,layer2,sparseness=.5,weight=topomap)
lateralmap=lambda i,j:exp(-abs(i-j)*.05)*0.5*mV
recurrent=Connection(layer2,layer2,sparseness=.5,weight=lateralmap)
spikes=SpikeMonitor(layer2)
run(1*second)
subplot(211)
raster_plot(spikes)
subplot(223)
imshow(feedforward.W.todense(), interpolation='nearest', origin='lower')
title('Feedforward connection strengths')
subplot(224)
imshow(recurrent.W.todense(), interpolation='nearest', origin='lower')
title('Recurrent connection strengths')
show()
[/python]

</td>
<td><img class="alignnone wp-image-51" title="topographic" src="http://briansimulator.org/WordPress/wp-content/uploads/2009/05/topographic.png" alt="topographic" width="400" height="412"></td>
</tr>
</tbody>
</table>
<h3>Adaptive threshold model</h3>
A model with adaptive threshold (increases with each spike).
<table border="0" width="100%">
<tbody>
<tr>
<td>

```python
/mV)
show()

```

</td>
<td><img class="alignnone wp-image-52" title="adaptive" src="http://briansimulator.org/WordPress/wp-content/uploads/2009/05/adaptive.png" alt="adaptive" width="400" height="313"></td>
</tr>
</tbody>
</table>
<h3>Hodgkin-Huxley network</h3>
<table border="0" width="100%">
<tbody>
<tr>
<td>

[python]
from brian import *
# Parameters
area=20000*umetre**2
Cm=(1*ufarad*cm**-2)*area
gl=(5e-5*siemens*cm**-2)*area
El=-60*mV
EK=-90*mV
ENa=50*mV
g_na=(100*msiemens*cm**-2)*area
g_kd=(30*msiemens*cm**-2)*area
VT=-63*mV
# Time constants
taue=5*ms
taui=10*ms
# Reversal potentials
Ee=0*mV
Ei=-80*mV
we=6*nS # excitatory synaptic weight (voltage)
wi=67*nS # inhibitory synaptic weight
# The model
eqs=Equations('''
dv/dt = (gl*(El-v)+ge*(Ee-v)+gi*(Ei-v)-g_na*(m*m*m)*h*(v-ENa)-g_kd*(n*n*n*n)*(v-EK))/Cm : volt
dm/dt = alpham*(1-m)-betam*m : 1
dn/dt = alphan*(1-n)-betan*n : 1
dh/dt = alphah*(1-h)-betah*h : 1
dge/dt = -ge*(1./taue) : siemens
dgi/dt = -gi*(1./taui) : siemens
alpham = 0.32*(mV**-1)*(13*mV-v+VT)/(exp((13*mV-v+VT)/(4*mV))-1.)/ms : Hz
betam = 0.28*(mV**-1)*(v-VT-40*mV)/(exp((v-VT-40*mV)/(5*mV))-1)/ms : Hz
alphah = 0.128*exp((17*mV-v+VT)/(18*mV))/ms : Hz
betah = 4./(1+exp((40*mV-v+VT)/(5*mV)))/ms : Hz
alphan = 0.032*(mV**-1)*(15*mV-v+VT)/(exp((15*mV-v+VT)/(5*mV))-1.)/ms : Hz
betan = .5*exp((10*mV-v+VT)/(40*mV))/ms : Hz
''')
P=NeuronGroup(4000,model=eqs,
threshold=EmpiricalThreshold(threshold=-20*mV,refractory=3*ms),
implicit=True,freeze=True)
Pe=P.subgroup(3200)
Pi=P.subgroup(800)
Ce=Connection(Pe,P,'ge',weight=we,sparseness=0.02)
Ci=Connection(Pi,P,'gi',weight=wi,sparseness=0.02)
# Initialization
P.v=El+(randn(len(P))*5-5)*mV
P.ge=(randn(len(P))*1.5+4)*10.*nS
P.gi=(randn(len(P))*12+20)*10.*nS
# Record a few trace
trace=StateMonitor(P,'v',record=[1,10,100])
run(1000*msecond)
plot(trace.times/ms,trace[1]/mV)
plot(trace.times/ms,trace[10]/mV)
plot(trace.times/ms,trace[100]/mV)
show()
[/python]

</td>
<td><img class="alignnone wp-image-53" title="hh" src="http://briansimulator.org/WordPress/wp-content/uploads/2009/05/hh.png" alt="hh" width="400" height="311"></td>
</tr>
</tbody>
</table></body></html>