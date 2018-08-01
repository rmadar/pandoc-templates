#!/bin/bash

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   makeReport <input.md> <output.pdf>"
    echo ""
    exit 1
fi

# PDF via latex
pandoc -N -s ${1} -o ${2} --template ${PANDOC_TEMPLATES}/document_template.tex \
       -V geometry="a4paper, total={6in,9in}" \
       --toc --toc-depth=2 -V display-abstract\
       --bibliography biblio.bib --filter pandoc-citeproc --csl apa.csl --metadata link-citations=true \
       -V linestretch="1.3" -V fontsize="11pt" -V language="francais" \
       -V fontfamily="gillius" -V fontoption="default"\
