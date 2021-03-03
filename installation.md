---
layout: page
title: Setting Up Anaconda
permalink: installation/
---

An important part of PIC16B is navigating the Python package ecosystem. We will do so using the Anaconda distribution of Python. Getting set up with Anaconda is a somewhat detailed process that will require you to briefly use the command line. 

## Step-By-Step

### §1. Install Anaconda

You can find installers for Anaconda [here](https://docs.anaconda.com/anaconda/install/). Choose the one appropriate to your operating system. 

If installing on macOS, **do not install Anaconda in the `opt` directory.** It is recommended that you install in the folder directly under your username. This is the same folder in which your "Downloads" folder exists. 

<figure class="image" style="width:50%">
    <img src="http://philchodrow.github.io/PIC16B/_images/installation-directory.png" alt="A screencap of the Anaconda graphical installer. The prompt states 'You have chosen to install this software in the folder philchodrow on the disk Macintosh HD'">
    <figcaption><i>Example of installing Anaconda to the directory corresponding to your username.</i></figcaption>
</figure>

### §2. Create the PIC16B Anaconda Environment

1. Open Anaconda Navigator. 
2. Navigate to the **Environments** tab. 
3. Choose "Create."
4. Create a Python **3.7** environment named "PIC16B." 

<figure class="image" style="width:50%">
    <img src="http://philchodrow.github.io/PIC16B/_images/create-environment.png" alt="A screencap of the Anaconda graphical installer. The prompt states 'You have chosen to install this software in the folder philchodrow on the disk Macintosh HD'">
    <figcaption><i>Creating the PIC16B environment.</i></figcaption>
</figure>

### §3. Install `nb_conda`

Still in the **Environments** tab, search for the `nb_conda` package on the right-hand side (you may need to update the index). 
Check the box beside this package, and then click "Apply" to install. 

### §4. Install TensorFlow 

Follow the same procedure to install the `tensorflow` package. This may take some time. While you're here, you may also wish to install some other familiar packages, such as `matplotlib` and `pandas`. In the future, if you ever attempt to import a package and encounter an error, you should attempt to install it via the Environments tab. 

### §5. Launch Jupyter Lab

Now go back to the "Home" tab. Launch JupyterLab. You may need to install the app first. 

Create a new Jupyter notebook. *Change the kernel* to the PIC16B environment that you created in Step §2

<figure class="image" style="width:50%">
    <img src="http://philchodrow.github.io/PIC16B/_images/change-kernel.png" alt="A screencap of the Anaconda graphical installer. The prompt states 'You have chosen to install this software in the folder philchodrow on the disk Macintosh HD'">
    <figcaption><i>Selecting the PIC16B environment from within a Jupyter notebook.</i></figcaption>
</figure>

### §6. Verify

Type the two lines below into your blank Jupyter Notebook and run them, swapping out my name for yours. If you do not encounter an error, then your setup was successful. Take a screencap of the result and submit it. Otherwise, contact the instructor for assistance. 

```python
import tensorflow as tf
print("My name is Phil Chodrow and I installed Anaconda and TensorFlow")
```