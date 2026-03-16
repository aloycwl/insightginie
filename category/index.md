---
layout: default
title: Categories
---

# Categories

<ul>

{% for category in site.categories %}

<li>
<a href="/category/{{ category[0] }}/">
{{ category[0] | capitalize }}
</a>

<ul>

{% for post in category[1] limit:20 %}

<li><a href="{{ post.url }}">{{ post.title }}</a></li>

{% endfor %}

</ul>

</li>

{% endfor %}

</ul>