
x = 10
for (i=0;i<50;i=i+1)
    echo "start"
    if (i==x)
        echo "i is {i} and we should continue"
        continue
    fi
    if (i==(x*2))
        echo "i is {i} and we should continue"
        continue
    fi
    echo "again {i} not reaching {x}"
    echo "end"
endfor
echo "end of for"
