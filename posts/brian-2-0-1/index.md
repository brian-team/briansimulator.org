<html><body><p>We are happy to announce the release of<strong> Brian 2.0.1</strong>. This is a bug fix release which does not add any new features but fixes a few important bugs and updates the documentation.
Earlier versions of Brian 2 contained bugs that could lead to incorrect recordings from subgroups with <em>PopulationRateMonitor</em> and <em>SpikeMonitor</em>. The issue was only triggered under quite specific circumstances and not for all code generation targets (for more details, see <a href="https://github.com/brian-team/brian2/issues/772">github issues 772</a> and <a href="https://github.com/brian-team/brian2/issues/777">777</a>), but could in the worst case lead to the recording of incorrectly high firing rates at certain time steps (for <em>SpikeMonitor</em>, the bug meant that spikes beyond the size of the subgroup were recorded).

The new release also fixes a few other issues reported by users, see the<a href="http://brian2.readthedocs.io/en/2.0.1/introduction/release_notes.html"> release notes</a> for more information. We strongly recommend all users of Brian 2 to update.

<strong>How to get Brian 2:</strong> follow the <a href="http://brian2.readthedocs.io/en/2.0.1/introduction/install.html">installation instructions in the documentation</a>

<strong>Further information about Brian2:</strong> <a class="moz-txt-link-freetext" href="http://brian2.readthedocs.org">http://brian2.readthedocs.org</a>

As always, please report bugs or suggestions to the <a href="https://github.com/brian-team/brian2/issues">github bug tracker</a> or to the brian-development mailing list (<a class="moz-txt-link-abbreviated" href="mailto:brian-development@googlegroups.com">brian-development@googlegroups.com</a>).</p></body></html>