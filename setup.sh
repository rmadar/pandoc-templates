#!/bin/bash

export PANDOC_TEMPLATES=`pwd`/templates
export PANDOC_SCRIPTS=`pwd`/scripts
export PANDOC_FILTERS=`pwd`/filters
PATH=$PATH:${PANDOC_SCRIPTS}
