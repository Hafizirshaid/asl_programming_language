echo "testing for loop"

for "var=1;var <= 10;var = var + 1"
    if "(var % 2) == 0"
        echo "{var} is even"
    else
        echo "{var} is odd"
    fi
endfor