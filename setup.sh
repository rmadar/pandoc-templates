#!/bin/bash

export PANDOC_TEMPLATES=`pwd`/templates
export PANDOC_SCRIPTS=`pwd`/scripts
PATH=$PATH:${PANDOC_SCRIPTS}
