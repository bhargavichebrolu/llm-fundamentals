
"""
PYTHON LISTS - COMPLETE PRACTICAL REFERENCE

Repository: python-for-agents
Module: Python Fundamentals
Topic: Lists
"""

import copy


# =====================================================
# 1. CREATING LISTS
# =====================================================

empty_list = []

languages = ["Python", "Java", "C++"]

numbers = [10, 20, 30, 40]

mixed_data = ["Ammu", 24, 85.5, True]

nested_list = [[1, 2], [3, 4]]

characters = list("PYTHON")

range_numbers = list(range(1, 6))

print("1. Creating Lists")
print(languages)
print(numbers)
print(mixed_data)
print(characters)
print(range_numbers)


# =====================================================
# 2. INDEXING
# =====================================================

tools = ["Python", "LangChain", "LangGraph", "MCP"]

print("\n2. Indexing")

print(tools[0])
print(tools[1])
print(tools[-1])
print(tools[-2])


# =====================================================
# 3. SLICING
# =====================================================

numbers = [10, 20, 30, 40, 50, 60]

print("\n3. Slicing")

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])


# =====================================================
# 4. MODIFYING ELEMENTS
# =====================================================

languages = ["Python", "Java", "C++"]

languages[1] = "JavaScript"

print("\n4. Modifying Elements")
print(languages)


# =====================================================
# 5. ADDING ELEMENTS
# =====================================================

tools = ["Python", "LangChain"]

# Add one element
tools.append("LangGraph")

# Add multiple elements
tools.extend(["MCP", "RAG"])

# Insert at a specific position
tools.insert(1, "NumPy")

print("\n5. Adding Elements")
print(tools)


# =====================================================
# 6. APPEND VS EXTEND
# =====================================================

a = [1, 2]
a.append([3, 4])

b = [1, 2]
b.extend([3, 4])

print("\n6. Append vs Extend")
print("Append:", a)
print("Extend:", b)


# =====================================================
# 7. REMOVING ELEMENTS
# =====================================================

tools = ["Python", "Java", "MCP", "RAG"]

# Remove by value
tools.remove("Java")

# Remove by index and return value
removed = tools.pop(1)

print("\n7. Removing Elements")
print("Removed:", removed)
print("Remaining:", tools)

# Delete by index
del tools[0]

# Clear all elements
temporary = [1, 2, 3]
temporary.clear()

print("After del:", tools)
print("After clear:", temporary)


# =====================================================
# 8. SEARCHING
# =====================================================

languages = ["Python", "Java", "Python", "C++"]

print("\n8. Searching")

print("Python exists:", "Python" in languages)
print("Java missing:", "JavaScript" not in languages)
print("Python index:", languages.index("Python"))
print("Python count:", languages.count("Python"))


# =====================================================
# 9. SORTING
# =====================================================

numbers = [40, 10, 30, 20]

numbers.sort()

print("\n9. Sorting")
print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)

original = [40, 10, 30, 20]

sorted_numbers = sorted(original)

print("Sorted copy:", sorted_numbers)
print("Original:", original)


# =====================================================
# 10. REVERSE
# =====================================================

numbers = [10, 20, 30, 40]

numbers.reverse()

print("\n10. Reverse")
print(numbers)


# =====================================================
# 11. BUILT-IN FUNCTIONS
# =====================================================

numbers = [10, 20, 30, 40, 50]

print("\n11. Built-in Functions")

print("Length:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))


# =====================================================
# 12. ITERATING THROUGH LISTS
# =====================================================

tools = ["Python", "LangChain", "MCP"]

print("\n12. For Loop")

for tool in tools:
    print(tool)


# Using while loop

print("\nWhile Loop")

i = 0

while i < len(tools):
    print(tools[i])
    i += 1


# Using enumerate()

print("\nEnumerate")

for index, tool in enumerate(tools, start=1):
    print(index, tool)


# =====================================================
# 13. LIST COMPREHENSION
# =====================================================

numbers = [1, 2, 3, 4, 5, 6]

squares = [n ** 2 for n in numbers]

even_numbers = [
    n for n in numbers
    if n % 2 == 0
]

labels = [
    "Even" if n % 2 == 0 else "Odd"
    for n in numbers
]

print("\n13. List Comprehension")
print("Squares:", squares)
print("Even:", even_numbers)
print("Labels:", labels)


# =====================================================
# 14. NESTED LISTS
# =====================================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n14. Nested Lists")

print(matrix[0])
print(matrix[1][2])

for row in matrix:
    for element in row:
        print(element)


# =====================================================
# 15. COPYING LISTS
# =====================================================

original = [10, 20, 30]

# Direct assignment: same object
same_reference = original

# Shallow copy
shallow_copy = original.copy()

# Slicing copy
slicing_copy = original[:]

print("\n15. Copying Lists")

same_reference.append(40)

print("Original:", original)
print("Same reference:", same_reference)
print("Shallow copy:", shallow_copy)
print("Slicing copy:", slicing_copy)


# Deep copy with nested lists

nested_original = [[1, 2], [3, 4]]

deep_copy = copy.deepcopy(nested_original)

deep_copy[0][0] = 100

print("Nested original:", nested_original)
print("Deep copy:", deep_copy)


# =====================================================
# 16. LIST UNPACKING
# =====================================================

details = ["Python", "AI", 24]

language, field, age = details

print("\n16. List Unpacking")
print(language)
print(field)
print(age)


numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print("First:", first)
print("Middle:", middle)
print("Last:", last)


# =====================================================
# 17. LIST OPERATORS
# =====================================================

a = [1, 2]
b = [3, 4]

print("\n17. List Operators")

print("Concatenation:", a + b)
print("Repetition:", a * 3)
print("Membership:", 2 in a)


# =====================================================
# 18. REMOVING DUPLICATES
# =====================================================

languages = ["Python", "Java", "Python", "C++", "Java"]

# Preserve the original order
unique_languages = list(dict.fromkeys(languages))

print("\n18. Removing Duplicates")
print(unique_languages)


# =====================================================
# 19. AI APPLICATION: CONVERSATION HISTORY
# =====================================================

messages = [
    {
        "role": "user",
        "content": "What is Python?"
    },
    {
        "role": "assistant",
        "content": "Python is a programming language."
    }
]

print("\n19. AI Conversation History")

for message in messages:
    print(message["role"], ":", message["content"])


# =====================================================
# 20. AI APPLICATION: AGENT TOOLS
# =====================================================

agent_tools = [
    "web_search",
    "calculator",
    "database_search"
]

agent_tools.append("file_reader")

print("\n20. AI Agent Tools")
print(agent_tools)


# =====================================================
# 21. AI APPLICATION: EVALUATION RESULTS
# =====================================================

scores = [0.91, 0.87, 0.94, 0.89]

average_score = sum(scores) / len(scores)

print("\n21. Model Evaluation")
print("Average score:", average_score)


# =====================================================
# 22. SAFE LIST ACCESS
# =====================================================

def get_element(items, index):
    if -len(items) <= index < len(items):
        return items[index]

    return None


numbers = [10, 20, 30]

print("\n22. Safe Access")
print(get_element(numbers, 1))
print(get_element(numbers, 10))


# =====================================================
# END
# =====================================================
