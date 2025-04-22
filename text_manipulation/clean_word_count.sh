#!/bin/bash

file="input.txt"

# If file exists AND is not empty
if [ -f "$file" ] && [ -s "$file" ]; then
  echo "Word frequency:"
  
  grep -vE '^#|^$' "$file" | \
  sed "s/[^a-zA-Z']//g" | \
  tr 'A-Z' 'a-z' | \
  tr -s ' ' | \
  tr ' ' '\n' | \
  grep -v '^$' | \
  awk '{count[$1]++} END {for (w in count) printf "%-10s %d\n", w, count[w]}' | \
  sort -k2,2nr -k1,1

else
  echo "Error: File is missing or empty." >&2
  exit 1
fi
