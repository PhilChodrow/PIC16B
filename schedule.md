---
layout: page
title: Sequence of Topics
permalink: schedule/
---

This is the *rough* sequence of topics that we'll study in this course. 
We'll cover *most* of the topics below, in *approximately* the order listed. 
The exact schedule of topics, as well as things like due dates for assignments, will be available through BruinLearn. 

{% assign sorted = site.days | sort: 'order' %}

## Workflows

<ul>
{% for day in sorted %}
  {% if day.subject == "workflows" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Advanced Data Wrangling and Visualization

<ul>
{% for day in sorted %}
  {% if day.subject == "EDA" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Web Scraping

<ul>
{% for day in sorted %}
  {% if day.subject == "scrape" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Web Development with Flask

<ul>
{% for day in sorted %}
  {% if day.subject == "webdev" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Computational Math for Data Science

<ul>
{% for day in sorted %}
  {% if day.subject == "math" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Deep Learning with TensorFlow

<ul>
{% for day in sorted %}
  {% if day.subject == "tf" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Network Science

<ul>
{% for day in sorted %}
  {% if day.subject == "nx" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

## Other

<ul>
{% for day in sorted %}
  {% if day.subject == "other" %}
    <li>
        <a href="{{ day.link }}" title="{{ day.title }}">{{ day.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>