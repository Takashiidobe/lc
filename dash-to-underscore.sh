#!/bin/bash
for file in *.py
do
  mv -- "$file" "${file//-/_}"
done

