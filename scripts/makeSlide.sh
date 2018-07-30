#!/bin/bash

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   ./makeSlide.sh <input.md> <output.pdf>"
    echo ""
    exit 1
    fi

# Beamer slides
pandoc ${1} -o ${2} --to beamer --template ../templates/slides_template.tex --slide-level=2 \
       -V theme="CambridgeUS" -V colortheme="seagull" -V fonttheme="structurebold" -V fontfamily="libertine" \
       -V colorlinks\
       -V toc\
