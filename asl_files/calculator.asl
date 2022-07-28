while(1 == 1)

    echo "--------------- Calculator --------------- "
    num1 = 0
    num2 = 0
    op = 0

    echo "Please enter number 1"
    input num1

    echo "Please Enter Operation:"
    echo "  1 for +"
    echo "  2 for -"
    echo "  3 for *"
    echo "  4 for /"
    input op

    echo "Please enter number 2"
    input num2

    result = 0
    if (op == "plus")
        result = num1 + num2
    elif (op == 2)
        result = num1 - num2
    elif (op == 3)
        result = num1 * num2
    elif (op == 4)
        result = num1 / num2
    else
        echo "invalid operation"
    fi

    echo "Result: {result}"

    echo "To continue, enter 1, to exit enter 2"

    cmd = 1
    input cmd

    if (cmd == 1)
        continue
    else
        break
    fi
endwhile