#!/bin/bash

PYTHON=/usr/local/bin/python3
files_list=$(ls tests/*.py)

for i in $files_list; do
	echo $i
	$PYTHON -m unittest -f $i
	$PYTHON -m coverage run $i
	$PYTHON -m coverage html -d tests/coverage/coverage_$i/html
done
