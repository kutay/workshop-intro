#!/bin/bash


bundle config --local github.https true
bundle --path=.bundle/gems --binstubs=.bundle/.bin

trash-put *.html

bundle exec asciidoctor-revealjs -a revealjsdir=https://cdn.jsdelivr.net/npm/reveal.js@3.9.2 0*.adoc


