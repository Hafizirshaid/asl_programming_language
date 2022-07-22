#!/bin/bash

PYTHON=/usr/local/bin/python3
FOLDER_NAME=asl_files

for i in $(ls $FOLDER_NAME/*.asl);do

    echo "------ Running $i `date` ------"

    $PYTHON asl.py -f $i
    echo "Result: $?"
    echo "------ Done $i    `date` ------"

done
