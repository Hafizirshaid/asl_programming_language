echo "while loop"
i = 0
end = 50
while (i <= end)
    if ((i % 2) == 0)
        echo "{i} is even"
    else
        echo "{i} is odd"
    fi
    i = i + 1
endwhile

echo "testing for loop"

for (var=1;var <= 10;var = var + 1)
    if ((var % 2) == 0)
        echo "{var} is even"
    else
        echo "{var} is odd"
    fi
endfor