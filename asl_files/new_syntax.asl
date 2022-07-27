
x = 10
i = 0

yy
=
11
+
22
for(;;)
echo "bailout"
break
endfor
for          (     ;         ((i < 10) | (i < 22))         ;          )
    echo "hi {x} {i}"
    x = x + 1
    i = i + 1
endfor

echo "end"
echo "x is {x}"
if (
    (x < 20)
    |(x == 22)
    |(x == 21)
    |(x == 32)
    )
    echo "hi"

elif ( (x == 44)  |
        (x == 22) |
        (x == 33)
    )
        echo "hello"
else

    echo "hello"

endif

x = 32.0
echo "x is {x}"


while (
    x < 45
)
    echo "x is {x}"
    x = x + 1
endwhile

for (i = 0;
     i < 10;
     i = i +1)
    echo "hello"
endfor