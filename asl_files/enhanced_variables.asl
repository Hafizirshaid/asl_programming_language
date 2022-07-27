x = 10

echo "x is {x}"

x += 1

echo "x is {x} after increment"

y = 2


x += y

echo "x is {x} after adding y {y}"
z = x + y + 20
echo "z is {z}"

for (i = 0; i < 10; i += 1)
    echo "for loop {i}"
    i += 2

endfor


for (i = 0; i < 10; i += 1)
    xx = 1
    z += x + y + 20 + xx
    echo ("z is {z}")
endfor

echo ("end of program")
