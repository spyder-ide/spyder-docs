#!/bin/bash -ex

pip3 install -U pip
pip3 install sphinx doctr sphinx-panels sphinx-multiversion
# You can change the command above to use a different version of the theme (but return it to the correct one before merging)
pip3 install git+https://github.com/dalthviz/spyder-docs-sphinx-theme.git@sidebar_widgets
# Needed to build PR previews using Netlify with the different versions of the docs available
if [ "${CI-}" = "true" ]; then
    # Set up the actual branch to build on
    if [ "${PULL_REQUEST-}" = "true" ] || [ "${TRAVIS_PULL_REQUEST_BRANCH-}" != "" ]; then
        git branch current
    fi
    git config remote.origin.url >&- || git remote add origin https://github.com/spyder-ide/spyder-docs.git
    git fetch --all
fi
