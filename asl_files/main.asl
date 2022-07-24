echo "hello"
x = 10
if (12 >= 10)
    echo "x is grater than or equal 10"
else
    echo "x is not grater than or equal 10"
fi
// hello
echo "before for"

for (var=1; var > 10; var = var + 1)
    echo "inside for loop 1"
    echo "inside for loop 2"
    echo "inside for loop 3"
endfor

echo "after for"

y = 60
while (y > 50)
    echo "inside while loop"
    y = y - 1
    if (y == 10)
        echo "breaking ...."
    fi
endwhile
