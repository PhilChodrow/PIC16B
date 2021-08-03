---
layout: post
title:  "Project Proposal"
date:   2021-05-16 15:36:27
categories: project assignment
permalink: posts/project-proposal
author: Phil Chodrow
---

In this assignment, you'll do two things: 

1. You'll get some practice using *collaborative workflows* with git and GitHub. 
2. You'll formally propose your project.

Please note that you should be in active communication with your project partners when completing this assignment. For Parts §1 and §2, it's probably easiest to hop on a video call and complete them all together in one sitting. For Part §3, in which you'll actually write your proposal, you should probably make a plan as a group, split up to do some writing, and then make a time to meet back to discuss and make revisions. 

## §1. Create the Project Repository

**One** member of the group should go on GitHub.com and create the project repository. This is the central location that will house your project files. After creating the project repository, this group member should add all other group members as collaborators on the project (under Settings --> Manage Access). 

All group members should now clone the repository. 

{::options parse_block_html="true" /}
<div class="gave-help">
**Do not** fork the project repository, as this will lead to everyone having their own private version. Not very collaborative! 
</div>
{::options parse_block_html="false" /}

By the end of this step, you now have a shared repository, under version control, in which you can all collaborate. This is where your project files, including code and data, will live. 

## §2. Collaborative Workflows in Git

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

## §3. Write Your Project Proposal

Write your project proposal in your project repository. For now, you can just use the file `README.md` to hold your proposal; this has the benefit that GitHub.com will automatically render it for you. Specs for your proposal are below. 

{::options parse_block_html="true" /}
<div class="gave-help">
Please ensure that all group members participate in writing the proposal. In particular, **each group member should commit at least two changes to the proposal document.** 
</div>
{::options parse_block_html="false" /}

### Required Components

You are required to include sections in your proposal that address the following topics. Feel free to include additional sections as needed. 

1. **Abstract**: In 2-4 sentences, describe what problem the project addresses, and the overall approach you will use to solve that problem. 
2. **Planned Deliverables**: Concisely state what you are going to create and what capabilities it will have. Are you making a webapp? A Python package for others to use? Code that creates a novel data set? Etc. Please consider two scenarios: 
    - "Full success." What will your deliverable be if everything works out for you exactly as you plan?
    - "Partial success." What useful deliverable will you be able to offer even if things don't 100% work out? For example, maybe you aren't able to get that webapp together, but you can still create a code repository that showcases the machine learning pipeline needed to use to support the app. Have a contingency plan! 
3. **Resources Required**: Do you need certain data sets? Do you know whether those data sets exist? Are they freely accessible? You should do at least a small amount of research for this part, in which you convince me that there is good reason to believe that you will be able to access or obtain the resources needed for your proposal. 
4. **Tools/Skills Required**: What skills will you need? Machine learning, database management, complex visualization, something else? If you know the names of Python packages that you will need to use, include them here. If you're not sure, just describe the skills or tasks you will need to accomplish.
5. **Risks**: What are two things that could potentially stop you from achieving the full deliverable above? Maybe it turns out that the data doesn't exist and you need change plan? Or maybe your idea requires more computational power than is available to you? What particular risks might be applicable for your project?
6. **Ethics**: All projects we undertake involve decisions about whose interests matter; which problems are important; and which tradeoffs are considered acceptable. Take some time to reflect on the potential impacts of your product on its users and the broader world. If you can see potential biases or harms from your work, describe some of the ways in which you will work to mitigate them. Remember that even relatively simple ideas can have unexpected and impactful biases. [Here's a nice introductory video](https://youtu.be/Ok5sKLXqynQ) for thinking about these questions, and [here's one](https://youtu.be/S-6YGPrmtYc) that goes into somewhat more detail. Here are some relevant examples: 
    - Will your recipe recommender app privilege the cuisines of some cultures above others? For example, peanut butter and tomato might seem an odd combination in the context of European cuisine, but is common in many traditional dishes of the African diaspora. A similar set of questions applies to recommendation systems related to style or beauty. 
    - What data set will your sentiment analysis be trained on? What languages will be included? Will diverse dialects be included, or only the "standard" version of the target language? Who would be excluded by such a choice, and how will you communicate about your limitations? 
    - Will your facial recognition system work well well on *all* faces, or will it systematically underperform on certain marginalized subgroups? (see the videos above for examples of this.)
7. **Tentative Timeline**: There will be checkpoints for the project at approximately two-week intervals. With this in mind, please describe what you expect to achieve after **two**, **four**, and **six** weeks. At each stage, you should have "something that works." For example, maybe by Week 2 you're ready to demonstrate the data acquisition pipeline, by Week 4 you can demonstrate some data analysis, and by Week 6 you have your full machine learning pipeline set up. Please keep in mind that you'll be asked to present at each of these checkpoints. Showing "something that works" will usually be necessary for full credit. The "something that works" idea is related to the common concept of "minimum viable products" in software development, and is visually illustrated here:  
![First row:  sad faces above a single wheel, two wheels, a car without a roof, and finally a happy face above a completed car. Second row: a face becoming progressively happier above a skateboard, scooter, bicycle, motorcycle, and car.](https://miro.medium.com/max/2604/1*aXIr4rEoYwsTLuS2L1-UmQ.png)    

### Length

There is no specifically required length for the proposal. Generally speaking, I would expect a thoughtful proposal to require at least 600 words (roughly the length of two double-spaced pages.)