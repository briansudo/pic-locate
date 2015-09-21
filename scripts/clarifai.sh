#!/bin/bash
FILES=/Users/briansu/workspace/test/$1/*
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  curl -H "Authorization: Bearer feNDrMZUC5zmvDY1aPSvzWwsID6xK8" -F "encoded_data=@$f" https://api.clarifai.com/v1/tag/ > $f.json
done
