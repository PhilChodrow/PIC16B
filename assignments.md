---
layout: page
title: Assignments
permalink: assignments/
---

At the time of writing, the dates supplied are not meaningful. In the future, they will reflect due dates for first submissions. 

# Preparation

<!-- <ul class="listing"> -->
<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "preparation" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>


# Blog Posts 

<!-- <ul class="listing"> -->
<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "blog" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>

# Project

<dl>
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
  {% endif %}

  {% if post.categories.first == "project" %}
    <dt>
        <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time> 
    </dt>
    <dl>
        <a href="/PIC16B/{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    </dl>
  {% endif %}
{% endfor %}
</dl>