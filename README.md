# Writting documentation with pandoc

This repository contains various templates and building scripts based on [pandoc](http://pandoc.org) 
in order to produce article, slides or webpage with a predifined (and tunable) style. The workflow model
of this repository the following:

> raw markdown -> [PANDOC] -> article/book/webpage/slide

The "pandoc box" needs templates and filters which are stored/installed in corresponding directories of the repository. Also, in order to properly break long code lines, the package `fvextra`. See [dependencies section](#dependencies) for more details.

The `raw markdown` file can be generated in two ways:
  1. simply with an editor
  2. using jupyter notebooks, where more work was needed.

First of all, cell tags where implemented in `nbconvert` template [nbconverter_md_pandoc.tpl](templates/nbconverter_md_pandoc.tpl) in order to hide a whole cell, its code or its output. But a proper generation of markdown file (including figure/table caption, hidding code, etc ...) from a notebook is not straightfoward. That's the reason why the python package [jupy_pandoc_utils](jupy_pandoc_utils) was developped. It allows to attach caption and label to figure and table, as well as automatically find `pdf` files to replace the `png` (optional). Having output plots as file lead to some refreshing issues (browser caching) that was worked around more or less manually.

---

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
### Create a markdown file from a notebook

Two main informations to exploit this tool:
  1. you need to import `jupy_pandoc_utils` package to get figure/table caption and lable.
  2. use the tags `hide`, `hide_input` and `hide_output` to select what you want to remove from your final document.

It is recommanded to read and run [this example notebook](examples/NotebookWithCode/test.ipynb), where all the features are demonstrated.

## Run the examples

There are two available example that can be ran in the `example` directory. 
One is based on some notes I took during a conference ([article](examples/NoteSUSY2018/Article.pdf), [slides](examples/NoteSUSY2018/Slides.pdf), [html](examples/NoteSUSY2018/Webpage.htm)),
and the other is based on the notebooks produce with [jupyter notebook](http://jupyter.org/) and exported
in markdown via `nbconvert` ([article](examples/BookRandomTopics/RandomTopics.pdf), [html](examples/BookRandomTopics/RandomTopics.html)).
[Another example](examples/ActivityReport) shows with bibliography in both pdf and html.

---

## Technical comments

## Dependencies

- [fvextra](https://ctan.org/pkg/fvextra?lang=en) latex package, to be installed with miktex as
```
sudo cp fvextra /usr/share/texlive/texmf-dist/tex/latex/.
sudo mktexlsr
```
- [tabulate](https://pypi.org/project/tabulate/) python package needed to properly render 
pandas dataframe in markdown, to be installed as
```
pip install tabulate
```
- [pandoc-crossref](https://github.com/lierdakil/pandoc-crossref) to be able to label table and figures. This can be installed by downloading the executable on [this page](https://github.com/lierdakil/pandoc-crossref/releases/tag/v0.3.2.1) and put it in `./filters/`


### To-do list

It might be interesting to have a look to [pandoc filter in python](https://github.com/jgm/pandocfilters) in 
order to properly perform the tasks below (and possibly many more).

### Cross-references
- [ ] `pandoc-crossref` works well but:
  1. there are no hyperlink for table in HTML (while it works in LaTeX)
  2. there is no counting of figure in HTML (while it works in LaTeX and for Tables in HTML too)

### Beamer template

- [ ] add logos on beamer presentations
- [ ] define a block appearing only on slides and not in the article 
(equivalent to `<div class="note">` but for slides only)

### Latex template

- [ ] tune title page for LaTeX books
- [ ] modify latex template to remove horizontal line (so that slide transition don't appear in article.pdf)


### Using jupyter notebook

- [x] implement a tag-filter system to hide input or output (copied on currently implement `hide` tag)
- [ ] references works for article conversion but not beamer slides. The issue is because there is no `frame` environment to print the biblio
- [x] investigate/test html and tune the css file for the notebook
- [x] check the exported figure with pdf format and how to add caption (for ouput of codes)
   + [x] solution found and implemted in [jupy_pandoc_utils](python_tools/jupy_pandoc_utils.py) 
   quite manual for now but it works, except for the NB visualisation online (main
   issue: *data caching* for `png`, worked around by creating a new `png` each time)
   + [x] but visualization needs the last `png` version (which always changes): how to solve these issues? Done by a cleaning script
   + [x] find a way to replace in `output.md` figure extension `png` by `pdf` when the pdf exist
- [x] pandas dataframe output as markdown, not html (check [tabulate](https://pypi.org/project/tabulate/))
