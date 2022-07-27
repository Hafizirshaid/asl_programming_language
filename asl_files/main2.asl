echo "------ start ------"
echo "helllo"

x = 10.1
y = 20
x = x + 10
y = y + 50
z = y - x
echo "x = §123-=+'/>,````$%@! is {x} y is {y} z is {z}"

if (x > 4)
    echo "if 1"
    x = 50
    y = 60
    z = 0
    if ((x > 29) & (z == 0))
        echo "looks like (x > 29) & (z == 0)"
        z = 299
        echo "inside second x {x}"
        x = 30
        w = 9
        echo "x is {x} y is {y} z is {z} w is {w}"
        if (x == 30)
            echo "x > 29"
            x = 80
            w = 99
        else
            echo "else 1"
        fi

        if (x == 80)
            echo "x is 80"
        fi
        echo "hi hafiz"
    else
        echo "else 111"
    fi
elif (x > 22)
    echo "elif"
    x = 77
    if (x == 29)
        echo "inside second x"
        x = 80
    else
        echo "else 1"
    fi
elif (x < 9)
    echo "elif 2"
    x = 00
    if (x == 29)
        echo "inside second x"
        x = 80
    else
        echo "else 1"
        hh = 33
    fi
else
    echo "else"
    echo "else else"
    if (x == 29)
        echo "inside second x"
        x = 80
        hh = 2
    else
        echo "else 1"
    fi
fi


echo "-------testing while loop ------"

xx = 1
while (xx < 10)
    echo "inside while loop {xx}"
    xx = xx + 1
endwhile

echo "---- end of program -----"
