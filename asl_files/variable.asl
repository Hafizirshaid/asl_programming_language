x = 10
y = 20
z = 11

echo  "{x} y {y} z {z}"
w = x
echo "w is {w}"

if "x == 10"
    zz = w
    echo "{zz}"
    x = w + 1
    zz = w + 1
    echo "zz {zz} x {x}"
    if "x == 11"
        old = 1222
        echo "old {old}"
        xx = w
        y = w + 1
        xx = w + 1
        echo "zz {xx} x {y} x {x}"
    fi
echo "hi"

fi

echo "hi2"