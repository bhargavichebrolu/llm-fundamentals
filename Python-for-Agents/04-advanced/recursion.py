
"""
RECURSION IN PYTHON

Topics:
1. Base case and recursive case
2. Countdown
3. Sum of numbers
4. Factorial
5. Fibonacci
6. Memoization
7. String reversal
8. Nested list traversal
9. Tree traversal
10. Practice exercises
"""

from functools import cache


# ============================================================
# 1. COUNTDOWN
# ============================================================

def countdown(number):
    if number < 0:
        return

    if number == 0:
        print("Finished")
        return

    print(number)
    countdown(number - 1)


print("\n1. COUNTDOWN")
countdown(5)


# ============================================================
# 2. SUM OF NUMBERS FROM 1 TO N
# ============================================================

def recursive_sum(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    return number + recursive_sum(number - 1)


print("\n2. RECURSIVE SUM")
print(recursive_sum(5))


# ============================================================
# 3. FACTORIAL
# ============================================================

def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print("\n3. FACTORIAL")
print(factorial(5))


# ============================================================
# 4. FIBONACCI WITHOUT MEMOIZATION
# ============================================================

def fibonacci(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print("\n4. FIBONACCI")
print(fibonacci(6))


# ============================================================
# 5. FIBONACCI WITH MEMOIZATION
# ============================================================

@cache
def fibonacci_optimised(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return (
        fibonacci_optimised(number - 1)
        + fibonacci_optimised(number - 2)
    )


print("\n5. OPTIMISED FIBONACCI")
print(fibonacci_optimised(40))


# ============================================================
# 6. REVERSE A STRING
# ============================================================

def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


print("\n6. REVERSE STRING")
print(reverse_string("Python"))


# ============================================================
# 7. SUM OF A NESTED LIST
# ============================================================

def nested_list_sum(items):
    total = 0

    for item in items:
        if isinstance(item, list):
            total += nested_list_sum(item)
        else:
            total += item

    return total


nested_data = [1, 2, [3, 4, [5, 6]], 7]

print("\n7. NESTED LIST SUM")
print(nested_list_sum(nested_data))


# ============================================================
# 8. FIND MAXIMUM IN A LIST
# ============================================================

def recursive_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    if len(numbers) == 1:
        return numbers[0]

    maximum_of_rest = recursive_max(numbers[1:])

    return max(numbers[0], maximum_of_rest)


print("\n8. RECURSIVE MAXIMUM")
print(recursive_max([12, 45, 7, 89, 23]))


# ============================================================
# 9. TREE TRAVERSAL
# ============================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def traverse_tree(node):
    if node is None:
        return

    print(node.value)

    for child in node.children:
        traverse_tree(child)


root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

root.children = [node_b, node_c]
node_b.children = [node_d, node_e]

print("\n9. TREE TRAVERSAL")
traverse_tree(root)


# ============================================================
# 10. TRACE RECURSIVE EXECUTION
# ============================================================

def trace_recursion(number):
    print(f"Entering function: {number}")

    if number == 0:
        print("Base case reached")
        return

    trace_recursion(number - 1)

    print(f"Returning from function: {number}")


print("\n10. TRACE RECURSION")
trace_recursion(3)


# ============================================================
# 11. PRACTICE EXERCISES
# ============================================================

"""
EXERCISE 1:
Write a recursive function to print numbers
from 1 to 10.

EXERCISE 2:
Write a recursive function to calculate the
sum of numbers from 1 to n.

EXERCISE 3:
Write a recursive function to calculate the
factorial of a number.

EXERCISE 4:
Write a recursive Fibonacci function.

EXERCISE 5:
Optimise Fibonacci using functools.cache.

EXERCISE 6:
Write a recursive function to reverse a string.

EXERCISE 7:
Write a recursive function to calculate the sum
of all numbers in a nested list.

EXERCISE 8:
Write a recursive function to find the maximum
value in a list.

EXERCISE 9:
Create a tree and implement depth-first traversal.

EXERCISE 10:
Explain why naive recursive Fibonacci is inefficient.

RULE:
For every exercise, identify:
- Base case
- Recursive case
- How the input gets closer to the base case
- What each function call returns
"""


# ============================================================
# END OF RECURSION
# ============================================================
