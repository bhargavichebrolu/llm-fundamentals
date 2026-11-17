# Python Dictionaries – Complete Notes

## 1. What is a Dictionary?

A dictionary is a built-in Python data structure that stores information as key-value pairs.

Each item contains:
- Key: identifies the item.
- Value: the information associated with that key.

### Example

```python
student = {
    "name": "Ammu",
    "age": 24,
    "course": "Artificial Intelligence"
}

print(student)
print(type(student))
```

Output:

```text
{'name': 'Ammu', 'age': 24, 'course': 'Artificial Intelligence'}
<class 'dict'>
```

Access information using its key:

```python
print(student["name"])
print(student["age"])
```

Output:

```text
Ammu
24
```

## 2. Characteristics of Dictionaries

A Python dictionary has these characteristics:

1. **Key-value structure:** Each item contains a key and a value.
2. **Insertion ordered:** Python preserves the order in which items are inserted.
3. **Mutable:** You can add, update and remove items.
4. **Unique keys:** Duplicate keys are not stored separately. A later value replaces an earlier value for the same key.
5. **Different value types:** Values can be strings, numbers, lists, tuples, dictionaries, booleans and other objects.
6. **Hashable keys:** Keys must be hashable, such as strings, integers and suitable tuples.

Example:

```python
data = {
    "name": "Ammu",
    "age": 24,
    "skills": ["Python", "Java"],
    "active": True
}
```

## 3. Creating Dictionaries

### Empty dictionary

```python
student = {}
```

Or:

```python
student = dict()
```

### Dictionary with values

```python
student = {
    "name": "Ammu",
    "age": 24
}
```

### Using dict()

```python
student = dict(name="Ammu", age=24)
```

### Creating a dictionary from pairs

```python
pairs = [
    ("name", "Ammu"),
    ("age", 24)
]

student = dict(pairs)
```

### Dictionary with different data types

```python
data = {
    "name": "Ammu",
    "age": 24,
    "marks": [80, 85, 90],
    "location": ("London", "UK"),
    "active": True
}
```

## 4. Accessing Dictionary Values

### Using square brackets

```python
student = {
    "name": "Ammu",
    "age": 24
}

print(student["name"])
```

If the key does not exist, Python raises a `KeyError`.

```python
print(student["email"])  # KeyError
```

### Using get()

The `get()` method retrieves a value without raising a `KeyError` when the key is missing.

```python
print(student.get("name"))
print(student.get("email"))
```

You can provide a default value:

```python
print(student.get("email", "Not available"))
```

Output:

```text
Not available
```

### Difference between [] and get()

| Feature | `dict[key]` | `dict.get(key)` |
|---|---|---|
| Existing key | Returns value | Returns value |
| Missing key | Raises KeyError | Returns None by default |
| Default value | Not supported directly | Supported |
| Typical use | Required key | Optional key |

## 5. Adding and Updating Dictionary Items

Dictionaries are mutable, so you can add or update values.

### Adding a new item

```python
student = {
    "name": "Ammu",
    "age": 24
}

student["course"] = "Artificial Intelligence"

print(student)
```

### Updating an existing item

```python
student["age"] = 25
```

If the key exists, its value is updated. If it does not exist, a new item is added.

### Updating multiple items with update()

```python
student.update({
    "age": 25,
    "city": "London"
})
```

### setdefault()

`setdefault()` returns the existing value if the key exists. Otherwise, it inserts the key with the specified default value.

```python
student = {"name": "Ammu"}

student.setdefault("course", "AI")
student.setdefault("name", "Unknown")

print(student)
```

Result:

```python
{
    "name": "Ammu",
    "course": "AI"
}
```

The existing name is not replaced.

## 6. Removing Dictionary Items

### pop()

Removes a specified key and returns its value.

```python
student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

age = student.pop("age")

print(age)
print(student)
```

You can provide a default for a missing key:

```python
student.pop("email", None)
```

### popitem()

Removes and returns the last inserted key-value pair.

```python
student = {
    "name": "Ammu",
    "age": 24
}

item = student.popitem()

print(item)
print(student)
```

### del

Deletes a particular key-value pair.

```python
del student["name"]
```

### clear()

Removes all items.

```python
student.clear()
```

### Summary

| Operation | Purpose |
|---|---|
| `pop(key)` | Removes a specified key and returns its value |
| `popitem()` | Removes and returns the last inserted pair |
| `del dict[key]` | Deletes a specified item |
| `clear()` | Removes all items |

## 7. Dictionary Methods

### keys()

Returns a dynamic view of all keys.

```python
student = {"name": "Ammu", "age": 24}

print(student.keys())
```

### values()

Returns a dynamic view of all values.

```python
print(student.values())
```

### items()

Returns a dynamic view of key-value pairs.

```python
print(student.items())
```

### copy()

Creates a shallow copy of a dictionary.

```python
original = {"name": "Ammu", "age": 24}

copied = original.copy()

copied["age"] = 25

print(original)
print(copied)
```

The top-level dictionaries are separate, but nested mutable objects are still shared.

### fromkeys()

Creates a new dictionary from a collection of keys.

```python
keys = ["name", "age", "course"]

student = dict.fromkeys(keys, "Unknown")

print(student)
```

Result:

```python
{
    "name": "Unknown",
    "age": "Unknown",
    "course": "Unknown"
}
```

Be careful when using a mutable default value with `fromkeys()`: all keys will refer to the same object.

## 8. Iterating Through Dictionaries

### Loop through keys

```python
student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

for key in student:
    print(key)
```

This is equivalent to:

```python
for key in student.keys():
    print(key)
```

### Loop through values

```python
for value in student.values():
    print(value)
```

### Loop through key-value pairs

```python
for key, value in student.items():
    print(key, value)
```

This is one of the most useful dictionary iteration patterns.

## 9. Checking Whether a Key Exists

Use the `in` operator.

```python
student = {
    "name": "Ammu",
    "age": 24
}

print("name" in student)
print("email" in student)
```

Important: `in` checks dictionary keys, not values.

```python
print("Ammu" in student)  # False
print("Ammu" in student.values())  # True
```

## 10. Nested Dictionaries

A nested dictionary is a dictionary containing another dictionary as a value.

```python
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
```

Access nested values:

```python
print(students["student1"]["name"])
print(students["student2"]["age"])
```

Update a nested value:

```python
students["student1"]["age"] = 25
```

Add a nested item:

```python
students["student1"]["course"] = "AI"
```

Nested dictionaries are useful for representing structured information.

## 11. Dictionary Comprehension

Dictionary comprehension creates dictionaries using a compact expression.

Syntax:

```python
{key_expression: value_expression for item in iterable}
```

### Example 1: Squares

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}

print(squares)
```

Result:

```python
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
```

### Example 2: Conditional comprehension

```python
numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)
```

### Example 3: Transforming values

```python
names = ["ammu", "ravi", "john"]

uppercase_names = {
    name: name.upper()
    for name in names
}
```

## 12. Dictionary Operations

### Length

```python
student = {"name": "Ammu", "age": 24}

print(len(student))
```

Returns the number of key-value pairs.

### Merge dictionaries

Using the `|` operator in Python 3.9 and later:

```python
first = {"name": "Ammu"}
second = {"age": 24}

combined = first | second

print(combined)
```

Using update():

```python
first.update(second)
```

If both dictionaries contain the same key, the value from the right-hand dictionary wins when using `|`.

### Membership

```python
student = {"name": "Ammu", "age": 24}

print("name" in student)
print("email" not in student)
```

## 13. Dictionary Copying: Shallow Copy vs Deep Copy

This is an important Python concept.

### Shallow copy

A shallow copy creates a new outer dictionary, but nested objects remain shared.

```python
original = {
    "name": "Ammu",
    "skills": ["Python", "Java"]
}

copied = original.copy()

copied["name"] = "Ravi"
copied["skills"].append("AI")

print(original)
print(copied)
```

Changing the top-level name does not affect the original. However, appending to the nested list affects both dictionaries.

### Deep copy

A deep copy recursively copies nested objects.

```python
import copy

original = {
    "name": "Ammu",
    "skills": ["Python", "Java"]
}

copied = copy.deepcopy(original)

copied["skills"].append("AI")

print(original)
print(copied)
```

The original nested list remains unchanged.

## 14. Dictionary and JSON

Dictionary and JSON are related but are not the same thing.

### Python dictionary

A dictionary is a Python object stored in memory.

```python
student = {
    "name": "Ammu",
    "age": 24,
    "active": True
}
```

### JSON

JSON is a language-independent text format used to exchange structured data.

```json
{
    "name": "Ammu",
    "age": 24,
    "active": true
}
```

Important differences:

| Python dictionary | JSON |
|---|---|
| Python data structure | Text-based data format |
| Uses `True`, `False`, `None` | Uses `true`, `false`, `null` |
| Keys can be any hashable type | Object keys are strings |
| Can contain Python-specific objects | Supports JSON data types |

### Convert JSON string into Python dictionary

```python
import json

json_data = '{"name": "Ammu", "age": 24}'

python_data = json.loads(json_data)

print(python_data)
print(type(python_data))
```

### Convert Python dictionary into JSON string

```python
import json

student = {
    "name": "Ammu",
    "age": 24
}

json_string = json.dumps(student, indent=4)

print(json_string)
```

### Working with JSON files

- `json.load(file)` reads JSON from a file and returns Python data.
- `json.dump(data, file)` writes Python data to a JSON file.
- `json.loads(string)` parses a JSON string.
- `json.dumps(data)` serialises Python data into a JSON string.

## 15. Dictionaries in APIs

APIs commonly use JSON request and response bodies. Python applications parse these into dictionaries and lists.

Example API response:

```json
{
    "status": "success",
    "user": {
        "name": "Ammu",
        "role": "AI Engineer"
    }
}
```

After parsing:

```python
response = {
    "status": "success",
    "user": {
        "name": "Ammu",
        "role": "AI Engineer"
    }
}

print(response["status"])
print(response["user"]["name"])
```

This is why dictionaries are important for backend development and AI integrations.

## 16. Dictionaries in AI and Agentic AI

Dictionaries are heavily used in AI applications.

### Example 1: LLM configuration

```python
model_config = {
    "model": "gpt-model",
    "temperature": 0.7,
    "max_tokens": 1000
}
```

### Example 2: Prompt templates

```python
prompt = {
    "role": "You are a Python tutor.",
    "question": "Explain dictionaries.",
    "format": "step-by-step"
}
```

### Example 3: Tool definitions

```python
tool = {
    "name": "search_web",
    "description": "Search for information",
    "parameters": {
        "query": "string"
    }
}
```

### Example 4: Agent state

```python
agent_state = {
    "user_message": "Find information about Python",
    "messages": [],
    "tool_results": [],
    "next_action": "search"
}
```

### Example 5: Tool execution result

```python
tool_result = {
    "tool": "weather",
    "status": "success",
    "temperature": 18,
    "unit": "Celsius"
}
```

### Example 6: Counting words

```python
text = "AI agents use tools and AI agents use memory"

word_counts = {}

for word in text.lower().split():
    word_counts[word] = word_counts.get(word, 0) + 1

print(word_counts)
```

This demonstrates a common dictionary-based counting pattern.

## 17. Common Mistakes

### Mistake 1: Accessing a missing key

```python
student = {"name": "Ammu"}

print(student["age"])  # KeyError
```

Use `get()` when a key is optional.

### Mistake 2: Using a list as a dictionary key

```python
data = {
    [1, 2]: "value"
}
```

This raises `TypeError` because lists are unhashable.

Use a tuple when appropriate:

```python
data = {
    (1, 2): "value"
}
```

### Mistake 3: Confusing keys and values

```python
student = {"name": "Ammu"}

print("Ammu" in student)  # False
print("Ammu" in student.values())  # True
```

### Mistake 4: Duplicate keys

```python
student = {
    "name": "Ammu",
    "name": "Ravi"
}

print(student)
```

The second value replaces the first.

### Mistake 5: Modifying a dictionary while iterating

Avoid adding or removing dictionary items directly while iterating over the same dictionary.

Safer approach:

```python
scores = {
    "Ammu": 80,
    "Ravi": 90,
    "John": 70
}

for name in list(scores):
    if scores[name] < 80:
        del scores[name]
```

### Mistake 6: Assuming copy() performs a deep copy

`copy()` only creates a shallow copy. Use `copy.deepcopy()` when independent nested objects are required.

## 18. Dictionary Time Complexity

For typical Python dictionaries:

| Operation | Average time complexity |
|---|---|
| Access by key | O(1) |
| Insert | O(1) |
| Update | O(1) |
| Delete | O(1) |
| Membership by key | O(1) |
| Iteration | O(n) |
| Copy | O(n) |

These are average-case complexities. Some operations can take O(n) in worst-case circumstances.

## 19. Interview Questions

1. What is a dictionary in Python?
2. What is a key-value pair?
3. Are dictionaries mutable?
4. Do dictionaries allow duplicate keys?
5. Are dictionaries ordered?
6. What types can be dictionary keys?
7. Why can't lists be dictionary keys?
8. What is the difference between `get()` and square-bracket access?
9. What is the difference between `keys()`, `values()` and `items()`?
10. What is the difference between `pop()` and `popitem()`?
11. What does `setdefault()` do?
12. What is dictionary comprehension?
13. What is a nested dictionary?
14. What is the difference between shallow copy and deep copy?
15. What is the difference between a Python dictionary and JSON?
16. What do `json.loads()` and `json.dumps()` do?
17. How do you merge two dictionaries?
18. What is the average lookup complexity of a dictionary?
19. How can you count word frequencies using a dictionary?
20. How are dictionaries used in AI agents?

## 20. Key Takeaways

- A dictionary stores data as key-value pairs.
- Keys must be unique and hashable.
- Dictionaries are mutable and insertion ordered.
- Use `dict[key]` for required keys and `dict.get()` for optional keys.
- Use `update()` to add or modify multiple items.
- Use `items()` to iterate over keys and values together.
- Nested dictionaries represent structured data.
- Dictionary comprehension creates dictionaries efficiently.
- `copy()` is shallow; `deepcopy()` recursively copies nested objects.
- JSON is a text format; dictionaries are Python objects.
- Dictionaries are essential for APIs, LLM configurations, tool arguments and agent state.

## 21. Completion Checklist

- [ ] I can create dictionaries.
- [ ] I understand keys and values.
- [ ] I can access values using keys.
- [ ] I understand `get()` and its default values.
- [ ] I can add and update items.
- [ ] I can remove dictionary items.
- [ ] I know the important dictionary methods.
- [ ] I can iterate through dictionaries.
- [ ] I can create and access nested dictionaries.
- [ ] I understand dictionary comprehension.
- [ ] I understand shallow copy and deep copy.
- [ ] I can convert between dictionaries and JSON.
- [ ] I can explain dictionary applications in AI agents.