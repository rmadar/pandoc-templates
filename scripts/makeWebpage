#!/bin/bash

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   ./makeWebpage.sh <input.md> <output.pdf>"
    echo ""
    exit 1
fi

# HTML
pandoc -N -s ${1} -o ${2} --highlight-style kate --mathjax --css ${PANDOC_TEMPLATES}/webstyle_template.css --toc
