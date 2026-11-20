# Advanced Function Arguments in Python

## 1. Introduction

Python functions support different ways of receiving arguments.

Understanding advanced function arguments is important when building reusable functions, decorators, APIs, libraries, and AI applications.

The main concepts covered in this topic are:

1. Positional arguments
2. Keyword arguments
3. Default arguments
4. `*args`
5. `**kwargs`
6. Keyword-only arguments
7. Positional-only arguments
8. Argument unpacking
9. Combining different argument types
10. Type hints and function signatures

---

## 2. Positional Arguments

Positional arguments are passed to a function according to the order of its parameters.

```python
def introduce(name, age, city):
    print(f"My name is {name}")
    print(f"My age is {age}")
    print(f"I live in {city}")


introduce("Alex", 25, "London")
```

Output:

```text
My name is Alex
My age is 25
I live in London
```

Python assigns the first argument to the first parameter, the second argument to the second parameter, and so on.

**Important:** The order matters.

```python
introduce("London", 25, "Alex")
```

This executes without an error, but the values are assigned to the wrong parameters.

---

## 3. Keyword Arguments

Keyword arguments are passed using parameter names.

```python
def introduce(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")


introduce(
    name="Alex",
    age=25,
    city="London"
)
```

Output:

```text
Alex is 25 years old and lives in London
```

Keyword arguments make function calls easier to understand.

### Changing the order

Unlike positional arguments, keyword arguments do not depend on the order in which they are supplied.

```python
introduce(
    city="London",
    name="Alex",
    age=25
)
```

This produces the same result.

### Mixing positional and keyword arguments

You can combine both types.

```python
def calculate_total(price, quantity, discount):
    return price * quantity - discount


result = calculate_total(
    100,
    quantity=2,
    discount=10
)

print(result)
```

Output:

```text
190
```

**Rule:** Positional arguments must appear before keyword arguments in a function call.

Incorrect:

```python
calculate_total(price=100, 2, discount=10)
```

---

## 4. Default Arguments

Default arguments allow parameters to have predefined values.

If the caller does not provide a value, Python uses the default.

```python
def greet(name, message="Welcome"):
    print(f"{message}, {name}")


greet("Alex")
greet("Sam", "Good morning")
```

Output:

```text
Welcome, Alex
Good morning, Sam
```

Default arguments make parameters optional.

### Important: Mutable Default Arguments

Avoid using mutable objects such as lists or dictionaries as default parameter values.

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items


print(add_item("Python"))
print(add_item("FastAPI"))
```

The same list is reused across function calls.

Output:

```text
['Python']
['Python', 'FastAPI']
```

This happens because Python evaluates default argument expressions when the function is defined, not every time the function is called.

### Correct approach

Use `None` as the default and create a new list inside the function.

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items


print(add_item("Python"))
print(add_item("FastAPI"))
```

Output:

```text
['Python']
['FastAPI']
```

This prevents accidental sharing of mutable default state.

---

## 5. Variable-Length Positional Arguments: `*args`

Sometimes you do not know how many positional arguments a function will receive.

Python provides `*args` for this purpose.

```python
def calculate_sum(*args):
    return sum(args)


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30))
print(calculate_sum(1, 2, 3, 4, 5))
```

Output:

```text
30
60
15
```

### How `*args` works

```python
def example(*args):
    print(args)


example(10, 20, 30)
```

Output:

```text
(10, 20, 30)
```

`args` receives the extra positional arguments as a tuple.

The asterisk is what enables Python to collect those arguments.

The name `args` is a convention. You could use another name, although `args` is standard.

### Using `*args` with normal parameters

```python
def calculate_total(currency, *prices):
    total = sum(prices)

    return f"{currency}{total}"


print(calculate_total("£", 10, 20, 30))
```

Output:

```text
£60
```

The first positional argument is assigned to `currency`. The remaining positional arguments are collected in `prices`.

---

## 6. Variable-Length Keyword Arguments: `**kwargs`

Sometimes a function needs to accept an unknown number of keyword arguments.

Python provides `**kwargs`.

```python
def display_details(**kwargs):
    print(kwargs)


display_details(
    name="Alex",
    age=25,
    city="London"
)
```

Output:

```text
{'name': 'Alex', 'age': 25, 'city': 'London'}
```

`kwargs` receives the extra keyword arguments as a dictionary.

### Iterating through `**kwargs`

```python
def display_details(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_details(
    name="Alex",
    role="Developer",
    experience=2
)
```

Output:

```text
name: Alex
role: Developer
experience: 2
```

### Using normal parameters with `**kwargs`

```python
def create_user(name, **details):

    print(f"Name: {name}")

    for key, value in details.items():
        print(f"{key}: {value}")


create_user(
    "Alex",
    age=25,
    city="London",
    role="Developer"
)
```

The `name` parameter receives its value directly. Other keyword arguments are collected in `details`.

---

## 7. Understanding `*args` vs `**kwargs`

| Feature | `*args` | `**kwargs` |
|---|---|---|
| Purpose | Collect extra positional arguments | Collect extra keyword arguments |
| Data structure | Tuple | Dictionary |
| Argument format | `10, 20, 30` | `name="Alex"` |
| Access | By index or iteration | By key or iteration |
| Typical use | Variable numbers of values | Flexible configuration |

Example using both:

```python
def process_data(*args, **kwargs):

    print("Positional:", args)
    print("Keyword:", kwargs)


process_data(
    10,
    20,
    30,
    name="Alex",
    role="Developer"
)
```

Output:

```text
Positional: (10, 20, 30)
Keyword: {'name': 'Alex', 'role': 'Developer'}
```

---

## 8. Keyword-Only Arguments

Keyword-only arguments must be supplied using their parameter names.

Python uses `*` in the function definition to establish the keyword-only boundary.

```python
def create_account(name, *, email, password):
    print(name)
    print(email)
    print(password)


create_account(
    "Alex",
    email="alex@example.com",
    password="secret"
)
```

The following call is invalid:

```python
create_account(
    "Alex",
    "alex@example.com",
    "secret"
)
```

The parameters after `*` must be supplied by keyword.

### Why use keyword-only arguments?

They make important parameters explicit.

For example:

```python
def search_documents(query, *, limit=5, threshold=0.80):
    print(query)
    print(limit)
    print(threshold)


search_documents(
    "Python functions",
    limit=10,
    threshold=0.90
)
```

This makes the function call easier to read and reduces mistakes when several optional parameters exist.

---

## 9. Positional-Only Arguments

Positional-only arguments must be supplied according to their position.

Python uses `/` in the function definition to establish the positional-only boundary.

```python
def divide(a, b, /):
    return a / b


print(divide(10, 2))
```

The following call is invalid:

```python
divide(a=10, b=2)
```

Both arguments must be supplied positionally.

### Combining positional-only and keyword-only arguments

```python
def calculate(a, b, /, *, operation):
    if operation == "add":
        return a + b

    if operation == "multiply":
        return a * b

    raise ValueError("Unsupported operation")


print(calculate(10, 5, operation="add"))
print(calculate(10, 5, operation="multiply"))
```

Here:

- `a` and `b` are positional-only.
- `operation` is keyword-only.

---

## 10. Argument Unpacking

Argument unpacking allows you to pass values from an existing collection into a function.

### 10.1 Unpacking a List or Tuple with `*`

```python
def add(a, b, c):
    return a + b + c


numbers = [10, 20, 30]

print(add(*numbers))
```

Output:

```text
60
```

The `*` operator unpacks the list into individual positional arguments.

Equivalent call:

```python
add(10, 20, 30)
```

### 10.2 Unpacking a Dictionary with `**`

```python
def introduce(name, age, city):
    return f"{name}, {age}, {city}"


details = {
    "name": "Alex",
    "age": 25,
    "city": "London"
}

print(introduce(**details))
```

The `**` operator unpacks dictionary entries into keyword arguments.

Equivalent call:

```python
introduce(
    name="Alex",
    age=25,
    city="London"
)
```

---

## 11. Combining All Argument Types

Python supports a specific order for parameters in a function definition.

The general order is:

1. Positional-only parameters
2. Standard positional-or-keyword parameters
3. `*args`
4. Keyword-only parameters
5. `**kwargs`

Example:

```python
def example(
    a,
    b,
    /,
    c,
    *args,
    d,
    e=10,
    **kwargs
):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("args:", args)
    print("d:", d)
    print("e:", e)
    print("kwargs:", kwargs)


example(
    1,
    2,
    3,
    4,
    5,
    d=6,
    e=7,
    name="Alex",
    city="London"
)
```

Output:

```text
a: 1
b: 2
c: 3
args: (4, 5)
d: 6
e: 7
kwargs: {'name': 'Alex', 'city': 'London'}
```

This combines all major parameter types in one function.

You will not need every type in every function. Use the simplest signature that satisfies the requirements.

---

## 12. Type Hints with Advanced Arguments

Type hints describe the expected types of function parameters and return values.

They improve readability and help static analysis tools identify potential mistakes.

### Example with `*args`

```python
def calculate_sum(*numbers: int) -> int:
    return sum(numbers)


print(calculate_sum(10, 20, 30))
```

### Example with `**kwargs`

```python
def display_user(**details: str) -> None:

    for key, value in details.items():
        print(key, value)


display_user(
    name="Alex",
    city="London"
)
```

### Example with Callable

```python
from collections.abc import Callable


def execute_operation(
    operation: Callable[[int, int], int],
    a: int,
    b: int
) -> int:
    return operation(a, b)


def add(a: int, b: int) -> int:
    return a + b


print(execute_operation(add, 10, 20))
```

Type hints do not automatically validate values at runtime. Use a validation mechanism when runtime validation is required.

---

## 13. Inspecting Function Signatures

Python provides `inspect.signature()` to examine a function's parameters.

```python
import inspect


def create_user(name, age=18, *, city):
    pass


signature = inspect.signature(create_user)

print(signature)
```

Output:

```text
(name, age=18, *, city)
```

You can inspect individual parameters:

```python
for parameter in signature.parameters.values():
    print(parameter.name, parameter.kind)
```

This is useful when developing:

- Frameworks
- Reusable libraries
- Dependency injection systems
- Function-based tools
- Dynamic function execution

---

## 14. Advanced Arguments in Decorators

Decorators frequently use `*args` and `**kwargs` because they need to support functions with different parameter signatures.

```python
from functools import wraps


def logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Executing: {function.__name__}")
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)

        result = function(*args, **kwargs)

        return result

    return wrapper


@logger
def create_user(name, age, city=None):
    return {
        "name": name,
        "age": age,
        "city": city
    }


print(
    create_user(
        "Alex",
        25,
        city="London"
    )
)
```

The wrapper accepts different combinations of positional and keyword arguments and forwards them to the original function.

This is one of the most important practical uses of advanced function arguments.

---

## 15. Advanced Arguments in Agentic AI

Agentic AI applications often need flexible function interfaces.

For example, a tool may accept a query and optional configuration parameters.

```python
def search_tool(
    query: str,
    *,
    limit: int = 5,
    category: str = "general"
):
    return {
        "query": query,
        "limit": limit,
        "category": category
    }


result = search_tool(
    "Python decorators",
    limit=10,
    category="programming"
)

print(result)
```

This interface makes the required query positional while ensuring that optional configuration is explicit.

### Dynamic tool execution

A function registry can store different tools.

```python
def calculator(expression):
    return f"Calculating: {expression}"


def search(query, limit=5):
    return {
        "query": query,
        "limit": limit
    }


tools = {
    "calculator": calculator,
    "search": search
}


selected_tool = tools["search"]

result = selected_tool(
    "Agentic AI",
    limit=10
)

print(result)
```

The selected function can be called with its supported arguments.

In a production agent, tool arguments should be validated against an explicit schema. Do not assume arbitrary `**kwargs` are safe or valid.

---

## 16. Common Mistakes

### Mistake 1: Positional arguments after keyword arguments

Incorrect:

```python
def calculate(a, b):
    return a + b


calculate(a=10, 20)
```

Correct:

```python
calculate(10, b=20)
```

### Mistake 2: Mutable default arguments

Incorrect:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Correct:

```python
def add_item(item, items=None):

    if items is None:
        items = []

    items.append(item)

    return items
```

### Mistake 3: Confusing `*args` and `**kwargs`

- `*args` collects positional arguments into a tuple.
- `**kwargs` collects keyword arguments into a dictionary.

### Mistake 4: Incorrect parameter order

Incorrect:

```python
def example(**kwargs, *args):
    pass
```

Correct:

```python
def example(*args, **kwargs):
    pass
```

### Mistake 5: Passing the wrong dictionary keys

When using `function(**dictionary)`, the dictionary keys must match the function's accepted parameter names unless the function accepts additional keyword arguments.

---

## 17. Key Concepts to Remember

| Concept | Meaning |
|---|---|
| Positional arguments | Values assigned according to parameter order |
| Keyword arguments | Values assigned using parameter names |
| Default arguments | Parameters with predefined values |
| `*args` | Collects extra positional arguments into a tuple |
| `**kwargs` | Collects extra keyword arguments into a dictionary |
| Keyword-only | Parameters that must be passed by name |
| Positional-only | Parameters that must be passed by position |
| `*` | Used for unpacking iterables and defining keyword-only boundaries |
| `**` | Used for dictionary unpacking and collecting keyword arguments |
| `inspect.signature()` | Inspects function parameters |

---

## 18. Practice Tasks

Complete these exercises independently.

1. Write a function that accepts three positional arguments and returns their sum.
2. Create a function with default arguments for name, age, and city.
3. Write a function that accepts any number of integers using `*args` and calculates their average.
4. Write a function that accepts any number of keyword arguments using `**kwargs` and displays them.
5. Create a function that combines normal parameters, `*args`, and `**kwargs`.
6. Write a function with keyword-only arguments for `limit` and `threshold`.
7. Write a function with positional-only arguments using `/`.
8. Unpack a list into positional arguments using `*`.
9. Unpack a dictionary into keyword arguments using `**`.
10. Create a flexible decorator using `*args` and `**kwargs`.
11. Use `inspect.signature()` to inspect a function with multiple parameter types.
12. Build a simulated AI search tool that accepts a required query and optional keyword-only configuration.

**Completion requirement:** You must be able to design function signatures deliberately, explain the difference between `*args` and `**kwargs`, unpack collections into function calls, and choose positional-only or keyword-only parameters when appropriate.