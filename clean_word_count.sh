#!/bin/bash

[ -s input.txt ] && echo "Word Count:" || { echo "File is empty or missing."; exit 1; }

grep -vE '^#|^$' input.txt | \
sed 's/[^a-zA-Z ]//g' | \
tr 'A-Z' 'a-z' | \
tr -s ' ' | \
tr ' ' '\n' | \
grep -v '^$' | \
awk '{count[$1]++} END {for (w in count) printf "%-10s %d\n", w, count[w]}' | sort
