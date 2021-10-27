---
layout: post
title:  "Blog Post 4"
date:   2020-11-16
due: 2021-11-05
categories: blog assignment
permalink: posts/blog-post-4
author: Phil Chodrow
---


This blog post follows a somewhat more definite sequence than others. For this reason, I thought you might find it convenient to have a pre-constructed Jupyter Notebook for you to fill in. Find it [here](https://nbviewer.jupyter.org/github/PhilChodrow/PIC16B/blob/master/HW/spectral-clustering.ipynb). Once you've written code in this notebook, you can then bring that code into a standard Jekyll blog post. 

Please note that, although I've supplied explanations for various steps, part of the blog post spec is for you to write your **own explanations in your own words**. Extreme mathematical detail is not necessary, but you are expected to make an effort to communicate to your reader the meaning of the various computations. Submissions that include language taken verbatim from the linked notebook will be assessed as <span style="color: gold;"><i class="fas fa-arrow-alt-circle-up"></i></span> **In Progress**.  

<div class="fancy-h1"> Specifications </div>

Please remember that you must meet all specifications in order to receive credit on the first submission! 

# Coding Problem

1. The similarity matrix is constructed without loops (Part A). 
2. The **cut** and **volume** terms are correctly implemented, with no loops for the **volume** (Part B). 
3. The function `transform()` is implemented and the equation for the normcut objective is verified, with no loops (Part C). 
4. The `scipy.optimize.minimize()` function is used to compute a minimum of the function $$R_A$$ (Part D).
5. The plot shows the attempted data clustering from the optimization (Part E).   
6. The Laplacian matrix and its eigenvector corresponding to the second-smallest eigenvalue are both computed. The plot shows a more correct clustering of the data, with only a small number of points mis-clustered (Part F). 
7. The function written appears correct and is under 10 lines of code, with a demonstration plot supplied (Part G). 
8. Experiments for at least 3 different values of the `noise` argument to `make_moons` are shown and discussed (Part H).
9. Through experimentation, a value of `epsilon` is shown for which the algorithm correctly clusters the bullseye (Part I).

# Style and Documentation

1. The function `spectral_cluster` has an appropriate docstring indicating its purpose, inputs, outputs, and assumptions. 

# Writing

1. The blog post is written in tutorial format, in engaging and clear English. Grammar and spelling errors are acceptable within reason. 
2. The blog post explains how each of the different computations are related, although mathematical detail is not required. "This is an approximation of that" is an adequate level of detail. 
3. The blog posts includes brief written discussions of the results after each of the experiments in Parts F, G, H, and I. 
