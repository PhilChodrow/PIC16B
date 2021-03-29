---
layout: page
title: Course Project
permalink: project/
---

Rather than an exam, the cumulative evaluation in PIC16B is a course project. The purpose of the project is for you to demonstrate your ability to independently identify and solve complex problems using Python.  

This project is open-ended, and should match your interests and goals. You are free to work on a project that is connected to other work you are doing, in another class, research, an internship, or a job. However, your project must be original work -- i.e. no submitting code that you already wrote. 


<div class="fancy-h1">Project Topic</div>


You have considerable freedom to set the topic and goal of your project, subject to my approval. There are a few requirements. If you aren't sure about whether your project idea fulfills these requirements, please approach me as early as possible to discuss. 

## Use Tools Beyond PIC16A

Part of the purpose of the project is for you to demonstrate what you learned during your time in PIC16B. For this reason, you are required to demonstrate tools from the course. A project that uses basic `pandas` and decision trees to analyze a data set won't receive full credit -- that's PIC16A stuff. Some possibilities: 

- Use TensorFlow and/or OpenCV for image classification or language modeling in a data set that you scraped yourself. 
- Perform a detailed analysis and visualization of a large data set, using SQL to access the data. 
- Perform and visualize a complex simulation by solving partial differential equations. Use boundary conditions drawn from real data. 
- Analyze a networked data set using `networkx` and other tools.   
- Write an app to visualize different kinds of dynamical processes (like disease spread or opinion dynamics) evolving on networks. 
- Use webscraping and database skills to access and consolidate a range of disparate data sources into a new, publicly available data set. 

You might wish to use tools from later in the course in your project.  In this case, you'll need to learn these tools early! You can approach me as a group, and we will discuss a way to ensure that you are able to learn the needed content in time to work on your project.  

You are allowed and even encouraged to additionally use tools not covered in PIC16B. However, you must still incorporate some content from PIC16B as well in order to receive full credit. 

## Beyond Kaggle

A common pattern on machine learning websites such as [Kaggle](https://www.kaggle.com/) is: 

1. Acquire cleaned data. 
2. Fit several machine learning models to the data. 
3. Assess performance and report test score. 

**This is not enough** for a successful course project. While you are welcome to do a machine learning project, I expect more than the above for a quarter-long effort. A project whose primary punchline is "we got 93% test accuracy on a public data set" is likely to be an A- project at best. 


Here's how you can deepen your project: 

1. Perform a significant **data acquisition** task. Obtain, clean several novel data sets on which to base your analysis. 
2. Perform a detailed analysis of **model error and bias**. Does your model have the same performance on different subgroups of the data? Why is that? Can you adjust your model to reduce bias? 
3. Construct **complex visualizations** to help your audience understand why your model works on the data, and what we can learn from the data using the model. 


<div class="fancy-h1">Project Requirements</div>

## Format and Structure

- Your project must be hosted on GitHub as a version-controlled repository. 
- Functions and classes should not be defined in notebooks. Rather, your project must include functions and classes defined in two or more `.py` files, which must in turn be packaged as a module that can be imported. To use your functions and classes in a notebook, you will import these functions and classes using `import myProject`. 
- Your provisional and final project submissions must include a blog post that clearly demonstrates how to use your project tools. Your code and explanation must be sufficiently careful that a user could clone your repository and run exactly the code demonstrated on your blog. It's fine for group members to collaborate on a single blog post and post the same one to each of their blogs. 
- All your source code must include thorough comments and comprehensive docstrings on functions, classes, and methods. 

## Presentation

You will be responsible for presenting your project in various formats throughout the quarter. 

- **Pitches** in Week 1. These are for getting your classmates interested in your project idea. Posted on Campuswire. 
- **Proposal** due Week 3. This is a written document for telling me what you are going to work on, and getting my feedback. Submitted as a group on CCLE. 
- **Progress Updates** in Discussion throughout the quarter. These are very short (3-5 minute) presentations to the class about what you've achieved on your project so far. You are required to have some kind of visual aid --- updates which consist only of you talking are not sufficient. Appropriate visual aids include slides or (even better) live-coding demonstrations of of your code so far. 
- **Provisional Submission** at the end of Week 8. Your submission consists of a blog post in which you demonstrate the use of the code you have written for its intended purpose, such as performing a simulation or analyzing a data set. Your submission must include a link to your project GitHub repository. Each group member must submit a blog post, although it is acceptable for this post to be the same between group members. The purpose of the provisional submission is for me to give you feedback and indicate where your opportunities are to improve your project. 
- **Final Presentation** in Week 10. A group presentation, using either slides or live-coding, that makes clear what your project achieves and how to use it. Presented in class. 
- **Final Submission** during Finals Week. The submission requirements are the same as those for the provisional submission, but I will be expecting you to have made revisions in response to my feedback from the provisional submission. 

The **Pitches** and **Progress Updates** count toward your Participation grade, while the other components all count toward your Project grade. 

## Group Work

In your project's GitHub repository (not your blog post), you should have a top-level `README.md` file that includes a **Group Contributions Statement**. Your group contributions statement should make clear the primary ways in which each group member contributed to the project. 

Additionally, I expect **all group members** to contribute to the project repository. The commit history of the project repository is public, and so I will be checking to ensure that everyone has made commits. If I see that only one group member has been committing code, I will have questions. 

Generally speaking, all group members will receive the same project grade. The only exceptions are if I see a highly inequitable Group Contributions Statement or GitHub commit history.  

