
grade = 0
echo "please input grade: "
input grade

if ((grade >= 90) & (grade <= 100))
    echo "{grade} Outstanding"
elif ((grade >= 80) & (grade <= 90))
    echo "{grade} very good"
elif ((grade >= 70) & (grade <= 80))
    echo "{grade} good"
elif ((grade >= 60) & (grade <= 70))
    echo "{grade} fair"
elif ((grade >= 0) & (grade <= 60))
    echo "{grade} failure"
else
    echo "Invalid Grade"
fi