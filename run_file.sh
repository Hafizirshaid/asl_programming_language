#!/bin/bash

PYTHON=/usr/local/bin/python3

for i in `ls asl_files`;do
    echo "------running $i------"
    $PYTHON main.py -f asl_files/$i
    echo "------done $i------"
done