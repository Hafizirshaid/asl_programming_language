echo "hello"
x = 10
if (x >= 10)
    echo "x is grater than or equal 10"
else
    echo "x is not grater than or equal 10"
fi

for 1 to 10 incr 1
    echo "hello"
endfor

y = 60
while (y > 50)
    echo "inside while loop"
    y = y - 1
    if y == 10
        echo "breaking ...."
        break
    fi
endwhile
