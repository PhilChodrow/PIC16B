---
layout: post
title:  "Project Proposal"
date:   2021-03-16 15:36:27
due:   2021-10-14
categories: project assignment
permalink: posts/project-proposal
author: Phil Chodrow
---

In this assignment, you'll do two things: 

1. You'll get some practice using *collaborative workflows* with git and GitHub. 
2. You'll formally propose your project.

Please note that you should be in active communication with your project partners when completing this assignment. For Parts §1 and §2, it's probably easiest to meet in person or hop on a video call and complete them all together in one sitting. For Part §3, in which you'll actually write your proposal, you should probably make a plan as a group, split up to do some writing, and then make a time to meet back to discuss and make revisions. 

<div class="fancy-h1"> §1. Create the Project Repository </div>

**One** member of the group should go on GitHub.com and create the project repository. This is the central location that will house your project files. After creating the project repository, this group member should add all other group members as collaborators on the project (under Settings --> Manage Access). 

All group members should now clone the repository. 

**Do not fork the project repository**, as this will lead to everyone having their own private version. Not very collaborative! 

By the end of this step, you now have a shared repository, under version control, in which you can all collaborate. This is where your project files, including code and data, will live. 


<div class="fancy-h1"> §2. Collaborative Workflows in Git </div>

In this part of the activity, you'll get familiar with the most important collaborative workflows with Git and GitHub by playing tic-tac-toe with your group members. 

*Working through this mini activity with your group is optional but strongly recommended.*

### §2.1 Make a Grid

It's possible that your repository already has a top-level file named `README.md`. If not, a new group member (not the one who created the repo) should create one. Then, this group member should create a code block in the file `README.md` containing a 3x3 grid of dots, like the below: 

```
. . . 
. . .
. . .
```

Save, commit, and push. All other group members should now pull, so that they have the grid of dots as well. 

### §2.2 Play Tic-Tac-Toe

If you have more than two people, separate into two teams -- it's ok if they are not the same size. Play a few games of [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) by replacing the dots in the grid you made with the symbol X or O. Here's how to make a move: 

1. A member of Team X deletes a dot and replaces it with an X. 
2. This member commits and pushes their change. 
3. All other team members pull, so that the move is reflected in their file. 
4. A member of Team O deletes a dot and replaces it with an O...

By playing some Tic-Tac-Toe, you practice the fundamental pull-commit-push workflow of collaboration. Make sure that every group member gets a chance to make a move, commit their move, and push at least twice. 

### §2.3 Merging

Create a new, blank Tic-Tac-Toe game. Imagine that Team X and Team O miscommunicated about who would go first, so they both make moves simultaneously. Test out the following scenarios. 

**Scenario 1:**

Team X makes the following move:

```
. . . 
. . .
. X .
```

Team O makes the following move: 

```
. O . 
. . .
. . .
```

Both teams should now attempt to commit and push. One team will be prompted to *pull* prior to pushing. This pull will prompt a *merge*, since two changes were made to the same file. Observe what happens, commit, and then push. Pull as needed so that both teams have both moves in their file. 

**Scenario 2:**

Team X makes the following move:

```
. . . 
. X .
. . .
```

Team O makes the following move: 

```
. . . 
. O .
. . .
```

The current representative of each team should commit these respective moves, and attempt to push. 

Whoops! One team will be prompted to pull, and after pulling will be informed that there is a *merge conflict* in the repository. Inspect the file. Notice that the relevant part of the file now looks very weird. If you look closely, you can find lines corresponding both to the X move and to the O move. Pick one (arbitrarily), and commit/push the result. 

This is an example of the process used to handle merge conflicts, which occur when separate team members have modified the same file in conflicting ways. 

It's recommended, but not required, that your team members take some time on their own to do a little reading on how merge conflicts work. [This page](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) gives a good explanation, and also covers the (optional but highly useful) topic of *branching*. 



<div class="fancy-h1"> §3. Write Your Project Proposal </div>

Write your project proposal in your project repository. For now, you can just use the file `README.md` to hold your proposal; this has the benefit that GitHub.com will automatically render it for you. Specs for your proposal are below. 





## The Big Picture

It's around this stage that it's very natural to ask: 

> What makes a good project? 

The Required Sections of the project proposal, as well as the overall [Project Description](http://philchodrow.github.io/PIC16B/project/) will tell you a lot about what I'm looking for. That said, there are two simple questions that you should ask yourselves when envisioning your project: 

> Will I learn something by completing this project? <br>
> Will I be proud of this project once it's done?

If the answer to both questions is "yes," then your overall project idea is likely good. Feel free to approach me early if you want to talk over whether your project idea is suitable for the course. 

## Required Sections

You are required to include sections in your proposal that address the following topics. Feel free to include additional sections as needed. Remember that you can create Markdown sections using the \# character. 

### Abstract

In 3-4 sentences, describe what problem the project addresses, and the overall approach you will use to solve that problem. 

### Planned Deliverables

Concisely state what you are aiming to create and what capabilities it will have. Are you making a webapp? A Python package for others to use? Code that creates a novel data set? Etc. Please consider two scenarios: 
    - "Full success." What will your deliverable be if everything works out for you exactly as you plan?
    - "Partial success." What useful deliverable will you be able to offer even if things don't 100% work out? For example, maybe you aren't able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan! 

In each case, please make sure to be clear about what the *interface* is for your project. If you are making an app, then the interface should likely be either a local app or a webapp. If you are focusing on scientific computation or data science, then a Jupyter notebook *may* be an appropriate interface -- talk to me if you're not sure. 

### Resources Required

What resources do you need in order to complete your project? Data? Computing power? An account with a specific service? 

Please pay special attention to the question of **data**. If your project idea involves data, include **at least one link** to a data set you can use. It's also acceptable to link to a website from which you intend to scrape the data you will use (although note that high-quality scraping is a lot of work). 

If you can't find data for your original idea, that's ok! Think of something related to your group's interests for which you can find data. 

Most projects should involve data in some way, but certain projects may not require data. Ask me if you're not sure. 

### Tools and Skills Required

What skills will you need? Machine learning, database management, complex visualization, something else? Do a bit of research into which Python packages accomplish the tasks you are going to need. Feel free to look ahead at what we're going to do in the remainder of the course -- you're likely to find some of the packages you'll need there! 

### What You Will Learn 

What will you learn by completing this project? Feel free to mention particular techniques, software packages, version control, project management principles, any other learning goals you might have.  

### Risks

What are two things that could potentially stop you from achieving the full deliverable above? Maybe it turns out that the signal you thought would be present in the data just doesn't exist? Or maybe your idea requires more computational power than is available to you? What particular risks might be applicable for your project?

### Ethics 

All projects we undertake involve decisions about whose interests matter; which problems are important; and which tradeoffs are considered acceptable. Take some time to reflect on the potential impacts of your product on its users and the broader world. If you can see potential biases or harms from your work, describe some of the ways in which you will work to mitigate them. Remember that even relatively simple ideas can have unexpected and impactful biases. [Here's a nice introductory video](https://youtu.be/Ok5sKLXqynQ) for thinking about these questions, and [here's one](https://youtu.be/S-6YGPrmtYc) that goes into somewhat more detail. Here are some relevant examples: 
    - A recipe recommendation app can privilege the cuisines of some locales over others. Will your user search recipes by ingredients? Peanut butter and tomato might seem an odd combination in the context of European cuisine, but is common in many traditional dishes of the African diaspora. A similar set of questions applies to recommendation systems related to style or beauty. 
    - A sentiment analyzer must be trained on specific languages. What languages will be included? Will diverse dialects be included, or only the "standard" version of the target language? Who would be excluded by such a choice, and how will you communicate about your limitations? 

A related question is: *should this app exist*? In a few sentences, discuss the following questions:  

1. What groups of people have the potential to **benefit** from the existence of our product? 
2. What groups of people have the potential to be **harmed** from the existence of our product? 
3. Will the world become an **overall better place** because of the existence of our product? Describe at least 2 **assumptions** behind your answer. For example, if your project aims to make it easier to predict crime, your assumptions might include: 
    - Criminal activity is predictable based on other features of a person or location. 
    - The world is a better place when police are able to perform their roles more efficiently. 

### Tentative Timeline 

There will be checkpoints for the project at approximately two-week intervals. With this in mind, please describe what you expect to achieve after **two**, **four**, and **six** weeks. At each stage, you should have "something that works." For example, maybe in two weeks you'll ready to demonstrate the data acquisition pipeline, in four weeks you'll be able to demonstrate some data analysis, and in six weeks you'll have your full machine learning pipeline set up. Please keep in mind that you'll be asked to present at each of these checkpoints. Showing "something that works" will usually be necessary for full credit. The "something that works" idea is related to the common concept of "minimum viable products" in software development, and is visually illustrated here:  
![First row:  sad faces above a single wheel, two wheels, a car without a roof, and finally a happy face above a completed car. Second row: a face becoming progressively happier above a skateboard, scooter, bicycle, motorcycle, and car.](https://miro.medium.com/max/2604/1*aXIr4rEoYwsTLuS2L1-UmQ.png)    

If you have any questions about this, please don't hesitate to ask me. 

<div class="fancy-h1"> Proposal Specifications </div>

Your proposal meets specs and will receive credit if: 

1. The proposal is hosted on GitHub as the top-level README.md file in a repository hosted by one of the group members. 
2. Each team member has made at least two commits to this file, which in total demonstrate substantial commitments to the writing of the proposal. 
3. The proposal contains thoughtful discussion in each of the required sections, which addresses all of the questions posed in each one. 
4. The proposal is written in clear English prose. Within reason, grammatical mistakes are not a problem.  
5. You have submitted a link to the proposal on CCLE by the stated deadline. 


## Length

There is no specifically required length for the proposal. Generally speaking, I would expect a thoughtful proposal to require around 600-900 words (roughly the length of 2-3 double-spaced pages). However, any length is acceptable provided that it provides thoughtful discussion of each of the required components.  
