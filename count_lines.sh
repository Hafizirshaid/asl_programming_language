#!/bin/bash

count=0

files_list=$(find . -name "*.py")

for i in $files_list; do

    c=$(cat $i | wc -l | awk '{print $1}')

    count=`expr $count + $c`

done

echo $count