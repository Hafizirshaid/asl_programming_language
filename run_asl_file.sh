#!/bin/bash

PYTHON=/usr/local/bin/python3
FOLDER_NAME=asl_files
ERROR_COUNT=0

for i in $(ls $FOLDER_NAME/*.asl); do

    echo "------ Running $i `date` ------"

    $PYTHON asl.py -f $i

    RESULT=$?

    if [ $RESULT -eq 0 ]; then
        echo "Pass"
    else
        echo "Fail"

        ERROR_COUNT=$(expr $ERROR_COUNT + 1)
    fi

    echo "Result: $RESULT"
    echo "------ Done $i    `date` ------"

done

echo "ERRORS: $ERROR_COUNT"

