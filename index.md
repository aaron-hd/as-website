---
title: "Asymptotic Safety Seminars"
layout: splash
date: 2016-03-23T11:48:41-04:00
header:
  overlay_color: "#000"
  overlay_filter: "0"
  overlay_image: /assets/images/zooming.png
  actions:
    - label: "Learn More"
      url: "/about/"
#  caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
excerpt: "An international online seminar series. Since 2011."
intro: 
  - excerpt: 'The international seminar on asymptotic safety was founded in spring 2011, with the intention of bringing the asymptotic-safety community together, and providing a platform for talks on asymptotic safety in and beyond quantum gravity, as well as related topics in quantum gravity and quantum field theory.
If you are interested in attending the seminars, please contact one of the three organizers (link to organizers) to join the corresponding mailing list.'

feature_row:
  - image_path: assets/images/eichhorn.png
#    image_caption: "Thomas Frandsen/VILLUM FONDEN"
    alt: "placeholder image 1"
    title: "Astrid Eichhorn"
    excerpt: "Astrid is an Associate Professor at CP3-Origins, University of Southern Denmark, Villum Young Investigator and Perimeter Institute Visiting Fellow. She works on building connections in quantum gravity: connections between quantum-gravity approaches, connections between fundamental theory and phenomenology, and connections between neighboring research communities. [more](https://www.cp3-origins.dk/people/eichhorn-astrid/)"
  - image_path: /assets/images/aaron.png
    alt: "placeholder image 2"
    title: "Aaron Held"
    excerpt: "Aaron works on phenomenological constraints in quantum and classical effective field theories of gravity. Currently Royal Society Newton International Fellow at Imperial College London."
  - image_path: /assets/images/marc.png
    title: "Marc Schiffer"
    excerpt: "Marc works on ..."
---

{% include feature_row id="intro" type="center" %}

***Recent past seminars***

<div class="grid__wrapper">
  {% for post in site.posts limit:4 %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
<br/>&nbsp;<br/>

---

***The organizers***

{% include feature_row %}
