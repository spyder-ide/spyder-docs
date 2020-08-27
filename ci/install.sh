#!/bin/bash -ex

pip3 install -U pip
pip3 install sphinx doctr sphinx-panels sphinx-multiversion
# You can change the command above to use a different version of the theme (but return it to the correct one before merging)
pip3 install git+https://github.com/dalthviz/spyder-docs-sphinx-theme.git@sidebar_widgets
# Needed to build PR previews using Netlify with the different versions of the docs available 
if [ "${PULL_REQUEST-}" = "true" ]; then
    git remote add origin https://github.com/spyder-ide/spyder-docs.git
    git fetch origin
    git branch pr
    git checkout master
    git pull origin master
    git checkout 3.x
    git pull origin 3.x
    git checkout pr
fi
