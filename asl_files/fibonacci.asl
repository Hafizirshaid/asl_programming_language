a = 0
b = 1
n = 10

// this program doesnt work correctly fix it

for (i = 0; i <= n; i = i + 1)
    a = b
    b = a + b
    echo "{b} {a}"
endfor