#!/bin/bash

# PDF via latex
pandoc -N -s RapportActivite.md -o RapportActivite.pdf --template ${PANDOC_TEMPLATES}/document_template.tex \
       -V geometry="a4paper, total={6in,9in}" \
       --toc --toc-depth=2 -V display-abstract\
       --bibliography biblio.bib --filter pandoc-citeproc --csl apa.csl --metadata link-citations=true \
       -V linestretch="1.3" -V fontsize="11pt" -V language="francais" \
       -V fontfamily="gillius" -V fontoption="default"

# HTML
pandoc -N -s RapportActivite.md -o RapportActivite.html --css ${PANDOC_TEMPLATES}/webstyle_template.css\
       --bibliography biblio.bib --filter pandoc-citeproc --csl apa.csl --metadata link-citations=true\
       --toc --toc-depth=1 -V display-abstract
