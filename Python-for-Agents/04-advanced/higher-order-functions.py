
"""
HIGHER-ORDER FUNCTIONS IN PYTHON

Topics:
1. First-class functions
2. Passing functions as arguments
3. Returning functions
4. map()
5. filter()
6. sorted() with key
7. reduce()
8. Function composition
9. Callbacks
10. AI-related applications
"""

from functools import reduce
from collections.abc import Callable


# ============================================================
# 1. FIRST-CLASS FUNCTIONS
# ============================================================

def greet():
    return "Hello from Python"


# Assigning a function to another variable
greeting = greet

print("\n1. FIRST-CLASS FUNCTIONS")
print(greeting())


# ============================================================
# 2. PASSING FUNCTIONS AS ARGUMENTS
# ============================================================

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(a, b, operation):
    return operation(a, b)


print("\n2. PASSING FUNCTIONS AS ARGUMENTS")

print(calculate(10, 5, add))
print(calculate(10, 5, multiply))


# ============================================================
# 3. RETURNING FUNCTIONS
# ============================================================

def select_operation(operation):

    if operation == "square":
        return lambda number: number ** 2

    elif operation == "cube":
        return lambda number: number ** 3

    else:
        raise ValueError("Unsupported operation")


square_function = select_operation("square")
cube_function = select_operation("cube")

print("\n3. RETURNING FUNCTIONS")

print(square_function(4))
print(cube_function(4))


# ============================================================
# 4. MAP()
# ============================================================

numbers = [1, 2, 3, 4, 5]


def square(number):
    return number ** 2


squared_numbers = list(map(square, numbers))

print("\n4. MAP()")
print(squared_numbers)


# Using lambda with map()

doubled_numbers = list(
    map(lambda number: number * 2, numbers)
)

print(doubled_numbers)


# ============================================================
# 5. FILTER()
# ============================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(number):
    return number % 2 == 0


even_numbers = list(filter(is_even, numbers))

print("\n5. FILTER()")
print(even_numbers)


# Filter numbers greater than 5

large_numbers = list(
    filter(lambda number: number > 5, numbers)
)

print(large_numbers)


# ============================================================
# 6. SORTED() WITH KEY
# ============================================================

students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95)
]


# Sort by marks
students_by_marks = sorted(
    students,
    key=lambda student: student[1]
)

print("\n6. SORTED()")
print("Ascending:", students_by_marks)


# Sort by marks in descending order
students_by_marks_desc = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Descending:", students_by_marks_desc)


# ============================================================
# 7. REDUCE()
# ============================================================

numbers = [1, 2, 3, 4, 5]


total = reduce(
    lambda accumulated, current: accumulated + current,
    numbers
)

product = reduce(
    lambda accumulated, current: accumulated * current,
    numbers
)

print("\n7. REDUCE()")
print("Sum:", total)
print("Product:", product)


# ============================================================
# 8. FUNCTION COMPOSITION
# ============================================================

def add_ten(number):
    return number + 10


def multiply_by_two(number):
    return number * 2


def compose(function_one, function_two):
    def combined(value):
        return function_two(function_one(value))

    return combined


operation = compose(add_ten, multiply_by_two)

print("\n8. FUNCTION COMPOSITION")
print(operation(5))


# ============================================================
# 9. CALLBACK FUNCTIONS
# ============================================================

def on_success():
    print("Operation completed successfully")


def process_data(callback):
    print("Processing data...")
    callback()


print("\n9. CALLBACKS")
process_data(on_success)


# ============================================================
# 10. TYPE HINTS WITH CALLABLE
# ============================================================

def execute(
    operation: Callable[[int], int],
    number: int
) -> int:
    return operation(number)


def triple(number: int) -> int:
    return number * 3


print("\n10. CALLABLE TYPE HINT")
print(execute(triple, 5))


# ============================================================
# 11. FUNCTION REGISTRY
# ============================================================

def search_tool(query):
    return f"Searching for: {query}"


def calculator_tool(expression):
    return f"Calculating: {expression}"


def execute_tool(tool_function, argument):
    return tool_function(argument)


tools = {
    "search": search_tool,
    "calculator": calculator_tool
}


print("\n11. FUNCTION REGISTRY")

selected_tool = tools["search"]

print(execute_tool(selected_tool, "Python higher-order functions"))


# ============================================================
# 12. AI APPLICATION: FILTER MODEL PREDICTIONS
# ============================================================

predictions = [
    {"label": "spam", "confidence": 0.98},
    {"label": "ham", "confidence": 0.65},
    {"label": "spam", "confidence": 0.91},
    {"label": "ham", "confidence": 0.40}
]


def high_confidence(prediction):
    return prediction["confidence"] >= 0.80


filtered_predictions = list(
    filter(high_confidence, predictions)
)

print("\n12. AI MODEL PREDICTIONS")
print(filtered_predictions)


# ============================================================
# 13. AI APPLICATION: RANK RETRIEVED DOCUMENTS
# ============================================================

documents = [
    {"content": "Python fundamentals", "score": 0.75},
    {"content": "Advanced Python", "score": 0.95},
    {"content": "Java fundamentals", "score": 0.60},
    {"content": "Python functions", "score": 0.88}
]


ranked_documents = sorted(
    documents,
    key=lambda document: document["score"],
    reverse=True
)

print("\n13. RANKED DOCUMENTS")

for document in ranked_documents:
    print(document)


# ============================================================
# 14. PRACTICE EXERCISES
# ============================================================

"""
EXERCISE 1:
Create a function that accepts another function
and executes it with a given number.

EXERCISE 2:
Create a function that returns another function
which calculates the square of a number.

EXERCISE 3:
Use map() to convert a list of temperatures
from Celsius to Fahrenheit.

Formula:
Fahrenheit = (Celsius * 9/5) + 32

EXERCISE 4:
Use filter() to extract numbers divisible by 3.

EXERCISE 5:
Sort a list of dictionaries containing employee
names and salaries by salary in descending order.

EXERCISE 6:
Use reduce() to calculate the maximum value
in a list of numbers.

EXERCISE 7:
Create a function composition system that combines
three functions in sequence.

EXERCISE 8:
Create a callback function that executes after
a simulated data processing operation.

EXERCISE 9:
Create a function registry containing:
- search
- calculator
- summarise

Allow the user to select and execute a tool.

EXERCISE 10:
Given a list of AI predictions, use filter()
to retain predictions with confidence >= 0.90.
"""


# ============================================================
# END OF HIGHER-ORDER FUNCTIONS
# ============================================================
