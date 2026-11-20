
"""
PYTHON FUNCTION SCOPE
Topics:
1. Local scope
2. Enclosing scope
3. Global scope
4. Built-in scope
5. LEGB rule
6. global keyword
7. nonlocal keyword
8. Nested functions
9. Common scope errors
"""

# ============================================================
# 1. LOCAL SCOPE
# ============================================================

def local_scope_example():
    name = "Python"
    age = 25

    print("Name:", name)
    print("Age:", age)


local_scope_example()

# name and age cannot be accessed directly outside this function.


# ============================================================
# 2. EACH FUNCTION HAS ITS OWN LOCAL SCOPE
# ============================================================

def first_function():
    message = "Hello from first function"
    print(message)


def second_function():
    message = "Hello from second function"
    print(message)


first_function()
second_function()

# Both functions have their own independent local variable.


# ============================================================
# 3. ENCLOSING SCOPE
# ============================================================

def outer_function():

    message = "Hello from outer function"

    def inner_function():
        print("Inner function:", message)

    inner_function()


outer_function()

# The inner function can access variables from its
# enclosing function.


# ============================================================
# 4. GLOBAL SCOPE
# ============================================================

company = "OpenAI"


def display_company():
    print("Company:", company)


display_company()
print("Global company:", company)


# ============================================================
# 5. GLOBAL KEYWORD
# ============================================================

total_requests = 0


def record_request():
    global total_requests
    total_requests += 1


record_request()
record_request()
record_request()

print("Total requests:", total_requests)


# ============================================================
# 6. BUILT-IN SCOPE
# ============================================================

numbers = [10, 20, 30, 40, 50]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Type:", type(numbers))


# ============================================================
# 7. LEGB RULE
# ============================================================

name = "Global"


def outer():

    name = "Enclosing"

    def inner():

        name = "Local"

        print("LEGB result:", name)

    inner()


outer()

# Python finds the variable in the local scope first.


# ============================================================
# 8. LEGB - ENCLOSING VARIABLE
# ============================================================

name = "Global"


def outer():

    name = "Enclosing"

    def inner():
        print("Enclosing result:", name)

    inner()


outer()

# The inner function has no local name.
# Python searches the enclosing scope.


# ============================================================
# 9. LEGB - GLOBAL VARIABLE
# ============================================================

name = "Global"


def outer():

    def inner():
        print("Global result:", name)

    inner()


outer()

# No local or enclosing name exists.
# Python searches the global scope.


# ============================================================
# 10. MODIFYING AN ENCLOSING VARIABLE WITH NONLOCAL
# ============================================================

def outer_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        print("Count:", count)

    increment()
    increment()
    increment()


outer_counter()


# ============================================================
# 11. GLOBAL VS NONLOCAL
# ============================================================

value = 100


def outer():

    value = 50

    def inner():
        nonlocal value
        value += 10

    inner()

    print("Enclosing value:", value)


outer()

print("Global value:", value)


# ============================================================
# 12. NESTED FUNCTIONS
# ============================================================

def create_greeting():

    greeting = "Welcome"

    def greet_user(username):
        print(greeting, username)

    return greet_user


greeting_function = create_greeting()

greeting_function("Alex")
greeting_function("Sam")


# ============================================================
# 13. COMMON ERROR: ACCESSING A LOCAL VARIABLE OUTSIDE
# ============================================================

def calculate():
    result = 100
    print("Result inside function:", result)


calculate()

# Uncommenting the following line raises NameError:
# print(result)


# ============================================================
# 14. COMMON ERROR: MODIFYING WITHOUT GLOBAL
# ============================================================

# Uncomment this example to observe UnboundLocalError.

# count = 0
#
# def increment_without_global():
#     count += 1
#
# increment_without_global()


# ============================================================
# 15. SHADOWING A GLOBAL VARIABLE
# ============================================================

language = "Java"


def change_language():
    language = "Python"
    print("Inside function:", language)


change_language()

print("Outside function:", language)

# The local variable does not modify the global variable.


# ============================================================
# 16. PRACTICAL EXAMPLE: REQUEST TRACKER
# ============================================================

api_requests = 0


def track_api_request():
    global api_requests
    api_requests += 1
    return api_requests


print("API request:", track_api_request())
print("API request:", track_api_request())
print("API request:", track_api_request())


# ============================================================
# 17. PRACTICAL EXAMPLE: PRIVATE COUNTER
# ============================================================

def create_counter():

    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = create_counter()

print("Counter:", counter())
print("Counter:", counter())
print("Counter:", counter())


# ============================================================
# 18. INDEPENDENT COUNTERS
# ============================================================

counter_one = create_counter()
counter_two = create_counter()

print("Counter one:", counter_one())  # 1
print("Counter one:", counter_one())  # 2

print("Counter two:", counter_two())  # 1
print("Counter two:", counter_two())  # 2


# ============================================================
# 19. PRACTICE EXERCISES
# ============================================================

"""
Exercise 1:
Create a function called calculate_total().
Create a local variable called price with value 500.
Print the price inside the function.

Exercise 2:
Create an outer function called user_details().
Define username inside it.
Create an inner function that prints username.

Exercise 3:
Create a global variable called score = 0.
Create a function that increases score by 10.
Use the global keyword.

Exercise 4:
Create an outer function with a variable called balance = 1000.
Create an inner function that increases balance by 500.
Use nonlocal.

Exercise 5:
Create two nested functions.
Define the same variable name in local,
enclosing and global scopes.
Print the variable from the innermost function.
Identify which value Python selects.

Exercise 6:
Create a counter using a nested function.
Call the returned function five times.
Print each updated count.
"""
