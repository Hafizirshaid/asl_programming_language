x = 10

for "i=0;i<50;i=i+1"

    if "i==x"
        echo "i is {i} and we should break"
        break
    fi
    echo "again {i} not reaching {x}"
endfor
echo "end of for"

//break

while "x < 20"
    echo "printing x {x}"
    if "x == 15"
        echo "should break now---- but before another loop inside break"
        x = 5
        for "i=0;i<10;i=i+1"
            if "i==x"
                echo "i is {i} and we should break for loop"
                break
            fi
            echo "again {i} not reaching {x}"
        endfor
        echo "----- breaking while ------"
        break
    fi
    x = x + 1
endwhile

