
for "num=2;num<1000;num=num+1"
    flag=0
    for "i=2;((i < num) & (flag == 0));i=i+1"
        if "(num % i) == 0"
            flag=1
        fi
    endfor

    if "flag==0"
        echo "{num} is prime"
    fi
endfor