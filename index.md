---
layout: default
title: InsightGinie
---

# InsightGinie

Official site: <a href="https://insightginie.com">News of Tomorrow</a>

This repository is a mirror of the InsightGinie knowledge archive.

---

## Categories

{% assign mains = "" | split: "" %}

{% for post in site.posts %}
{% assign mains = mains | push: post.categories[0] %}
{% endfor %}

{% assign mains = mains | uniq | sort %}

<ul>

{% for main in mains %}

<li>

<strong>{{ main | capitalize }}</strong>

<ul>

{% assign subs = "" | split: "" %}

{% for post in site.posts %}
{% if post.categories[0] == main and post.categories.size > 1 %}
{% assign subs = subs | push: post.categories[1] %}
{% endif %}
{% endfor %}

{% assign subs = subs | uniq | sort %}

{% for sub in subs %}

<li>
<a href="/{{ main }}/{{ sub }}/">
{{ sub | capitalize }}
</a>
</li>

{% endfor %}

</ul>

</li>

{% endfor %}

</ul>