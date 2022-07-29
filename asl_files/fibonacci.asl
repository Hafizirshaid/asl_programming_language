a = 0
b = 1
n = 10
for (i = 0; i < n; i = i + 1)
    echo "{b}"
    a = b
    b = a + b
endfor
