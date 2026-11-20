# Closures in Python

## 1. What Is a Closure?

A closure is a function that remembers and retains access to variables from its enclosing scope, even after the outer function has finished executing.

A closure is created when:

1. A function is defined inside another function.
2. The inner function references a variable from the outer function.
3. The outer function returns the inner function or otherwise allows it to outlive the outer function call.

### Example

```python
def outer_function():
    message = "Hello from the outer function"

    def inner_function():
        print(message)

    return inner_function


my_function = outer_function()
my_function()
```

Output:

```text
Hello from the outer function
```

The outer function has finished executing, but `inner_function` can still access `message`.

This happens because the returned inner function retains access to the variable from its enclosing scope.

---

## 2. Understanding Scope Before Closures

To understand closures, you must understand Python's variable scope.

Scope defines where a variable can be accessed.

Python follows the LEGB rule when resolving variable names:

| Scope | Meaning |
|---|---|
| Local | Variables defined inside the current function |
| Enclosing | Variables in the enclosing function |
| Global | Variables defined at module level |
| Built-in | Names provided by Python, such as `print()` and `len()` |

### Example

```python
message = "Global message"


def outer():
    message = "Enclosing message"

    def inner():
        message = "Local message"
        print(message)

    inner()


outer()
```

Output:

```text
Local message
```

Python finds the variable in the local scope first.

If a variable is not found locally, Python searches the enclosing, global, and built-in scopes.

---

## 3. How a Closure Retains Variables

Consider this example:

```python
def create_greeting():
    message = "Welcome to Python"

    def greet():
        print(message)

    return greet


greeting = create_greeting()

greeting()
greeting()
```

Output:

```text
Welcome to Python
Welcome to Python
```

Step-by-step execution:

1. `create_greeting()` is called.
2. Python creates the local variable `message`.
3. The nested function `greet()` is defined.
4. `create_greeting()` returns the `greet` function.
5. The returned function is assigned to `greeting`.
6. The outer function call has finished.
7. `greeting()` still accesses `message`.

The inner function retains access to the enclosing variable through a closure.

It is not storing a previously printed result. It retains access to the variable itself.

---

## 4. Inspecting a Closure

Python allows you to inspect the variables retained by a closure through the function's `__closure__` attribute.

```python
def create_message():
    message = "Hello"

    def display():
        print(message)

    return display


function = create_message()

print(function.__closure__)
print(function.__closure__[0].cell_contents)
```

The `__closure__` attribute contains closure cells for variables captured from enclosing scopes.

`cell_contents` allows you to inspect the value held by a closure cell.

This is useful for understanding how closures work internally.

---

## 5. Modifying Enclosing Variables with `nonlocal`

An inner function can read a variable from its enclosing function.

However, assigning to that variable inside the inner function requires `nonlocal`.

### Example without `nonlocal`

```python
def outer():
    count = 10

    def inner():
        count = 20

    inner()
    print(count)


outer()
```

Output:

```text
10
```

The assignment creates a local variable called `count` inside `inner()`. It does not modify the enclosing variable.

### Example with `nonlocal`

```python
def outer():
    count = 10

    def inner():
        nonlocal count
        count = 20

    inner()
    print(count)


outer()
```

Output:

```text
20
```

The `nonlocal` keyword tells Python to use the nearest enclosing function's variable.

---

## 6. Creating a Counter with Closures

Closures are useful when you want to maintain state without using a class.

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print(counter())
print(counter())
print(counter())
```

Output:

```text
1
2
3
```

The variable `count` remains available to the returned function.

Each call to `increment()` modifies the same retained variable.

### Independent counters

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter_one = create_counter()
counter_two = create_counter()

print(counter_one())
print(counter_one())

print(counter_two())
print(counter_two())
```

Output:

```text
1
2
1
2
```

Each call to `create_counter()` creates a separate enclosing scope and an independent closure.

---

## 7. Closures with Parameters

An outer function can accept parameters that the inner function retains.

```python
def create_multiplier(multiplier):

    def multiply(number):
        return number * multiplier

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

The `double` function retains access to `multiplier = 2`.

The `triple` function retains access to `multiplier = 3`.

This allows you to create customised functions dynamically.

---

## 8. Closures vs Global Variables

Global variables are accessible throughout a module.

Closures allow state to remain associated with a particular returned function.

### Global variable

```python
count = 0


def increment():
    global count
    count += 1
    return count


print(increment())
print(increment())
```

### Closure

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print(counter())
print(counter())
```

| Feature | Global variable | Closure |
|---|---|---|
| Scope | Module level | Enclosing function |
| State | Shared through the module | Associated with a particular closure |
| Modification | Uses `global` | Uses `nonlocal` |
| Isolation | Can be shared by unrelated functions | Separate closure instances can maintain independent state |

Closures are often preferable when state should be private to a particular function.

---

## 9. Closures vs Classes

Closures can maintain state without creating a class.

However, classes are more suitable when an object needs several related methods, attributes, or more complex behaviour.

### Closure implementation

```python
def create_bank_account(initial_balance):

    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    return deposit


deposit_money = create_bank_account(100)

print(deposit_money(50))
print(deposit_money(25))
```

### Class implementation

```python
class BankAccount:

    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


account = BankAccount(100)

print(account.deposit(50))
print(account.deposit(25))
```

Both examples maintain state.

The class provides a clearer structure when multiple operations are required, such as deposit, withdraw, and check balance.

---

## 10. Closures in Decorators

Decorators commonly use closures.

A decorator is a function that takes another function, wraps it with additional behaviour, and returns a new function.

Example:

```python
def my_decorator(function):

    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@my_decorator
def greet():
    print("Hello")


greet()
```

Output:

```text
Before function execution
Hello
After function execution
```

The `wrapper` function retains access to the `function` variable from the enclosing `my_decorator` scope.

This is one of the most common practical uses of closures.

---

## 11. Closures in Software and AI Applications

Closures can be useful in several software engineering situations.

### 11.1 Configuration-Based Functions

Create functions that retain configuration values.

```python
def create_model_predictor(threshold):

    def predict(confidence):
        return confidence >= threshold

    return predict


strict_predictor = create_model_predictor(0.90)
normal_predictor = create_model_predictor(0.70)

print(strict_predictor(0.85))
print(normal_predictor(0.85))
```

The returned functions retain their respective confidence thresholds.

### 11.2 API Request Configuration

A closure can retain configuration for repeated API operations.

```python
def create_request_handler(base_url):

    def build_url(endpoint):
        return f"{base_url}/{endpoint}"

    return build_url


api_handler = create_request_handler(
    "https://api.example.com"
)

print(api_handler("users"))
print(api_handler("products"))
```

### 11.3 Agent Tool Configuration

A closure can create a tool function with a predefined configuration.

```python
def create_search_tool(search_limit):

    def search(query):
        return {
            "query": query,
            "limit": search_limit
        }

    return search


limited_search = create_search_tool(5)

print(limited_search("Python closures"))
```

The returned function retains the configured search limit.

This is a simple illustration of function configuration, not a complete agent tool implementation.

---

## 12. Memory and Lifetime of Closures

A closure can keep an enclosing variable alive after the outer function has returned.

The variable remains available while it is still referenced by the closure.

```python
def create_storage():

    data = []

    def add_item(item):
        data.append(item)
        return data

    return add_item


storage = create_storage()

print(storage("Python"))
print(storage("FastAPI"))
print(storage("Agentic AI"))
```

Output:

```text
['Python']
['Python', 'FastAPI']
['Python', 'FastAPI', 'Agentic AI']
```

The closure retains access to the same list.

When the closure and all other references to the retained object are no longer reachable, Python can reclaim the memory through its memory-management mechanisms.

---

## 13. Common Mistakes with Closures

### Mistake 1: Forgetting `nonlocal`

```python
def create_counter():
    count = 0

    def increment():
        count += 1
        return count

    return increment
```

This raises `UnboundLocalError` because the assignment makes `count` local to `increment()`.

Correct:

```python
def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment
```

### Mistake 2: Returning the Function's Result Instead of the Function

Incorrect:

```python
def outer():
    def inner():
        return "Hello"

    return inner()
```

This returns the string `"Hello"`.

Correct:

```python
def outer():
    def inner():
        return "Hello"

    return inner
```

This returns the function itself.

### Mistake 3: Confusing Closure with a Normal Nested Function

Not every nested function is a closure.

A nested function becomes a closure when it retains access to variables from its enclosing scope.

---

## 14. Key Concepts to Remember

| Concept | Meaning |
|---|---|
| Closure | Function retaining access to enclosing variables |
| Enclosing scope | Scope of the outer function |
| `nonlocal` | Allows assignment to an enclosing function variable |
| `global` | Allows assignment to a module-level variable |
| `__closure__` | Attribute exposing closure cells |
| `cell_contents` | Value stored in a closure cell |
| State | Data retained between function calls |
| Decorator | Function that wraps another function |

---

## 15. Practice Tasks

Complete these exercises independently.

1. Create a closure that returns a greeting using a name supplied to the outer function.
2. Create a counter using `nonlocal`.
3. Create two independent counters and demonstrate that their states do not interfere.
4. Create a multiplier closure that returns double, triple, or another multiplication operation.
5. Create a closure that retains a discount percentage and calculates discounted prices.
6. Create a closure that retains a confidence threshold and classifies model predictions.
7. Create a closure that stores items in a private list.
8. Create a closure-based API URL builder.
9. Inspect a closure using `__closure__` and `cell_contents`.
10. Explain the difference between a closure, a nested function, and a global variable.

**Completion requirement:** You must be able to explain why an inner function can still access an enclosing variable after the outer function has finished, and when `nonlocal` is required.