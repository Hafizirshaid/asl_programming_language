#!/bin/bash

PYTHON=/usr/local/bin/python3
FOLDER_NAME=asl_files

for i in $(ls $FOLDER_NAME/*.asl);do

    echo "------ Running $i `date` ------"

    $PYTHON main.py -f $i

    echo "------ Done $i    `date` ------"

done
