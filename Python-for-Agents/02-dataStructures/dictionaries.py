
# ============================================================
# DAY 02 - PYTHON DICTIONARIES
# ============================================================

import json
import copy


# 1. Creating dictionaries

empty_dict = {}

student = {
    "name": "Ammu",
    "age": 24,
    "course": "Artificial Intelligence"
}

print("1. Creating dictionaries")
print(student)
print(type(student))


# 2. Creating dictionaries using dict()

student_two = dict(name="Ravi", age=25)

pairs = [
    ("name", "John"),
    ("age", 26)
]

student_three = dict(pairs)

print("\n2. Using dict()")
print(student_two)
print(student_three)


# 3. Accessing values

student = {
    "name": "Ammu",
    "age": 24
}

print("\n3. Accessing values")
print(student["name"])
print(student.get("age"))
print(student.get("email", "Not available"))

# student["email"] would raise KeyError.


# 4. Adding and updating values

student["course"] = "AI"
student["age"] = 25

student.update({
    "city": "London",
    "active": True
})

print("\n4. Adding and updating")
print(student)


# 5. setdefault()

student.setdefault("country", "UK")
student.setdefault("name", "Unknown")

print("\n5. setdefault")
print(student)


# 6. Removing items

student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

removed_age = student.pop("age")
last_item = student.popitem()

print("\n6. Removing items")
print("Removed age:", removed_age)
print("Last item:", last_item)
print(student)

student["city"] = "London"
del student["city"]

print("After del:", student)

student.clear()

print("After clear:", student)


# 7. Dictionary methods

student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

print("\n7. Dictionary methods")
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

copied_student = student.copy()

print("Copy:", copied_student)

default_data = dict.fromkeys(
    ["name", "age", "course"],
    "Unknown"
)

print("From keys:", default_data)


# 8. Iterating through dictionaries

student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

print("\n8. Iterating through keys")

for key in student:
    print(key)

print("\nIterating through values")

for value in student.values():
    print(value)

print("\nIterating through key-value pairs")

for key, value in student.items():
    print(key, ":", value)


# 9. Checking whether a key exists

student = {
    "name": "Ammu",
    "age": 24
}

print("\n9. Membership")
print("name" in student)
print("email" in student)
print("Ammu" in student)
print("Ammu" in student.values())


# 10. Nested dictionaries

students = {
    "student1": {
        "name": "Ammu",
        "age": 24
    },
    "student2": {
        "name": "Ravi",
        "age": 25
    }
}

print("\n10. Nested dictionaries")
print(students["student1"]["name"])
print(students["student2"]["age"])

students["student1"]["course"] = "AI"
students["student1"]["age"] = 25

print(students)


# 11. Dictionary comprehension

squares = {
    number: number ** 2
    for number in range(1, 6)
}

print("\n11. Dictionary comprehension")
print(squares)

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)


# 12. Dictionary length

student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

print("\n12. Dictionary length")
print(len(student))


# 13. Merging dictionaries

first = {
    "name": "Ammu"
}

second = {
    "age": 24
}

combined = first | second

print("\n13. Merging dictionaries")
print(combined)

# Alternative:
first.update(second)
print(first)


# 14. Shallow copy

original = {
    "name": "Ammu",
    "skills": ["Python", "Java"]
}

shallow_copy = original.copy()

shallow_copy["name"] = "Ravi"
shallow_copy["skills"].append("AI")

print("\n14. Shallow copy")
print("Original:", original)
print("Copy:", shallow_copy)


# 15. Deep copy

original = {
    "name": "Ammu",
    "skills": ["Python", "Java"]
}

deep_copy = copy.deepcopy(original)

deep_copy["skills"].append("AI")

print("\n15. Deep copy")
print("Original:", original)
print("Deep copy:", deep_copy)


# 16. Python dictionary to JSON string

student = {
    "name": "Ammu",
    "age": 24,
    "active": True
}

json_string = json.dumps(student, indent=4)

print("\n16. Dictionary to JSON")
print(json_string)


# 17. JSON string to Python dictionary

json_data = '{"name": "Ammu", "age": 24, "active": true}'

python_data = json.loads(json_data)

print("\n17. JSON to dictionary")
print(python_data)
print(type(python_data))


# 18. JSON file operations

student = {
    "name": "Ammu",
    "age": 24
}

# Write dictionary data to a JSON file.
with open("student.json", "w", encoding="utf-8") as file:
    json.dump(student, file, indent=4)

# Read JSON file into a Python object.
with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

print("\n18. JSON file operations")
print(loaded_student)


# 19. AI application: model configuration

model_config = {
    "model": "gpt-model",
    "temperature": 0.7,
    "max_tokens": 1000
}

print("\n19. AI model configuration")
print(model_config["model"])
print(model_config["temperature"])


# 20. AI application: prompt structure

prompt = {
    "role": "You are a Python tutor.",
    "question": "Explain dictionaries.",
    "format": "Step by step"
}

print("\n20. Prompt structure")
print(prompt)


# 21. AI application: tool definition

tool = {
    "name": "search_web",
    "description": "Search for information",
    "parameters": {
        "query": "string"
    }
}

print("\n21. Tool definition")
print(tool)


# 22. AI application: agent state

agent_state = {
    "user_message": "Find information about Python",
    "messages": [],
    "tool_results": [],
    "next_action": "search"
}

agent_state["messages"].append("User requested Python information")

print("\n22. Agent state")
print(agent_state)


# 23. AI application: tool execution result

tool_result = {
    "tool": "weather",
    "status": "success",
    "temperature": 18,
    "unit": "Celsius"
}

print("\n23. Tool execution result")
print(tool_result["status"])
print(tool_result["temperature"])


# 24. Word frequency counter

text = "AI agents use tools and AI agents use memory"

word_counts = {}

for word in text.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

print("\n24. Word frequency")
print(word_counts)


# ============================================================
# END OF DAY 02 - DICTIONARIES
# ============================================================
