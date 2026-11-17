
# ============================================================
# DAY 02 - PYTHON TUPLES
# ============================================================

# 1. Creating tuples

empty_tuple = ()

numbers = (10, 20, 30, 40)

mixed_data = ("Python", 3.13, 100, True)

# Tuple without parentheses
another_tuple = 10, 20, 30

# Single-element tuple: comma is compulsory
single_element = (10,)

not_a_tuple = (10)

print("1. Creating tuples")
print(numbers)
print(type(single_element))
print(type(not_a_tuple))


# 2. Converting an iterable into a tuple

numbers_from_list = tuple([10, 20, 30])
characters = tuple("AI")

print("\n2. Tuple conversion")
print(numbers_from_list)
print(characters)


# 3. Indexing

languages = ("Python", "Java", "C++", "JavaScript")

print("\n3. Indexing")
print(languages[0])
print(languages[1])
print(languages[-1])
print(languages[-2])


# 4. Slicing

values = (10, 20, 30, 40, 50, 60)

print("\n4. Slicing")
print(values[1:4])
print(values[:3])
print(values[2:])
print(values[::2])
print(values[::-1])


# 5. Immutability

immutable_data = (10, 20, 30)

# This would raise TypeError:
# immutable_data[0] = 100

# A tuple can contain mutable objects.
nested_mutable_data = (10, 20, [30, 40])

nested_mutable_data[2].append(50)

print("\n5. Immutability")
print(nested_mutable_data)


# 6. Tuple methods: count() and index()

numbers = (10, 20, 10, 30, 10)

print("\n6. Tuple methods")
print("Count:", numbers.count(10))
print("First index:", numbers.index(10))


# 7. Built-in functions

scores = (75, 85, 90, 95)

print("\n7. Built-in functions")
print("Length:", len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
print("Sum:", sum(scores))
print("Sorted:", sorted(scores))
print("Any:", any((False, True, False)))
print("All:", all((True, True, True)))


# 8. Tuple unpacking

student = ("Ammu", 24, "Artificial Intelligence")

name, age, course = student

print("\n8. Tuple unpacking")
print(name)
print(age)
print(course)


# 9. Extended unpacking

numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print("\n9. Extended unpacking")
print("First:", first)
print("Middle:", middle)
print("Last:", last)


# 10. Ignoring values during unpacking

student = ("Ammu", 24, "AI")

name, _, course = student

print("\n10. Ignoring values")
print(name, course)


# 11. Concatenation

first_tuple = (10, 20)
second_tuple = (30, 40)

combined = first_tuple + second_tuple

print("\n11. Concatenation")
print(combined)


# 12. Repetition

repeated = (1, 2) * 3

print("\n12. Repetition")
print(repeated)


# 13. Membership

languages = ("Python", "Java", "C++")

print("\n13. Membership")
print("Python" in languages)
print("Ruby" not in languages)


# 14. Tuple comparison

print("\n14. Tuple comparison")
print((1, 2, 3) == (1, 2, 3))
print((1, 2) < (1, 3))


# 15. Nested tuples

students = (
    ("Ammu", 85),
    ("Ravi", 90),
    ("John", 78)
)

print("\n15. Nested tuples")
print(students[0])
print(students[0][0])
print(students[1][1])


# 16. List to tuple and tuple to list

numbers_list = [10, 20, 30]
numbers_tuple = tuple(numbers_list)

print("\n16. List to tuple")
print(numbers_tuple)

numbers_tuple = (10, 20, 30)
numbers_list = list(numbers_tuple)

numbers_list.append(40)

print("Tuple to list:", numbers_list)


# 17. Tuple as dictionary key

locations = {
    (51.5072, -0.1276): "London",
    (40.7128, -74.0060): "New York"
}

print("\n17. Tuple as dictionary key")
print(locations[(51.5072, -0.1276)])


# 18. Returning multiple values from a function

def get_student_details():
    name = "Ammu"
    age = 24
    course = "Artificial Intelligence"

    return name, age, course


student_details = get_student_details()

print("\n18. Returning multiple values")
print(student_details)

name, age, course = get_student_details()

print("Name:", name)
print("Age:", age)
print("Course:", course)


# 19. AI application: model configuration

model_config = ("gpt-model", 0.7, 1000)

model_name, temperature, max_tokens = model_config

print("\n19. AI model configuration")
print("Model:", model_name)
print("Temperature:", temperature)
print("Maximum tokens:", max_tokens)


# 20. AI application: tool execution result

def execute_tool():
    status = "success"
    message = "Weather retrieved"
    temperature = 18.5

    return status, message, temperature


tool_result = execute_tool()

status, message, temperature = tool_result

print("\n20. AI tool result")
print("Status:", status)
print("Message:", message)
print("Temperature:", temperature)


# ============================================================
# END OF DAY 02 - TUPLES
# ============================================================
