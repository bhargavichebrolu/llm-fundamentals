# Python Higher-Order Functions

## 1. What Is a Higher-Order Function?

A higher-order function is a function that does at least one of the following:

1. Accepts another function as an argument.
2. Returns another function as its result.

In Python, functions are first-class objects. This means functions can be:

- Assigned to variables.
- Passed as arguments to other functions.
- Returned from other functions.
- Stored in lists, tuples and dictionaries.

These capabilities make higher-order functions possible.

### Example 1: Passing a function as an argument

```python
def greet():
    return "Hello Python"


def execute_function(function):
    result = function()
    print(result)


execute_function(greet)
```

Output:

```text
Hello Python
```

Explanation:

- `greet` is a function.
- `execute_function()` accepts a function as an argument.
- `function()` executes the function it receives.
- `greet` is passed without parentheses because we are passing the function itself, not calling it immediately.

Here, `execute_function()` is a higher-order function.

### Example 2: Returning a function

```python
def outer():
    def inner():
        return "Hello from inner function"

    return inner


result = outer()

print(result())
```

Output:

```text
Hello from inner function
```

Explanation:

- `outer()` defines an inner function.
- `outer()` returns the inner function.
- `result` stores the returned function.
- `result()` executes it.

A function that returns another function is also a higher-order function.

---

## 2. First-Class Functions

Higher-order functions are possible because Python treats functions as first-class objects.

### 2.1 Assigning a function to a variable

```python
def calculate():
    return 100


operation = calculate

print(operation())
```

Output:

```text
100
```

`operation` now refers to the same function as `calculate`.

Notice the difference:

```python
operation = calculate
```

This assigns the function object.

```python
operation = calculate()
```

This executes the function and assigns its return value.

### 2.2 Passing functions as arguments

```python
def square(number):
    return number ** 2


def process(number, function):
    return function(number)


print(process(5, square))
```

Output:

```text
25
```

The `process()` function does not need to know how the calculation works. It receives the operation as an argument.

This makes functions reusable and flexible.

### 2.3 Returning functions

```python
def select_operation(operation):

    if operation == "square":
        return lambda number: number ** 2

    elif operation == "cube":
        return lambda number: number ** 3


square_function = select_operation("square")
cube_function = select_operation("cube")

print(square_function(4))
print(cube_function(4))
```

Output:

```text
16
64
```

The returned function can be stored and executed later.

---

## 3. Functions That Accept Other Functions

A higher-order function can receive another function and decide when to execute it.

Example:

```python
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def calculate(a, b, operation):
    return operation(a, b)


print(calculate(10, 5, add))
print(calculate(10, 5, multiply))
```

Output:

```text
15
50
```

The `calculate()` function is reusable because its behaviour depends on the function passed to it.

You can pass different operations without rewriting `calculate()`.

---

## 4. Built-in Higher-Order Functions

Python provides several useful functions that accept other functions.

Important examples:

- `map()`
- `filter()`
- `sorted()`
- `reduce()`

### 4.1 map()

`map()` applies a function to every element in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

def square(number):
    return number ** 2


result = map(square, numbers)

print(list(result))
```

Output:

```text
[1, 4, 9, 16, 25]
```

Explanation:

1. `map()` receives the `square` function.
2. It receives the `numbers` list.
3. It applies `square()` to every element.
4. It returns a map iterator.
5. `list()` converts the iterator into a list.

You can also use a lambda function:

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number ** 2, numbers)

print(list(result))
```

### 4.2 filter()

`filter()` selects elements based on a function that returns a truthy or falsy result.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0


result = filter(is_even, numbers)

print(list(result))
```

Output:

```text
[2, 4, 6, 8]
```

Explanation:

- `filter()` passes each element to `is_even()`.
- If the function returns `True`, the element is retained.
- If it returns `False`, the element is excluded.

### 4.3 sorted()

`sorted()` accepts a key function to determine how elements should be sorted.

Example:

```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78)
]


result = sorted(
    students,
    key=lambda student: student[1]
)

print(result)
```

Output:

```text
[('Charlie', 78), ('Alice', 85), ('Bob', 92)]
```

The lambda function extracts each student's marks for sorting.

### 4.4 reduce()

`reduce()` repeatedly combines elements using a supplied function until one result remains.

It is available in the `functools` module.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(
    lambda accumulated, current: accumulated + current,
    numbers
)

print(result)
```

Output:

```text
15
```

The function supplied to `reduce()` determines how the elements are combined.

---

## 5. Returning Functions from Functions

A function can create and return another function.

This is particularly useful when you want to configure behaviour.

Example:

```python
def create_multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
```

Output:

```text
20
30
```

Explanation:

- `create_multiplier()` accepts a configuration value.
- It defines a nested function.
- It returns that function.
- The returned function retains access to `factor`.

This is also an example of a closure.

The returned function remembers the enclosing variable even after `create_multiplier()` finishes executing.

---

## 6. Function Composition

Function composition means combining functions so that the output of one function becomes the input of another.

Example:

```python
def add_ten(number):
    return number + 10


def multiply_by_two(number):
    return number * 2


def compose(function_one, function_two):
    return lambda value: function_two(function_one(value))


operation = compose(add_ten, multiply_by_two)

print(operation(5))
```

Output:

```text
30
```

Execution:

1. Input is `5`.
2. `add_ten(5)` returns `15`.
3. `multiply_by_two(15)` returns `30`.

Function composition allows smaller functions to be combined into larger operations.

---

## 7. Callbacks

A callback is a function passed to another function so that it can be executed at an appropriate point.

Example:

```python
def on_success():
    print("Operation completed successfully")


def process_data(callback):
    print("Processing data...")

    callback()


process_data(on_success)
```

Output:

```text
Processing data...
Operation completed successfully
```

The `on_success` function is passed as a callback.

### Practical applications

Callbacks are commonly used in:

- Event handling.
- Asynchronous programming.
- API processing.
- Background tasks.
- Notification systems.
- Frameworks and libraries.

---

## 8. Higher-Order Functions in Backend Development

Higher-order functions allow reusable behaviour to be passed into other functions.

Example: validating data using a supplied validation function.

```python
def is_valid_email(email):
    return "@" in email


def validate_input(value, validation_function):
    if validation_function(value):
        return "Valid input"

    return "Invalid input"


print(validate_input("user@example.com", is_valid_email))
print(validate_input("invalid-email", is_valid_email))
```

Output:

```text
Valid input
Invalid input
```

The validation logic is separate from the function that executes it.

This separation improves reusability.

---

## 9. Higher-Order Functions in Agentic AI

Higher-order functions are useful in AI applications because they allow behaviour to be passed, selected and executed dynamically.

### 9.1 Tool execution

An agent can select a tool function and pass it to a common executor.

```python
def search_tool(query):
    return f"Searching for: {query}"


def calculator_tool(expression):
    return f"Calculating: {expression}"


def execute_tool(tool_function, argument):
    return tool_function(argument)


result = execute_tool(search_tool, "Python closures")

print(result)
```

Output:

```text
Searching for: Python closures
```

The executor does not need to know the internal implementation of every tool.

### 9.2 Filtering retrieved documents

```python
documents = [
    {"content": "Python basics", "score": 0.95},
    {"content": "Java basics", "score": 0.45},
    {"content": "Python advanced", "score": 0.88}
]


def is_relevant(document):
    return document["score"] >= 0.8


relevant_documents = list(
    filter(is_relevant, documents)
)

print(relevant_documents)
```

Output:

```text
[
    {'content': 'Python basics', 'score': 0.95},
    {'content': 'Python advanced', 'score': 0.88}
]
```

The filtering function can be changed without changing the filtering mechanism.

### 9.3 Processing model outputs

```python
def uppercase(text):
    return text.upper()


def remove_spaces(text):
    return text.strip()


def process_output(text, transformation):
    return transformation(text)


print(process_output(" hello ", uppercase))
print(process_output(" hello ", remove_spaces))
```

Output:

```text
 HELLO 
hello
```

Different transformations can be supplied to the same processing function.

---

## 10. Limitations of Higher-Order Functions

### 10.1 Can make code harder to understand

Passing functions into other functions and returning functions can make execution flow harder to follow.

Use descriptive function names and avoid unnecessary nesting.

### 10.2 Debugging can become difficult

The actual behaviour may depend on which function was passed at runtime.

This can make it harder to identify where unexpected behaviour originates.

### 10.3 Excessive abstraction

Not every operation needs to be converted into a higher-order function.

For a simple calculation, a normal function call may be clearer.

### 10.4 Type complexity

When functions accept other functions, type annotations can become more complex.

Python provides `Callable` from the `typing` module to describe callable arguments.

Example:

```python
from collections.abc import Callable


def execute(
    operation: Callable[[int], int],
    number: int
) -> int:
    return operation(number)


def square(number: int) -> int:
    return number ** 2


print(execute(square, 5))
```

Output:

```text
25
```

Here, `Callable[[int], int]` describes a function that accepts an integer and returns an integer.

---

## 11. Higher-Order Functions vs First-Class Functions

These concepts are related but not identical.

| Concept | Meaning |
|---|---|
| First-class functions | Functions can be treated as ordinary objects. |
| Higher-order functions | Functions accept other functions or return functions. |
| Callback | A function passed to another function for execution. |
| Closure | A function that retains access to enclosing variables. |
| Decorator | A function that takes another function and extends or modifies its behaviour. |

First-class functions are a capability of the language.

Higher-order functions are a programming technique that uses that capability.

---

## 12. Interview Questions

1. What is a higher-order function?
2. What are first-class functions in Python?
3. What is the difference between first-class and higher-order functions?
4. Can you pass a function as an argument?
5. Can a function return another function?
6. Explain how `map()` works.
7. Explain how `filter()` works.
8. What is the purpose of `reduce()`?
9. What is a callback function?
10. What is function composition?
11. How are closures related to higher-order functions?
12. How are higher-order functions useful in Agentic AI?

---

## 13. Knowledge Checklist

- [ ] Understand first-class functions.
- [ ] Assign functions to variables.
- [ ] Pass functions as arguments.
- [ ] Return functions from other functions.
- [ ] Understand higher-order functions.
- [ ] Use `map()`.
- [ ] Use `filter()`.
- [ ] Use `sorted()` with a key function.
- [ ] Use `reduce()`.
- [ ] Understand function composition.
- [ ] Understand callbacks.
- [ ] Explain how closures relate to higher-order functions.
- [ ] Understand how higher-order functions can support AI tool execution.

**Final takeaway:** A higher-order function accepts another function or returns a function. This allows behaviour to be passed around, selected dynamically and reused without hardcoding every operation into one function.
