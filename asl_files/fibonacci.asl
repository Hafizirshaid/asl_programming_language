i = 0
n = 30
t1 = 0
t2 = 1
sum = 0

i = 2

while (i < n)
    sum = t1 + t2
    t1 = t2
    t2 = sum
    i = i + 1
    echo "sum {sum}"
endwhile