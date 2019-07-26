#!/bin/bash


mkdir pdf

for file in $(find . -name "*.md" | sed 's/.md$//')
do
    echo "Converting $file.md to PDF..."
    pandoc --variable urlcolor=cyan $file.md -o pdf/$file.pdf

done
