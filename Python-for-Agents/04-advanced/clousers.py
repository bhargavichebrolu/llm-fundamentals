
"""
CLOSURES IN PYTHON

Topics:
1. Nested functions
2. Retaining enclosing variables
3. Inspecting closures
4. nonlocal keyword
5. Independent closure instances
6. Closures with parameters
7. Closures vs global variables
8. Closures vs classes
9. Decorator connection
10. Practical AI-related examples
"""

# ============================================================
# 1. BASIC CLOSURE
# ============================================================

def create_greeting():
    message = "Welcome to Python"

    def greet():
        print(message)

    return greet


print("\n1. BASIC CLOSURE")

greeting = create_greeting()
greeting()


# ============================================================
# 2. CLOSURE RETAINING AN ENCLOSING VARIABLE
# ============================================================

def create_message():
    message = "Hello from the enclosing scope"

    def display():
        return message

    return display


print("\n2. RETAINING ENCLOSING VARIABLE")

display_message = create_message()

print(display_message())
print(display_message())


# ============================================================
# 3. INSPECTING A CLOSURE
# ============================================================

def create_storage():
    data = "Retained value"

    def show():
        return data

    return show


storage_function = create_storage()

print("\n3. INSPECTING A CLOSURE")

print(storage_function.__closure__)
print(storage_function.__closure__[0].cell_contents)


# ============================================================
# 4. MODIFYING ENCLOSING VARIABLES WITH NONLOCAL
# ============================================================

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


print("\n4. NONLOCAL COUNTER")

counter = create_counter()

print(counter())
print(counter())
print(counter())


# ============================================================
# 5. INDEPENDENT CLOSURE INSTANCES
# ============================================================

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


print("\n5. INDEPENDENT COUNTERS")

counter_one = create_counter()
counter_two = create_counter()

print("Counter one:", counter_one())
print("Counter one:", counter_one())

print("Counter two:", counter_two())
print("Counter two:", counter_two())


# ============================================================
# 6. CLOSURES WITH PARAMETERS
# ============================================================

def create_multiplier(multiplier):

    def multiply(number):
        return number * multiplier

    return multiply


print("\n6. MULTIPLIER CLOSURES")

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))


# ============================================================
# 7. CLOSURE FOR DISCOUNT CALCULATION
# ============================================================

def create_discount_calculator(discount_percentage):

    def calculate_discount(price):
        discount = price * discount_percentage / 100
        return price - discount

    return calculate_discount


print("\n7. DISCOUNT CALCULATOR")

student_discount = create_discount_calculator(10)
premium_discount = create_discount_calculator(20)

print(student_discount(100))
print(premium_discount(100))


# ============================================================
# 8. CLOSURE FOR CONFIDENCE THRESHOLD
# ============================================================

def create_predictor(threshold):

    def predict(confidence):
        if confidence >= threshold:
            return "Accepted"

        return "Rejected"

    return predict


print("\n8. AI CONFIDENCE PREDICTOR")

strict_predictor = create_predictor(0.90)
normal_predictor = create_predictor(0.70)

print(strict_predictor(0.85))
print(normal_predictor(0.85))


# ============================================================
# 9. CLOSURE WITH PRIVATE LIST
# ============================================================

def create_item_storage():
    items = []

    def add_item(item):
        items.append(item)
        return items.copy()

    return add_item


print("\n9. PRIVATE ITEM STORAGE")

storage = create_item_storage()

print(storage("Python"))
print(storage("FastAPI"))
print(storage("Agentic AI"))


# ============================================================
# 10. CLOSURE-BASED API URL BUILDER
# ============================================================

def create_api_handler(base_url):

    def build_url(endpoint):
        return f"{base_url}/{endpoint.lstrip('/')}"

    return build_url


print("\n10. API URL BUILDER")

api = create_api_handler("https://api.example.com")

print(api("users"))
print(api("products"))


# ============================================================
# 11. CLOSURE VS CLASS
# ============================================================

def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    return deposit


print("\n11. CLOSURE ACCOUNT")

deposit = create_account(100)

print(deposit(50))
print(deposit(25))


class BankAccount:

    def __init__(self, initial_balance):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


print("\nCLASS ACCOUNT")

account = BankAccount(100)

print(account.deposit(50))
print(account.deposit(25))


# ============================================================
# 12. CLOSURES AND DECORATORS
# ============================================================

def my_decorator(function):

    def wrapper():
        print("Before execution")
        function()
        print("After execution")

    return wrapper


@my_decorator
def greet():
    print("Hello")


print("\n12. DECORATOR USING A CLOSURE")

greet()


# ============================================================
# 13. PRACTICE EXERCISES
# ============================================================

"""
EXERCISE 1:
Create a closure that returns a greeting using
a name supplied to the outer function.

EXERCISE 2:
Create a counter using nonlocal.

EXERCISE 3:
Create two independent counters and demonstrate
that their states do not interfere.

EXERCISE 4:
Create a multiplier closure that supports
double and triple operations.

EXERCISE 5:
Create a closure that retains a discount percentage
and calculates discounted prices.

EXERCISE 6:
Create a closure that retains a confidence threshold
and classifies model predictions.

EXERCISE 7:
Create a closure that stores items in a private list.

EXERCISE 8:
Create a closure-based API URL builder.

EXERCISE 9:
Inspect a closure using __closure__ and cell_contents.

EXERCISE 10:
Explain the difference between a closure,
a nested function, and a global variable.
"""


# ============================================================
# END OF CLOSURES
# ============================================================
