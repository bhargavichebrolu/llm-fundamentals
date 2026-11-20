
"""
DECORATORS IN PYTHON

Topics:
1. Basic decorators
2. @ decorator syntax
3. Decorators with arguments
4. *args and **kwargs
5. functools.wraps
6. Decorator factories
7. Stacked decorators
8. Logging
9. Execution time
10. Authentication
11. Validation
12. Caching
13. Error handling
14. AI tool decorators
15. Practice exercises
"""

from functools import wraps, lru_cache
import time


# ============================================================
# 1. BASIC DECORATOR
# ============================================================

def my_decorator(function):

    def wrapper():
        print("Before function execution")

        function()

        print("After function execution")

    return wrapper


@my_decorator
def greet():
    print("Hello, Python")


print("\n1. BASIC DECORATOR")
greet()


# ============================================================
# 2. DECORATOR WITHOUT @ SYNTAX
# ============================================================

def simple_decorator(function):

    def wrapper():
        print("Executing decorated function")
        function()

    return wrapper


def welcome():
    print("Welcome")


welcome = simple_decorator(welcome)

print("\n2. WITHOUT @ SYNTAX")
welcome()


# ============================================================
# 3. DECORATOR WITH *ARGS AND **KWARGS
# ============================================================

def flexible_decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Executing: {function.__name__}")

        result = function(*args, **kwargs)

        print("Execution completed")

        return result

    return wrapper


@flexible_decorator
def add(a, b):
    return a + b


@flexible_decorator
def introduce(name, city):
    return f"{name} lives in {city}"


print("\n3. ARGS AND KWARGS")
print(add(10, 20))
print(introduce(name="Alex", city="London"))


# ============================================================
# 4. PRESERVING FUNCTION METADATA
# ============================================================

def metadata_decorator(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)

    return wrapper


@metadata_decorator
def calculate_square(number):
    """Returns the square of a number."""
    return number ** 2


print("\n4. FUNCTION METADATA")
print(calculate_square(5))
print(calculate_square.__name__)
print(calculate_square.__doc__)


# ============================================================
# 5. DECORATOR FACTORY
# ============================================================

def repeat(times):

    def decorator(function):

        @wraps(function)
        def wrapper(*args, **kwargs):

            result = None

            for _ in range(times):
                result = function(*args, **kwargs)

            return result

        return wrapper

    return decorator


@repeat(3)
def say_hello():
    print("Hello")


print("\n5. DECORATOR FACTORY")
say_hello()


# ============================================================
# 6. STACKED DECORATORS
# ============================================================

def decorator_one(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Decorator one - Before")

        result = function(*args, **kwargs)

        print("Decorator one - After")

        return result

    return wrapper


def decorator_two(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        print("Decorator two - Before")

        result = function(*args, **kwargs)

        print("Decorator two - After")

        return result

    return wrapper


@decorator_one
@decorator_two
def execute():
    print("Original function")


print("\n6. STACKED DECORATORS")
execute()


# ============================================================
# 7. LOGGING DECORATOR
# ============================================================

def log_execution(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        print(f"Calling: {function.__name__}")

        result = function(*args, **kwargs)

        print(f"Completed: {function.__name__}")

        return result

    return wrapper


@log_execution
def process_data(data):
    return data.upper()


print("\n7. LOGGING")
print(process_data("python"))


# ============================================================
# 8. EXECUTION TIME DECORATOR
# ============================================================

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


print("\n8. EXECUTION TIME")
print(calculate_sum())


# ============================================================
# 9. AUTHENTICATION DECORATOR
# ============================================================

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


print("\n9. AUTHENTICATION")
print(view_dashboard(authenticated_user))
print(view_dashboard(guest_user))


# ============================================================
# 10. VALIDATION DECORATOR
# ============================================================

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


print("\n10. VALIDATION")
print(calculate_square(5))

# Uncomment to test the validation error:
# print(calculate_square(-5))


# ============================================================
# 11. CACHING DECORATOR
# ============================================================

@lru_cache(maxsize=128)
def expensive_calculation(number):

    print("Calculating...")

    return number * number


print("\n11. CACHING")

print(expensive_calculation(10))
print(expensive_calculation(10))
print(expensive_calculation(20))

print(expensive_calculation.cache_info())


# ============================================================
# 12. ERROR HANDLING DECORATOR
# ============================================================

def handle_errors(function):

    @wraps(function)
    def wrapper(*args, **kwargs):

        try:
            return function(*args, **kwargs)

        except ValueError as error:
            print(f"Validation error: {error}")
            return None

        except Exception:
            print("Unexpected error occurred")
            raise

    return wrapper


@handle_errors
def divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


print("\n12. ERROR HANDLING")
print(divide(10, 2))
print(divide(10, 0))


# ============================================================
# 13. AI TOOL LOGGING DECORATOR
# ============================================================

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


print("\n13. AI TOOL LOGGING")
print(search_documents("Python decorators"))


# ============================================================
# 14. DECORATOR WITH CONFIGURATION
# ============================================================

def confidence_threshold(threshold):

    def decorator(function):

        @wraps(function)
        def wrapper(prediction):

            if prediction < threshold:
                return "Low confidence"

            return function(prediction)

        return wrapper

    return decorator


@confidence_threshold(0.80)
def accept_prediction(confidence):
    return "Prediction accepted"


print("\n14. CONFIGURABLE DECORATOR")
print(accept_prediction(0.95))
print(accept_prediction(0.65))


# ============================================================
# 15. PRACTICE EXERCISES
# ============================================================

"""
EXERCISE 1:
Create a decorator that prints a message before
and after a function executes.

EXERCISE 2:
Create a decorator that supports positional
and keyword arguments.

EXERCISE 3:
Create a decorator that logs the function name
and its arguments.

EXERCISE 4:
Create a decorator that measures execution time.

EXERCISE 5:
Create a decorator that validates positive numbers.

EXERCISE 6:
Create a decorator that checks user authentication.

EXERCISE 7:
Create a decorator factory that repeats a function
a configurable number of times.

EXERCISE 8:
Stack two decorators and explain their execution order.

EXERCISE 9:
Use functools.wraps and inspect the decorated
function's name and documentation.

EXERCISE 10:
Create a decorator that logs the execution
of a simulated AI tool.

RULE:
For every exercise, identify:
- Original function
- Decorator function
- Wrapper function
- Arguments passed to the wrapper
- Return value
"""


# ============================================================
# END OF DECORATORS
# ============================================================
