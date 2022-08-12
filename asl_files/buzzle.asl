echo("a  b  c")
for (a = 0; a <= 100; a += 1)
    for (b = 0; b <= 100; b += 1)
        for (c = 0; c <= 100; c += 1)
            x = b + (0.5 * a) + (5 * c)
            y = a + b + c
            if ((x == 100) & (y == 100))
                echo("{a} {b} {c}")
            fi
        endfor
    endfor
endfor
3.0 38.0 73.0