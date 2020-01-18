<html><body><p>I am starting a new series of posts on this blog, called « Reader’s digest ». These are simply bibliographical notes on recent readings (of recent or old papers).

While reading Abeles’s Scholarpedia entry on <a href="http://www.scholarpedia.org/article/Synfire_Chains">synfire chains</a>, I learned that while Abeles introduced the terms “synfire chains”, the concept is in fact older. It seems that it dates back to Griffith in 1963 (Griffith 1963). In that paper, he considers threshold binary neurons, in discrete time. Previous authors showed that networks of such neurons could only be in two stationary states: quiescent or fully active (Beurle 1956; Ashby et al. 1962), and this was seen as a paradox, since apparently this is not what happens in the nervous system. This is reminiscent of a problem that is still present in current literature: the stability of the persistent irregular state in closed networks of spiking neurons (indeed most models use either external noise to maintain activity (Brunel 2000) or a suprathreshold intrinsic current, as in (Vogels &amp; Abbott 2005)).

In his paper, Griffith introduces a “transmission line”, which is exactly a synfire chain, except with discrete rather than continuous time (an approximation that he acknowledges and even reconsiders at the end of the paper). He demonstrates (with calculations involving binomial distributions and the central limit theorem) that indeed there is only a single stable mode of propagation (all neurons active) but that if inhibitory neurons are also included, then there may be another stable mode, with only a fraction of neurons being active. He also mentions the possibility of unstable oscillations due to inhibition (which corresponds to what is now called the “PING” mechanism, pyramidal-interneuron gamma).

The paper is interesting for two reasons: 1) it includes methods of calculations relevant for synfire chain propagation, 2) it seems to provide a solution for the problem of the stability of irregular activity, which is based on a small number of strong inhibitory neurons. This latter point applies both to synfire chains and to more traditional recurrent networks.

 

<span style="text-decoration: underline;">References</span>

Ashby, W.R., Von FOERSTER, H. &amp; Walker, C.C., 1962. Instability of Pulse Activity in a Net with Threshold. <em>Nature</em>, 196(4854), p.561‑562.

Beurle, R.L., 1956. Properties of a Mass of Cells Capable of Regenerating Pulses. <em>Philosophical Transactions of the Royal Society of London. Series B, Biological Sciences</em>, 240(669), p.55‑94.

Brunel, N., 2000. Dynamics of sparsely connected networks of excitatory and inhibitory spiking neurons. <em>J Comput Neurosci</em>, 8(3), p.183.

Griffith, J.S., 1963. On the Stability of Brain-Like Structures. <em>Biophysical Journal</em>, 3(4), p.299‑308.

Vogels, T.P. &amp; Abbott, L.F., 2005. Signal Propagation and Logic Gating in Networks of Integrate-and-Fire Neurons. <em>The Journal of Neuroscience</em>, 25(46), p.10786‑10795.</p></body></html>