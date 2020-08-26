#!/bin/bash -ex

pip3 install -U pip
pip3 install sphinx doctr sphinx-panels sphinx-multiversion
# You can change the command above to use a different version of the theme (but return it to the correct one before merging)
pip3 install git+https://github.com/dalthviz/spyder-docs-sphinx-theme.git@sidebar_widgets
make multidocs
