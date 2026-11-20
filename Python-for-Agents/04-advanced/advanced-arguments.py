
# ============================================================
# ADVANCED FUNCTION ARGUMENTS
# ============================================================

# 1. Positional Arguments
# Values are assigned based on their position.

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Ammu", 24)


# 2. Keyword Arguments
# Values are assigned using parameter names.

def create_profile(name, role, country):
    print(f"Name: {name}")
    print(f"Role: {role}")
    print(f"Country: {country}")


create_profile(
    name="Ammu",
    role="AI Engineer",
    country="UK"
)


# 3. Default Arguments
# A default value is used when an argument is not provided.

def greet(name, message="Welcome"):
    print(f"{message}, {name}!")


greet("Ammu")
greet("Ammu", "Good morning")


# 4. Mutable Default Argument Problem
# Never use a mutable object as a default argument
# when you intend to create a fresh object for each call.

def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item("Python"))
print(add_item("FastAPI"))


# 5. *args
# Accepts any number of positional arguments.
# Python collects them into a tuple.

def calculate_total(*numbers):
    return sum(numbers)


print(calculate_total(10, 20))
print(calculate_total(10, 20, 30, 40))


# 6. **kwargs
# Accepts any number of keyword arguments.
# Python collects them into a dictionary.

def display_details(**details):
    for key, value in details.items():
        print(f"{key}: {value}")


display_details(
    name="Ammu",
    role="Developer",
    skill="Python"
)


# 7. Combining Different Argument Types
# Parameter order matters.

def create_user(name, age, *skills, country="UK", **extra_details):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Skills: {skills}")
    print(f"Country: {country}")
    print(f"Additional details: {extra_details}")


create_user(
    "Ammu",
    24,
    "Python",
    "FastAPI",
    "SQL",
    country="UK",
    experience="Beginner",
    goal="Agentic AI"
)


# 8. Keyword-Only Arguments
# Parameters after * must be passed using their names.

def generate_response(prompt, *, temperature, max_tokens):
    print(f"Prompt: {prompt}")
    print(f"Temperature: {temperature}")
    print(f"Maximum tokens: {max_tokens}")


generate_response(
    "Explain Python decorators",
    temperature=0.7,
    max_tokens=200
)


# 9. Positional-Only Arguments
# Parameters before / must be passed positionally.

def divide(a, b, /):
    return a / b


print(divide(20, 5))

# This would raise a TypeError:
# divide(a=20, b=5)


# 10. Argument Unpacking with *
# Unpacks a list or tuple into positional arguments.

def add_numbers(a, b, c):
    return a + b + c


values = [10, 20, 30]

print(add_numbers(*values))


# 11. Argument Unpacking with **
# Unpacks a dictionary into keyword arguments.

def show_product(name, price, category):
    print(f"Product: {name}")
    print(f"Price: £{price}")
    print(f"Category: {category}")


product = {
    "name": "Laptop",
    "price": 850,
    "category": "Electronics"
}

show_product(**product)


# 12. Type Hints with Function Arguments
# Type hints communicate expected input and output types.

def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("The list cannot be empty")

    return sum(numbers) / len(numbers)


print(calculate_average([10.5, 20.5, 30.5]))


# 13. Passing Functions as Arguments
# Callable describes a function that can be passed as an argument.

from typing import Callable


def execute_operation(
    a: float,
    b: float,
    operation: Callable[[float, float], float]
) -> float:
    return operation(a, b)


def multiply(a: float, b: float) -> float:
    return a * b


print(execute_operation(5, 4, multiply))


# ============================================================
# PRACTICE EXERCISES
# Complete these without looking at solutions.
# ============================================================

# Exercise 1:
# Create a function called calculate_bill().
# It should accept:
# - item_name
# - quantity
# - price
# Return the total bill amount.


# Exercise 2:
# Create a function called calculate_marks().
# Accept any number of marks using *args.
# Return the total and average marks.


# Exercise 3:
# Create a function called build_student_profile().
# Accept a student's name as a required argument.
# Accept additional details using **kwargs.
# Print all the details.


# Exercise 4:
# Create a function called create_agent_config().
# Accept:
# - model_name as a positional argument
# - temperature as a keyword-only argument
# - max_tokens as a keyword-only argument
# Return these values in a dictionary.


# Exercise 5:
# Create a function called process_documents().
# Accept a list of document names.
# Use * to unpack the list into a function that accepts
# three document names as separate arguments.


# Exercise 6:
# Create a function called calculate_discount().
# Accept price as a positional-only argument.
# Accept discount_percentage as a keyword-only argument.
# Return the discounted price.


# Exercise 7:
# Create a function called merge_settings().
# Accept default settings and user settings as dictionaries.
# Use **kwargs to accept additional settings.
# Return one combined dictionary.


# Exercise 8:
# Create a function called apply_transformation().
# Accept a list of numbers and a function.
# Apply the supplied function to every number.
# Return the transformed list.


# Exercise 9:
# Create a function called generate_prompt().
# Accept:
# - role
# - task
# - context as an optional argument
# - additional parameters using **kwargs
# Return a formatted prompt string.


# Exercise 10:
# Create a function called run_agent().
# Accept:
# - agent_name
# - any number of tools using *args
# - model as a keyword-only argument
# - additional configuration using **kwargs
# Print all the supplied information.
