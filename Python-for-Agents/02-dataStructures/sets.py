
# ============================================================
# DAY 02 - PYTHON SETS
# ============================================================


# 1. Creating sets

numbers = {10, 20, 30, 40}

print("1. Creating sets")
print(numbers)
print(type(numbers))

# Empty set
empty_set = set()

# Empty dictionary
empty_dictionary = {}

print(type(empty_set))
print(type(empty_dictionary))


# 2. Removing duplicates automatically

numbers = {10, 20, 10, 30, 20}

print("\n2. Unique elements")
print(numbers)


# 3. Creating sets using set()

numbers_from_list = set([10, 20, 20, 30])
characters = set("hello")

print("\n3. Using set()")
print(numbers_from_list)
print(characters)


# 4. Iterating through sets

languages = {"Python", "Java", "C++"}

print("\n4. Iteration")

for language in languages:
    print(language)


# 5. Membership checking

numbers = {10, 20, 30}

print("\n5. Membership")
print(20 in numbers)
print(50 in numbers)


# 6. Adding elements

numbers = {10, 20, 30}

numbers.add(40)
numbers.add(20)

print("\n6. add()")
print(numbers)


# 7. Adding multiple elements

numbers.update([50, 60])
numbers.update((70, 80))

print("\n7. update()")
print(numbers)


# 8. Removing elements

numbers = {10, 20, 30, 40}

numbers.remove(20)

print("\n8. remove()")
print(numbers)

# discard() does not raise an error if missing.
numbers.discard(100)

print("After discard:", numbers)

# pop() removes an arbitrary element.
removed_element = numbers.pop()

print("Removed:", removed_element)
print("Remaining:", numbers)

numbers.clear()

print("After clear:", numbers)


# 9. Union

python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya", "David"}

union_result = python_students | java_students

print("\n9. Union")
print(union_result)

# Alternative
print(python_students.union(java_students))


# 10. Intersection

python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya", "John"}

intersection_result = python_students & java_students

print("\n10. Intersection")
print(intersection_result)

# Alternative
print(python_students.intersection(java_students))


# 11. Difference

python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya"}

difference_result = python_students - java_students

print("\n11. Difference")
print(difference_result)

# Difference is directional.
print(java_students - python_students)


# 12. Symmetric difference

python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya"}

symmetric_result = python_students ^ java_students

print("\n12. Symmetric difference")
print(symmetric_result)


# 13. Subset

small = {10, 20}
large = {10, 20, 30, 40}

print("\n13. Subset")
print(small.issubset(large))
print(small <= large)


# 14. Superset

print("\n14. Superset")
print(large.issuperset(small))
print(large >= small)


# 15. Disjoint sets

first = {10, 20}
second = {30, 40}

print("\n15. Disjoint")
print(first.isdisjoint(second))


# 16. Equality

print("\n16. Set equality")
print({10, 20, 30} == {30, 20, 10})


# 17. Updating existing sets

first = {10, 20, 30}
second = {20, 30, 40}

first.intersection_update(second)

print("\n17. intersection_update()")
print(first)


# 18. Set comprehension

squares = {
    number ** 2
    for number in range(1, 6)
}

print("\n18. Set comprehension")
print(squares)

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)


# 19. Removing duplicates from a list

numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print("\n19. Remove duplicates")
print(unique_numbers)

# Preserve original order:
unique_ordered_numbers = list(dict.fromkeys(numbers))

print("Order preserved:", unique_ordered_numbers)


# 20. Frozenset

permissions = frozenset({"read", "write", "execute"})

print("\n20. Frozenset")
print(permissions)

# This would raise AttributeError:
# permissions.add("delete")


# 21. Frozenset as a dictionary key

permissions = frozenset({"read", "write"})

roles = {
    permissions: "admin"
}

print("\n21. Frozenset as dictionary key")
print(roles[permissions])


# 22. AI application: unique tools

tools = [
    "search",
    "calculator",
    "search",
    "weather",
    "calculator"
]

unique_tools = set(tools)

print("\n22. Unique agent tools")
print(unique_tools)


# 23. AI application: permission checking

allowed_permissions = {
    "read",
    "search",
    "summarise"
}

requested_permissions = {
    "read",
    "search"
}

if requested_permissions.issubset(allowed_permissions):
    print("\n23. Permission granted")
else:
    print("\n23. Permission denied")


# 24. AI application: missing tools

available_tools = {
    "search",
    "calculator",
    "weather"
}

required_tools = {
    "search",
    "weather",
    "database"
}

missing_tools = required_tools - available_tools

print("\n24. Missing tools")
print(missing_tools)


# 25. AI application: retrieved document IDs

retrieved_documents = {
    "doc_101",
    "doc_102",
    "doc_103"
}

new_documents = {
    "doc_102",
    "doc_104"
}

all_documents = retrieved_documents | new_documents

print("\n25. Unique retrieved documents")
print(all_documents)


# 26. AI application: common skills

python_skills = {
    "Python",
    "NumPy",
    "Pandas",
    "FastAPI"
}

ai_skills = {
    "Python",
    "PyTorch",
    "Pandas",
    "Transformers"
}

common_skills = python_skills & ai_skills

print("\n26. Common skills")
print(common_skills)


# 27. Sorting set elements

numbers = {40, 10, 30, 20}

sorted_numbers = sorted(numbers)

print("\n27. Sorting")
print(sorted_numbers)
print(type(sorted_numbers))  # list


# ============================================================
# END OF DAY 02 - SETS
# ============================================================
