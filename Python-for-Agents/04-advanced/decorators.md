# Decorators in Python

## 1. What Is a Decorator?

A decorator is a function that takes another function as an argument, adds or modifies its behaviour, and returns a function.

Decorators allow you to extend the behaviour of existing functions without changing their original implementation.

They are commonly used for:

- Logging
- Authentication and authorisation
- Execution time measurement
- Input validation
- Caching
- API endpoint configuration
- Retry mechanisms

### Basic example

```python
def my_decorator(function):

    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


def greet():
    print("Hello, Python")


decorated_function = my_decorator(greet)

decorated_function()
```

Output:

```text
Before function execution
Hello, Python
After function execution
```

The decorator receives `greet` as an argument.

It defines a new function called `wrapper`, which executes additional instructions before and after calling `greet`.

Finally, it returns `wrapper`.

---

## 2. Understanding the Three Main Components

A basic decorator contains three important parts.

### 2.1 Original function

This is the function whose behaviour you want to extend.

```python
def greet():
    print("Hello")
```

### 2.2 Wrapper function

The wrapper controls when and how the original function executes.

```python
def wrapper():
    print("Before execution")
    greet()
    print("After execution")
```

In a reusable decorator, the original function is passed into the decorator rather than hardcoded into the wrapper.

### 2.3 Returning the wrapper

The decorator returns the wrapper function.

```python
return wrapper
```

The wrapper is returned without parentheses because you are returning the function itself, not executing it immediately.

---

## 3. Using the `@` Decorator Syntax

Python provides the `@` syntax to apply decorators.

Consider the previous example:

```python
def my_decorator(function):

    def wrapper():
        print("Before function execution")
        function()
        print("After function execution")

    return wrapper


@my_decorator
def greet():
    print("Hello, Python")


greet()
```

The following syntax:

```python
@my_decorator
def greet():
    print("Hello, Python")
```

is equivalent to:

```python
def greet():
    print("Hello, Python")


greet = my_decorator(greet)
```

Python passes the original function to the decorator and assigns the returned wrapper to the function name.

When you call `greet()`, you are executing the wrapper.

---

## 4. Decorators with Function Arguments

The previous wrapper works only for functions without arguments.

To create a reusable decorator, the wrapper must accept arbitrary positional and keyword arguments.

Python provides:

- `*args` for collecting positional arguments.
- `**kwargs` for collecting keyword arguments.

### Example

```python
def my_decorator(function):

    def wrapper(*args, **kwargs):
        print("Before execution")

        result = function(*args, **kwargs)

        print("After execution")

        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Before execution
After execution
30
```

The wrapper forwards all arguments to the original function.

It also returns the original function's result.

**Important:** Always preserve the return value when writing a general-purpose decorator. Otherwise, the decorated function may unexpectedly return `None`.

---

## 5. Understanding `*args` and `**kwargs` in Decorators

A decorator should not need to know the exact parameters of every function it decorates.

For example:

```python
def logger(function):

    def wrapper(*args, **kwargs):
        print(f"Executing: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Completed: {function.__name__}")

        return result

    return wrapper


@logger
def greet(name):
    return f"Hello, {name}"


@logger
def multiply(a, b):
    return a * b


print(greet("Alex"))
print(multiply(5, 4))
```

The same decorator works with functions that have different signatures.

This makes decorators reusable.

---

## 6. Preserving Function Metadata with `functools.wraps`

When a decorator returns a wrapper, the decorated function's metadata can be replaced by the wrapper's metadata.

For example:

```python
def my_decorator(function):

    def wrapper():
        return function()

    return wrapper


@my_decorator
def greet():
    """Displays a greeting."""

    return "Hello"


print(greet.__name__)
print(greet.__doc__)
```

Without metadata preservation, the output identifies the function as `wrapper` rather than `greet`.

Python provides `functools.wraps` to preserve important metadata.

### Correct implementation

```python
from functools import wraps


def my_decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """Displays a greeting."""

    return "Hello"


print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Displays a greeting.
```

**Best practice:** Use `@wraps(function)` inside reusable decorators.

---

## 7. Decorators with Their Own Arguments

Sometimes you need to configure the decorator itself.

For example, you may want a decorator to repeat a function a specified number of times.

This requires an additional outer function.

### Example

```python
from functools import wraps


def repeat(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def greet():
    print("Hello")


greet()
```

Output:

```text
Hello
Hello
Hello
```

There are three function levels:

1. `repeat(times)` receives the decorator configuration.
2. `decorator(function)` receives the original function.
3. `wrapper(*args, **kwargs)` executes the original function.

This structure is known as a decorator factory.

---

## 8. Understanding Decorator Execution Order

Decorators can be stacked on the same function.

Example:

```python
def decorator_one(function):

    def wrapper():
        print("Decorator One - Before")
        function()
        print("Decorator One - After")

    return wrapper


def decorator_two(function):

    def wrapper():
        print("Decorator Two - Before")
        function()
        print("Decorator Two - After")

    return wrapper


@decorator_one
@decorator_two
def greet():
    print("Hello")


greet()
```

Output:

```text
Decorator One - Before
Decorator Two - Before
Hello
Decorator Two - After
Decorator One - After
```

The decorators are applied from the bottom upwards.

The equivalent assignment is:

```python
greet = decorator_one(decorator_two(greet))
```

However, execution enters the outer wrapper first and then moves into the inner wrapper.

Understanding this order is important when combining authentication, logging, caching, and validation decorators.

---

## 9. Logging Decorator

Logging decorators record information about function execution.

They are useful for debugging and monitoring applications.

```python
from functools import wraps


def log_execution(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Calling {function.__name__}")

        result = function(*args, **kwargs)

        print(f"{function.__name__} completed")

        return result

    return wrapper


@log_execution
def process_data(data):
    return data.upper()


print(process_data("python"))
```

Output:

```text
Calling process_data
process_data completed
PYTHON
```

In production systems, use Python's `logging` module instead of relying on `print()` statements.

---

## 10. Execution Time Decorator

A decorator can measure how long a function takes to execute.

Python provides `time.perf_counter()` for measuring elapsed time.

```python
import time
from functools import wraps


def measure_time(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        start = time.perf_counter()

        result = function(*args, **kwargs)

        end = time.perf_counter()

        print(
            f"{function.__name__} took "
            f"{end - start:.6f} seconds"
        )

        return result

    return wrapper


@measure_time
def calculate_sum():
    return sum(range(1_000_000))


print(calculate_sum())
```

This decorator measures the execution time of the wrapped function.

It is useful for performance analysis, but one measurement is not enough for a reliable benchmark.

---

## 11. Authentication Decorator

Authentication decorators can check whether a user is authenticated before allowing a function to execute.

```python
from functools import wraps


def require_authentication(function):

    @wraps(function)
    def wrapper(user, *args, **kwargs):

        if not user.get("authenticated"):
            return "Access denied"

        return function(user, *args, **kwargs)

    return wrapper


@require_authentication
def view_dashboard(user):
    return f"Welcome, {user['name']}"


authenticated_user = {
    "name": "Alex",
    "authenticated": True
}

guest_user = {
    "name": "Guest",
    "authenticated": False
}


print(view_dashboard(authenticated_user))
print(view_dashboard(guest_user))
```

Output:

```text
Welcome, Alex
Access denied
```

This is an educational example. Real authentication must verify identity securely, and access control must be enforced on the server side.

---

## 12. Validation Decorator

Decorators can validate inputs before a function executes.

```python
from functools import wraps


def validate_positive(function):

    @wraps(function)
    def wrapper(number):

        if number <= 0:
            raise ValueError("Number must be positive")

        return function(number)

    return wrapper


@validate_positive
def calculate_square(number):
    return number ** 2


print(calculate_square(5))

# Raises ValueError:
# print(calculate_square(-5))
```

The decorator validates the input before calling the original function.

This is useful when the same validation rule applies to several functions.

For more complex applications, use validation libraries or explicit validation layers where appropriate.

---

## 13. Caching Decorator

Caching stores the result of a function so repeated calls with the same arguments can reuse previous results.

Python provides `functools.lru_cache` and `functools.cache`.

Example:

```python
from functools import lru_cache


@lru_cache(maxsize=128)
def expensive_calculation(number):
    print("Calculating...")

    return number * number


print(expensive_calculation(10))
print(expensive_calculation(10))
print(expensive_calculation(20))

print(expensive_calculation.cache_info())
```

The second call with `10` can reuse the cached result.

Caching is useful when:

- A calculation is expensive.
- The same inputs occur repeatedly.
- The function's result is safe to reuse.

Be careful with caching functions that depend on changing external state, current time, database contents, or user-specific permissions.

---

## 14. Decorators in FastAPI

FastAPI uses decorators to define API routes.

Example:

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}


@app.get("/users")
def get_users():
    return {"users": ["Alex", "Sam"]}
```

The decorators:

```python
@app.get("/")
@app.get("/users")
```

register the functions as HTTP endpoint handlers.

FastAPI uses this information to build its routing system and generate API documentation.

You will encounter decorators frequently when building backend applications.

---

## 15. Decorators in Agentic AI Applications

Decorators can help implement reusable behaviour around AI-related functions.

Examples include:

- Logging tool execution.
- Measuring LLM request duration.
- Validating tool inputs.
- Restricting access to tools.
- Retrying failed operations.
- Recording execution metadata.

### Example: Logging an AI tool call

```python
from functools import wraps


def tool_logger(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Tool started: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Tool finished: {function.__name__}")

        return result

    return wrapper


@tool_logger
def search_documents(query):
    return f"Searching documents for: {query}"


print(search_documents("Python decorators"))
```

This demonstrates how a decorator can add execution logging without modifying the tool's original implementation.

It is not a complete production tool-execution framework.

---

## 16. Error Handling in Decorators

A decorator can handle exceptions raised by the wrapped function.

```python
from functools import wraps


def handle_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)

        except ValueError as error:
            print(f"Validation error: {error}")
            return None

        except Exception as error:
            print(f"Unexpected error: {error}")
            raise

    return wrapper


@handle_errors
def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


print(divide(10, 2))
print(divide(10, 0))
```

The decorator handles the expected `ValueError` and re-raises unexpected exceptions.

**Important:** Do not silently swallow all exceptions. Error handling should preserve useful failure information.

---

## 17. Common Mistakes

### Mistake 1: Forgetting to return the wrapper

Incorrect:

```python
def decorator(function):

    def wrapper():
        function()

    wrapper()
```

This executes the wrapper immediately instead of returning it.

Correct:

```python
def decorator(function):

    def wrapper():
        function()

    return wrapper
```

### Mistake 2: Forgetting `*args` and `**kwargs`

A wrapper that accepts no arguments cannot decorate arbitrary functions.

Correct:

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

### Mistake 3: Forgetting the original return value

Incorrect:

```python
def wrapper(*args, **kwargs):
    function(*args, **kwargs)
```

Correct:

```python
def wrapper(*args, **kwargs):
    return function(*args, **kwargs)
```

### Mistake 4: Not using `functools.wraps`

Without `@wraps`, the wrapper can replace the original function's name, documentation, and other metadata.

### Mistake 5: Confusing decorator arguments with function arguments

In:

```python
@repeat(3)
def greet():
    pass
```

`3` configures the decorator. It is not an argument passed to `greet()`.

---

## 18. Decorators vs Closures vs Higher-Order Functions

These concepts are related but not identical.

| Concept | Meaning |
|---|---|
| Higher-order function | Accepts a function or returns a function |
| Closure | Function retaining access to enclosing variables |
| Decorator | Higher-order function that extends another function's behaviour |
| Wrapper | Function that calls or surrounds another function |
| Decorator factory | Function that creates a configured decorator |

A typical decorator uses both higher-order functions and closures.

---

## 19. Key Concepts to Remember

| Concept | Meaning |
|---|---|
| Decorator | Adds behaviour to an existing function |
| `@` syntax | Applies a decorator to a function |
| Wrapper | Function that surrounds the original function |
| `*args` | Collects positional arguments |
| `**kwargs` | Collects keyword arguments |
| `functools.wraps` | Preserves function metadata |
| Decorator factory | Creates decorators with configuration |
| Stacked decorators | Multiple decorators applied to one function |
| `lru_cache` | Provides least-recently-used caching |
| `perf_counter()` | Measures elapsed time |

---

## 20. Practice Tasks

Complete these exercises independently.

1. Create a decorator that prints a message before and after a function executes.
2. Create a decorator that supports functions with positional and keyword arguments.
3. Create a decorator that logs the function name and arguments.
4. Create a decorator that measures execution time.
5. Create a decorator that validates positive numbers.
6. Create a decorator that checks whether a user is authenticated.
7. Create a decorator factory that repeats a function a configurable number of times.
8. Stack two decorators and explain their execution order.
9. Use `functools.wraps` and inspect the decorated function's name and documentation.
10. Create a decorator that logs the execution of a simulated AI tool.

**Completion requirement:** You must be able to write a reusable decorator from scratch, explain how `@` syntax works, preserve arguments and return values, and use `functools.wraps` correctly.