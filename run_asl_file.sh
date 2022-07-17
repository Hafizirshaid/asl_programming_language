#!/bin/bash

PYTHON=/usr/local/bin/python3
FOLDER_NAME=asl_files

for i in $(ls $FOLDER_NAME);do

    echo "------ Running $i `date` ------"

    $PYTHON main.py -f $FOLDER_NAME/$i

    echo "------ Done $i    `date` ------"

done
