<!--
.. title: New release: Brian 2.10
.. slug: brian-210
.. date: 2025-12-10 17:00:00 UTC
.. category: news
.. tags: Release,Development
.. type: text
-->

We are happy to announce the **Brian 2.10 release**. This release extends the functionality of `PopulationRateMonitor` and `SpikeMonitor`, which now provide a unified interface to for smoothed and binned rates, and adds a new `run_at` function to execute code at specific time points. It also fixes several important bugs and comes with performance improvements for C++ standalone mode. Behind the scenes, it made important progress in refactoring aspects of our code generation system, working towards the long-term goal of having a single C++ code generation system for standalone and runtime mode, and retiring the current Cython code generation mechanism.

For more details, head over to the [release notes](https://brian2.readthedocs.io/en/2.10.1/introduction/release_notes.html).

<!-- TEASER_END -->

Brian 2 can be installed with pip from the [pypi repository](https://pypi.org/project/Brian2/), and via several other means (some of them might take a while to catch up to the latest release). See the [installation instructions](https://brian2.readthedocs.io/en/2.10.1/introduction/install.html), and the badges in the [README file](https://github.com/brian-team/brian2/blob/master/README.md) for more details.

Thanks to everyone who contributed 🤝!

