<!--
.. title: Brian online tutorial
.. slug: brian-online-tutorial
.. date: 2020-08-06 13:27:27 UTC
.. tags: Teaching
.. category: news
.. description: Brian online tutorial announcement
.. type: text
-->

We will experiment with running a Brian tutorial online. The first tutorial of
this kind will take place on **Friday, August 7th 2020** from **2pm-6pm BST** (UTC+1, see [here for other timezones](https://www.timeanddate.com/worldclock/fixedtime.html?msg=Brian+Online+Tutorial&iso=20200807T14&p1=136&ah=4)). Free (but mandatory)
registration [here](https://t.co/zS4VQ4Cp51?amp=1). We will run the tutorial as
a [Zoom](https://zoom.us/) meeting – registering with the link will give you the URL (please don't share so we can avoid zoombombing). We will record the meeting and
if everything goes reasonably well, we will upload the videos later.

If you participate, it would be really helpful if you could download and install Brian before the tutorial so that you can work along with it as we go. Instructions are:

1. Download and install the [Anaconda Python 3 distribution](https://www.anaconda.com/products/individual)
2. Open a command prompt and run the following lines:
    <pre class="code literal-block">
<i class="fa fa-chevron-right gp" aria-hidden="true"> conda create -n brian_tutorial -c conda-forge python=3 brian2 matplotlib notebook
<i class="fa fa-chevron-right gp" aria-hidden="true"> conda activate brian_tutorial
<i class="fa fa-chevron-right gp" aria-hidden="true"> pip install brian2tools
</pre>
3. You can now verify this is working by starting a Jupyter notebook server with:
    <pre class="code literal-block"><i class="fa fa-chevron-right gp" aria-hidden="true"> jupyter notebook</pre>
4. Your browser should open with the Jupyter notebooks interface. Now create a new notebook and put the following code in an empty cell:
    <pre class="code literal-block">from brian2 import *</pre>
5. Run that cell by pressing Ctrl+Enter. If that works without any errors (you might see a warning) then you're good to go.
6. If that doesn't work or you want to use a different system than Anaconda, take a look at our [detailed installation instructions](https://brian2.readthedocs.io/en/stable/introduction/install.html). 

If you have trouble installing, don't worry. You can use the [Brian installation on Binder](http://mybinder.org/v2/gh/brian-team/brian2-binder/master?filepath=index.ipynb) or [Google Colab](https://colab.research.google.com) instead.

For Colab, just make the first cell as follows:

 <pre class="code literal-block">
!pip install brian2
!pip install brian2tools
</pre>

Looking forward to seeing you all on Friday!
