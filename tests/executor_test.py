# Author: Hafez Irshaid <hafezkm.irshaid@wmich.edu>.

"""

Executor Unit Test

"""

from io import StringIO
import unittest
import sys

from asl_runner import AslRunner

class ExecutorUnitTest(unittest.TestCase):
    def setUp(self):
        super(ExecutorUnitTest, self).setUp()


    def test_executor_empty(self):
        code = """
        // no code
        """
        old_stdout = sys.stdout
        old_stdin = sys.stdin
        sys.stdin = StringIO()
        string_out = StringIO()
        sys.stdout = string_out

        AslRunner().run(code)

        expected_output = ""

        actual_output = string_out.getvalue()

        self.assertEqual(expected_output, actual_output)
        sys.stdout = old_stdout
        sys.stdin = old_stdin
        pass

    def test_executor_fibonacci_number(self):
        code = """
i = 0
n = 30
t1 = 0
t2 = 1
sum = 0
print_Val = 10
break_var = 22
i = 2

while (i < n)
    sum = t1 + t2
    t1 = t2
    t2 = sum
    i = i + 1
    echo "sum {sum}"
endwhile
"""
        old_stdout = sys.stdout
        old_stdin = sys.stdin
        sys.stdin = StringIO()
        string_out = StringIO()
        sys.stdout = string_out

        AslRunner().run(code)

        expected_output = """sum 1.0
sum 2.0
sum 3.0
sum 5.0
sum 8.0
sum 13.0
sum 21.0
sum 34.0
sum 55.0
sum 89.0
sum 144.0
sum 233.0
sum 377.0
sum 610.0
sum 987.0
sum 1597.0
sum 2584.0
sum 4181.0
sum 6765.0
sum 10946.0
sum 17711.0
sum 28657.0
sum 46368.0
sum 75025.0
sum 121393.0
sum 196418.0
sum 317811.0
sum 514229.0
"""

        actual_output = string_out.getvalue()

        self.assertEqual(expected_output, actual_output)
        sys.stdout = old_stdout
        sys.stdin = old_stdin
        pass

    def test_echo_string(self):
        code = """
        echo "hello, world!"
        """

        old_stdout = sys.stdout
        old_stdin = sys.stdin
        sys.stdin = StringIO()
        string_out = StringIO()
        sys.stdout = string_out

        AslRunner().run(code)

        expected_output = """hello, world!
"""

        actual_output = string_out.getvalue()

        self.assertEqual(expected_output, actual_output)
        sys.stdout = old_stdout
        sys.stdin = old_stdin

    def test_executor_input(self):
        code = """
var = 0
input var
echo "user input is {var}"
"""
        old_stdout = sys.stdout
        old_stdin = sys.stdin
        sys.stdin = StringIO("10\n")
        string_out = StringIO()
        sys.stdout = string_out
        AslRunner().run(code)
        sys.stdout = old_stdout
        sys.stdin = old_stdin
        expected_output = """user input is 10
"""
        actual_output = string_out.getvalue()
        self.assertEqual(actual_output, expected_output)

        pass

    def tearDown(self):
        super(ExecutorUnitTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
