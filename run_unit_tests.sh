PYTHON=/usr/local/bin/python3
files_list=$(ls tests/*.py)

for i in $files_list; do

	echo $i
	$PYTHON -m unittest -f $i
done


