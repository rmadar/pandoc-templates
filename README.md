# Writting documentation with pandoc

This repository contains various templates and building scripts based on [pandoc](http://pandoc.org) 
in order to produce article, slides or webpage with a predifined (and tunable) style.

## Setup the tool

First the user need to setup the proper environemental variables by doing:
```
source setup.sh
```
This will make aware the system where are the pandoc templates and let the user call the script from anywhere.
For an automatic setup, the user can use the following lines in `~/.bashrc` file:
```
export PANDOC_TEMPLATES=<installation-dir>/pandoc-templates/templates
export PANDOC_SCRIPTS=<installation-dir>/pandoc-templates/scripts
PATH=$PATH:${PANDOC_SCRIPTS}
```
where `<installation-dir>` is the directory where pandoc-templates is installed.

## Usage


### Latex article

```
makeArticle notes.md article.pdf
```

Title, author and abstract are specifed using the markdown file header. The table of contents is added by default
but this can be modified in `makeArticle`. The latex template `templates/document_template.tex` can be tuned/improved.


### Latex book

The same options are available then for the article (except the abstract).

```
makeBook notes.md book.pdf
```

### Latex slides

The beamer slide conversion uses another template `templates/beamer_template.tex` and the script `makeSlides`
contains a list of default option that can be simply changed.

```
makeSlides notes.md slides.pdf
```

The structure for the slides is the following
```
---
title: "My beautiful presentation"
author: ["Romain Madar"]
date: July 2018
...

# First section

## My first slide of the first section

This is the content of the slide called 'My first slide of the first section'.

---

This will be a second slide in section 'First section', without title.


## My second slide {.allowframebreaks}

This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'


This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'
This second slide can be very long, it will be splitted among
various slides thanks to the attribute '.allowframebreaks'

# Very poor second section

## Conclusion and outlooks

pandoc is great to actually create article, webpage and slides from the
same markdown file.

<div class="notes">
This text will appear only in the article/book/webpage but not in the beamer slides.
This could be useful to give additional details which don't fit a presentation but
a more complete document.
</div>
```

The output slides can be found [here](examples/SimpleSlides/slides.pdf) and the corresponding article
with more details in the conclusion is [here](examples/SimpleSlides/article.pdf).


### Webpage

```
makeWebpage notes.md blogpost.html
```


## Run the examples

There are two available example that can be ran in the `example` directory. 
One is based on some notes I took during a conference ([article](examples/NoteSUSY2018/Article.pdf), [slides](examples/NoteSUSY2018/Slides.pdf), [html](examples/NoteSUSY2018/Webpage.htm)),
and the other is based on the notebooks produce with [jupyter notebook](http://jupyter.org/) and exported
in markdown via `nbconvert` ([article](examples/BookRandomTopics/RandomTopics.pdf), [html](examples/BookRandomTopics/RandomTopics.html)).

## To-do-list

It might be interesting to have a look to [pandoc filter in python](https://github.com/jgm/pandocfilters) in 
order to properly perform the tasks below (and possibly many more).

- [ ] add logos on beamer presentations
- [ ] tune title page for LaTeX books
- [ ] modify latex template to remove horizontal line (so that slide transition don't appear in article.pdf)
- [ ] define a block appearing only on slides and not in the article 
(equivalent to `<div class="note">` but for slides only)
