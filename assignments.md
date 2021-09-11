---
layout: page
title: Assignments
permalink: assignments/
---


# Preparation

These assignments are not themselves graded, but you will need to complete them in order to complete most other graded assignments. The due dates can be viewed as strong recommendations. 

<br>

<!-- <ul class="listing"> -->
<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %} 
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "preparation" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.due | date:"%m/%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>


# Blog Posts 

For blog posts, the listed date is the due date of the first submission. Second submissions, if required, will be due one week after receiving feedback on the first submission. 

Remember that there are 7 total blog posts. An A in the course requires credit for 6 of them. <span style="color: green;"><i class="far fa-check-circle"></i></span> **Complete (Late)** posts count for half, and you can also write the [optional essay]({{site.essay}}) in place of one blog post. 



<br>

<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "blog" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.due | date:"%m/%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>

# Project

Remember that *you need to earn credit for all project components* in order to earn a satisfactory grade in the course. The specifications for project activities are not too picky. If your situation doesn't allow you to complete a project activity on time, please let me know and we'll work it out an alternative way for you to earn credit. 

<br> 

<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "project" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.due | date:"%m/%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>