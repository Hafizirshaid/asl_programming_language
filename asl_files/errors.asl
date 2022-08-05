x = 1
y = 2
z = 0
w = 1
x += 20 + w

print ("x = {x} y = {y} z = {z} w = {w}")
for (i = (x * y) / 2; i < 10; i += (x + z) + 1)
//for (i = (x * y) / 2; i < 10; i += 1)
    echo ("hello {i}")
endfor

// infinite loop

counter = 0
while (1 == 1)
    echo ("hafiz")
    counter += 1

    if (counter == 10)
        echo ("breaking")
        break
    fi
endwhile