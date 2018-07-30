#!/bin/bash

if [ $# -ne 2 ]; then
    echo ""
    echo "Script usage: "
    echo "   ./makeWebpage.sh <input.md> <output.pdf>"
    echo ""
    exit 1
fi

# HTML
pandoc -N ${1} -o ${2} --highlight-style kate --mathjax --css ../templates/webstyle_template.css --toc
