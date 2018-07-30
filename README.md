# Writting documentation with pandoc

This repository contains various templates and building scripts based on [pandoc](http://pandoc.org) 
in order to produce article, slides or webpage with a predifined (and tunable) style.

## Setup the too

First the user need to setup the proper environemental variables by doing:
```
source setup.sh
```
This will make aware the system where are the pandoc templates and let the user call the script from anywhere.

## Run the examples

There are two available example that can be ran in the `example` directory. 
One is based on some notes I took during a conference ([article](), [slides](), [html]()),
and the other is based on the notebooks produce with (jupyter notebook)[] and exported
in markdown via `nbconvert` ([article](), [html]()).

## To-do-list

- [ ] modify latex template to remove horizontal line (so that slide transition don't appear in article.pdf)
- [ ] define a block appearing only on slides and not in the article 
(equivalent to `<div class="note">` but for slides only)