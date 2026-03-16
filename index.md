---
layout: default
title: InsightGinie
---

# InsightGinie

Official site: <a href="https://insightginie.com">News of Tomorrow</a>

This repository is a mirror of the InsightGinie knowledge archive.

---

## Categories

<ul>

{% for category in site.categories %}

<li>
<a href="/{{ category[0] }}/">
{{ category[0] | capitalize }} ({{ category[1].size }})
</a>
</li>

{% endfor %}

</ul>