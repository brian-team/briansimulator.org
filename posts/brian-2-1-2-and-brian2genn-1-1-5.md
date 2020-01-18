<html><body><p>We have released new bug fix releases for <strong>Brian 2</strong> (version 2.1.2) and <strong>Brian2GeNN</strong> (version 1.1.5).

The new Brian 2 release fixes two bugs:
</p><ol>
 	<li>an incorrect application of the substitution mechanism in equations (i.e. when using the same set of equations several times and changing the equations' variable names via Brian's Equation class), and</li>
 	<li>an inadvertent deactivation of parts of the new caching mechanism which resulted in a major reduction of its performance improvement.</li>
</ol>
The Brian2GeNN release adds a workaround for a bug in some version of the glibc library on Linux which can potentially lead to drastically reduced performance. This is the same workaround that had already been applied to Brian 2's C++ standalone mode with an earlier release.

<strong>How to get Brian 2:</strong> <a href="http://brian2.readthedocs.io/en/2.1.2/introduction/install.html">http://brian2.readthedocs.io/en/2.1.2/introduction/install.html</a>

<strong>How to get Brian2GeNN:</strong> <a href="http://brian2genn.readthedocs.io/en/latest/introduction/index.html">http://brian2genn.readthedocs.io/en/latest/introduction/index.html</a>

As always, please report bugs or suggestions to the github bug tracker (<a href="https://github.com/brian-team/brian2/issues">https://github.com/brian-team/brian2/issues</a>) or to the brian-development mailing list (brian-development@googlegroups.com).</body></html>