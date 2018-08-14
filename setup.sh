#!/bin/bash

# Environment variables
export PANDOC_TEMPLATES=`pwd`/templates
export PANDOC_SCRIPTS=`pwd`/scripts
export PANDOC_FILTERS=`pwd`/filters

# Update the path
PATH=$PATH:${PANDOC_SCRIPTS}

# Locally install python helper packages
cd jupy_pandoc_utils/.
pip install -e .  --user
cd -
