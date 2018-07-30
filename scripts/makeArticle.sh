#!/bin/bash

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   ./makeArticle.sh <input.md> <output.pdf>"
    echo ""
    exit 1
fi

# PDF via latex
pandoc -N ${1} -o ${2} --template ../templates/document_template.tex \
       --variable geometry="a4paper, total={6in, 9in}" -V linestretch="1.2" -V fontsize="11pt"\
       --listings  --highlight-style kate\
       --toc
