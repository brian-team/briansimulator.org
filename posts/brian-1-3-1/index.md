<html><body><p>We have just released Brian 1.3.1, available via <strong>easy_install -U brian</strong> or from our <a href="https://neuralensemble.org/trac/brian/downloader/download/release/16/1.3.1">download page</a>.

This is a minor release, but there are some nice new features and many small improvements (listed below).

Minor features:
</p><ul>
	<li>New PoissonInput class</li>
	<li>New auditory model: TanCarney (brian.hears)</li>
	<li>Many more examples from papers</li>
	<li>New electrode compensation module (in library.electrophysiology)</li>
	<li>New trace analysis module (in library.electrophysiology)</li>
	<li>Added new brian.tools.taskfarm.run_tasks function to use multiple CPUs to perform multiple runs of a simulation and save results to a DataManager, with an optional GUI interface.</li>
	<li>Added FractionalDelay filterbank to brian.hears, fractional itds to HeadlessDatabase and fractional shifts to Sound.shifted.</li>
	<li>Added vowel function to brian.hears for creating artificial vowel sounds</li>
	<li>New spike_triggered_average function</li>
	<li>Added maxlevel and atmaxlevel to Sound</li>
	<li>New IRNS/IRNO noise functions</li>
</ul>
Improvements:
<ul>
	<li>SpikeGeneratorGroup is much faster.</li>
	<li>Added RemoteControlClient.set(var, name) to allow sending data to the server from the client (previously you could only receive data from the server but not send it, except in string form).</li>
	<li>Monitors do not process empty spike arrays when there have not been any spikes, increases speed for monitored networks with sparse firing (#78)</li>
	<li>Various speed optimisations</li>
</ul>
Bug fixes:
<ul>
	<li>Fixed bug with frozen equations and time variable in equations</li>
	<li>Fixed bug with loading sounds using Sound('filename.wav')</li>
	<li>SpikeMonitor now clears spiketimes correctly on reinit (#75)</li>
	<li>MultiConnection now propagates reinit (important for monitors) (#76)</li>
	<li>Fixed bug in realtime plotting</li>
	<li>Fixed various bugs in Sound</li>
	<li>Fixed bugs in STDP</li>
	<li>Now propagates spikes only if spikes exist (#78)</li>
</ul></body></html>