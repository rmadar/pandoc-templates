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
export PANDOC_TEMPLATES=<installation-dir>/pandoc-utils/templates
export PANDOC_SCRIPTS=<installation-dir>/pandoc-utils/scripts
export PANDOC_SCRIPTS=<installation-dir>/pandoc-utils/filters
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

The output slides can be found [here](examples/SimpleSlides/slides.pdf) and the corresponding article
with more details in the conclusion is [here](examples/SimpleSlides/article.pdf).


### Webpage

A webpage can be created using a customized css file `template/webstyle_template.css` and possible
a html file template (not yet created) with a given structure.
```
makeWebpage notes.md blogpost.html
```


## Run the examples

There are two available example that can be ran in the `example` directory. 
One is based on some notes I took during a conference ([article](examples/NoteSUSY2018/Article.pdf), [slides](examples/NoteSUSY2018/Slides.pdf), [html](examples/NoteSUSY2018/Webpage.htm)),
and the other is based on the notebooks produce with [jupyter notebook](http://jupyter.org/) and exported
in markdown via `nbconvert` ([article](examples/BookRandomTopics/RandomTopics.pdf), [html](examples/BookRandomTopics/RandomTopics.html)).
[Another example](examples/ActivityReport) shows with bibliography in both pdf and html.



## Technical comments

## Dependencies

- [fvextra](https://ctan.org/pkg/fvextra?lang=en) latex package, to be installed with miktex as
```
sudo cp fvextra /usr/share/texlive/texmf-dist/tex/latex/.
sudo mktexlsr
```


### To-do list

It might be interesting to have a look to [pandoc filter in python](https://github.com/jgm/pandocfilters) in 
order to properly perform the tasks below (and possibly many more).

### Bibliography

- [x] adjust the bibliography style
- [x] enable bibliography counting - if possible?


### Beamer template

- [ ] add logos on beamer presentations
- [ ] define a block appearing only on slides and not in the article 
(equivalent to `<div class="note">` but for slides only)

### Latex template

- [ ] tune title page for LaTeX books
- [ ] modify latex template to remove horizontal line (so that slide transition don't appear in article.pdf)


### HTML/css templates

- [x] center subtitle  


### Using jupyter notebook

- [ ] can we find a cleaner way to remove the environment verbatim in pandoc (instead of [manual_remove_verbatim.py](filters/manual_remove_verbatim.py acting on the `tex` file)?
- [ ] references works for article conversion but not beamer slides. The issue is because there is no `frame` environment to print the biblio
- [ ] investigate/test html and tune the css file for the notebook
- [ ] check the exported figure with pdf format and how to add caption (for ouput of codes)
- [ ] pandas dataframe output as markdown, not html (check [pytablewriter](https://github.com/thombashi/pytablewriter) or []())
