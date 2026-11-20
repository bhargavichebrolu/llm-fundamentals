# Python Lists

## 1. What Is a List?

A **list** is a built-in Python data structure used to store multiple items in a single variable.

Lists are:
- **Ordered:** Items maintain their insertion order.
- **Mutable:** Items can be added, removed, or modified.
- **Allow duplicates:** The same value can appear multiple times.
- **Heterogeneous:** A list can contain different data types.
- **Indexed:** Each item has a position, starting from index `0`.

```python
# Creating a list
skills = ["Python", "FastAPI", "SQL", "Machine Learning"]

print(skills)
print(type(skills))
```

Output:

```text
['Python', 'FastAPI', 'SQL', 'Machine Learning']
<class 'list'>
```

## 2. Creating Lists

Lists are created using square brackets `[]`.

```python
# Empty list
empty_list = []

# List of strings
languages = ["Python", "Java", "C++"]

# List of integers
numbers = [10, 20, 30, 40]

# List of mixed data types
student = ["Ammu", 24, 85.5, True]

# List containing duplicate values
values = [10, 20, 10, 30]

# Using the list() constructor
characters = list("Python")

print(empty_list)
print(languages)
print(numbers)
print(student)
print(values)
print(characters)
```

## 3. Accessing List Elements

Each element has an index.

Python uses zero-based indexing.

| Element | Python index |
|---|---:|
| Python | 0 |
| Java | 1 |
| FastAPI | 2 |
| SQL | 3 |

```python
technologies = ["Python", "Java", "FastAPI", "SQL"]

print(technologies[0])  # Python
print(technologies[1])  # Java
print(technologies[2])  # FastAPI
print(technologies[3])  # SQL
```

### Negative Indexing

Negative indexing accesses elements from the end of the list.

| Element | Negative index |
|---|---:|
| Python | -4 |
| Java | -3 |
| FastAPI | -2 |
| SQL | -1 |

```python
technologies = ["Python", "Java", "FastAPI", "SQL"]

print(technologies[-1])  # SQL
print(technologies[-2])  # FastAPI
print(technologies[-3])  # Java
```

Accessing an index outside the valid range raises an `IndexError`.

```python
numbers = [10, 20, 30]

# print(numbers[5])  # IndexError
```

## 4. Slicing Lists

Slicing extracts a portion of a list.

Syntax:

```python
list[start:stop:step]
```

- `start`: Index where slicing begins (included).
- `stop`: Index where slicing ends (excluded).
- `step`: Number of positions to move each time.

```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50, 60]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [60, 50, 40, 30, 20, 10]
```

Slicing does not include the stop index.

### Copying a List Using Slicing

```python
original = [10, 20, 30]

copied = original[:]

print(copied)
```

This creates a shallow copy of the list.

## 5. Modifying List Elements

Lists are mutable, so their elements can be changed after creation.

```python
languages = ["Python", "Java", "C++"]

languages[1] = "JavaScript"

print(languages)
```

Output:

```text
['Python', 'JavaScript', 'C++']
```

You can also modify multiple elements using slicing.

```python
numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)
```

Output:

```text
[10, 200, 300, 40]
```

## 6. Adding Elements to Lists

Python provides several methods to add elements.

### append()

Adds one element to the end of a list.

```python
skills = ["Python", "Java"]

skills.append("FastAPI")

print(skills)
```

Output:

```text
['Python', 'Java', 'FastAPI']
```

### extend()

Adds multiple elements from an iterable to the end of a list.

```python
skills = ["Python", "Java"]

skills.extend(["FastAPI", "SQL"])

print(skills)
```

Output:

```text
['Python', 'Java', 'FastAPI', 'SQL']
```

### insert()

Adds an element at a specified index.

```python
skills = ["Python", "Java"]

skills.insert(1, "FastAPI")

print(skills)
```

Output:

```text
['Python', 'FastAPI', 'Java']
```

### Difference Between append() and extend()

```python
numbers = [1, 2, 3]

numbers.append([4, 5])
print(numbers)

# Output: [1, 2, 3, [4, 5]]
```

`append()` adds the supplied object as one element.

```python
numbers = [1, 2, 3]

numbers.extend([4, 5])
print(numbers)

# Output: [1, 2, 3, 4, 5]
```

`extend()` adds each element from the supplied iterable.

## 7. Removing Elements from Lists

### remove()

Removes the first matching value.

```python
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)
```

Output:

```text
[10, 30, 20]
```

If the value does not exist, `remove()` raises a `ValueError`.

### pop()

Removes and returns an element.

```python
numbers = [10, 20, 30]

removed = numbers.pop()

print(removed)  # 30
print(numbers)  # [10, 20]
```

You can also specify an index.

```python
numbers = [10, 20, 30]

removed = numbers.pop(1)

print(removed)  # 20
print(numbers)  # [10, 30]
```

### del

Deletes an element or a slice using its index.

```python
numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)
```

Output:

```text
[10, 30, 40]
```

Delete multiple elements:

```python
numbers = [10, 20, 30, 40, 50]

del numbers[1:3]

print(numbers)
```

### clear()

Removes all elements but keeps the list object.

```python
numbers = [10, 20, 30]

numbers.clear()

print(numbers)  # []
```

## 8. Common List Methods

| Method | Purpose |
|---|---|
| `append(x)` | Adds one element at the end |
| `extend(iterable)` | Adds elements from an iterable |
| `insert(i, x)` | Inserts an element at an index |
| `remove(x)` | Removes the first matching value |
| `pop(i)` | Removes and returns an element |
| `clear()` | Removes all elements |
| `index(x)` | Returns the index of the first matching value |
| `count(x)` | Counts occurrences of a value |
| `sort()` | Sorts the original list |
| `reverse()` | Reverses the original list |
| `copy()` | Creates a shallow copy |

Examples:

```python
numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))  # 1
print(numbers.count(20))  # 2

numbers.reverse()
print(numbers)

numbers.sort()
print(numbers)

copied_numbers = numbers.copy()
print(copied_numbers)
```

## 9. Sorting Lists

### sort()

Sorts the original list in place.

```python
numbers = [40, 10, 30, 20]

numbers.sort()

print(numbers)
```

Output:

```text
[10, 20, 30, 40]
```

Descending order:

```python
numbers.sort(reverse=True)

print(numbers)
```

Output:

```text
[40, 30, 20, 10]
```

### sorted()

Returns a new sorted list without modifying the original list.

```python
numbers = [40, 10, 30, 20]

sorted_numbers = sorted(numbers)

print(sorted_numbers)
print(numbers)
```

Output:

```text
[10, 20, 30, 40]
[40, 10, 30, 20]
```

### Sorting Strings

```python
languages = ["Python", "Java", "C++", "JavaScript"]

print(sorted(languages))
```

### Sorting Using key

The `key` parameter allows you to define how elements should be compared.

```python
names = ["Alexander", "Sam", "Bhargavi", "John"]

names.sort(key=len)

print(names)
```

This sorts names by their length.

## 10. Iterating Through Lists

Iteration means accessing each element one at a time.

### Using a for loop

```python
skills = ["Python", "FastAPI", "SQL"]

for skill in skills:
    print(skill)
```

### Using a while loop

```python
numbers = [10, 20, 30]

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
```

### Using enumerate()

`enumerate()` provides both the index and the element.

```python
skills = ["Python", "FastAPI", "SQL"]

for index, skill in enumerate(skills):
    print(index, skill)
```

You can specify a starting index:

```python
for index, skill in enumerate(skills, start=1):
    print(index, skill)
```

### Using range() and len()

```python
numbers = [10, 20, 30]

for index in range(len(numbers)):
    print(numbers[index])
```

## 11. Checking Whether an Element Exists

Use the `in` and `not in` operators.

```python
skills = ["Python", "FastAPI", "SQL"]

print("Python" in skills)       # True
print("Java" in skills)         # False
print("Java" not in skills)     # True
```

This is useful when validating user input or checking whether a particular item exists.

## 12. List Concatenation and Repetition

### Concatenation

The `+` operator combines lists.

```python
backend = ["Python", "FastAPI"]
database = ["PostgreSQL", "MongoDB"]

technologies = backend + database

print(technologies)
```

### Repetition

The `*` operator repeats list elements.

```python
numbers = [1, 2, 3]

print(numbers * 3)
```

Output:

```text
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

## 13. List Comprehension

List comprehension provides a concise way to create a new list from an iterable.

Basic syntax:

```python
new_list = [expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

### List Comprehension with Conditions

Syntax:

```python
new_list = [expression for item in iterable if condition]
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

### List Comprehension with if-else

```python
numbers = [1, 2, 3, 4, 5]

results = [
    "Even" if number % 2 == 0 else "Odd"
    for number in numbers
]

print(results)
```

Output:

```text
['Odd', 'Even', 'Odd', 'Even', 'Odd']
```

### Nested List Comprehension

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened = [
    number
    for row in matrix
    for number in row
]

print(flattened)
```

Output:

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Use list comprehensions when the transformation is simple and readable. Use ordinary loops when the logic becomes complicated.

## 14. Nested Lists

A nested list is a list containing other lists.

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Accessing nested elements:

```python
print(matrix[0])     # [1, 2, 3]
print(matrix[0][1])  # 2
print(matrix[2][2])  # 9
```

Iterating through a nested list:

```python
for row in matrix:
    for value in row:
        print(value)
```

Nested lists are useful for representing:
- Matrices
- Tables
- Grids
- Structured datasets
- Hierarchical information

## 15. Copying Lists: Assignment vs Shallow Copy

This is an important concept because lists are mutable objects.

### Assignment Does Not Create a New List

```python
original = [10, 20, 30]

reference = original

reference[0] = 100

print(original)
print(reference)
```

Output:

```text
[100, 20, 30]
[100, 20, 30]
```

Both variables refer to the same list object.

### Shallow Copy

```python
original = [10, 20, 30]

copied = original.copy()

copied[0] = 100

print(original)
print(copied)
```

Output:

```text
[10, 20, 30]
[100, 20, 30]
```

A shallow copy creates a new outer list. However, nested mutable objects are still shared.

### Shallow Copy with Nested Lists

```python
original = [[1, 2], [3, 4]]

copied = original.copy()

copied[0][0] = 100

print(original)
print(copied)
```

Output:

```text
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

The nested list is shared between the two outer lists.

### Deep Copy

Use `copy.deepcopy()` when you need to copy nested mutable objects independently.

```python
import copy

original = [[1, 2], [3, 4]]

copied = copy.deepcopy(original)

copied[0][0] = 100

print(original)
print(copied)
```

Output:

```text
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

## 16. List Unpacking

Unpacking assigns list elements to individual variables.

```python
coordinates = [10, 20, 30]

x, y, z = coordinates

print(x)
print(y)
print(z)
```

### Extended Unpacking

Use `*` to collect remaining elements.

```python
numbers = [10, 20, 30, 40, 50]

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

The number of variables must match the number of elements unless extended unpacking is used.

## 17. Useful Built-in Functions for Lists

| Function | Purpose |
|---|---|
| `len(list)` | Returns the number of elements |
| `max(list)` | Returns the largest element |
| `min(list)` | Returns the smallest element |
| `sum(list)` | Returns the sum of numeric elements |
| `sorted(list)` | Returns a new sorted list |
| `any(list)` | Returns `True` if at least one element is truthy |
| `all(list)` | Returns `True` if every element is truthy |
| `enumerate(list)` | Provides index and value |
| `list(iterable)` | Converts an iterable into a list |

Example:

```python
scores = [75, 80, 90, 65, 95]

print(len(scores))
print(max(scores))
print(min(scores))
print(sum(scores))
print(sum(scores) / len(scores))
print(any(scores))
print(all(scores))
```

## 18. Common List Mistakes

### Mistake 1: Confusing append() and extend()

```python
numbers = [1, 2]

numbers.append([3, 4])

# Result: [1, 2, [3, 4]]
```

Use `extend()` when you want to add individual elements from another iterable.

### Mistake 2: Expecting sort() to Return a Sorted List

```python
numbers = [3, 1, 2]

result = numbers.sort()

print(result)  # None
print(numbers) # [1, 2, 3]
```

`sort()` modifies the original list and returns `None`. Use `sorted()` when you need a new sorted list.

### Mistake 3: Modifying a List While Iterating Over It

Avoid removing elements from a list while directly iterating over the same list.

Instead, create a filtered list:

```python
numbers = [1, 2, 3, 4, 5, 6]

numbers = [
    number
    for number in numbers
    if number % 2 != 0
]

print(numbers)
```

### Mistake 4: Using Mutable Default Arguments

Avoid:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

The same default list can be reused across function calls.

Use `None` instead:

```python
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
```

## 19. Time Complexity of Common List Operations

Let `n` represent the number of elements in a list.

| Operation | Typical time complexity |
|---|---:|
| Access by index | O(1) |
| Modify by index | O(1) |
| Append | O(1) amortized |
| Pop from end | O(1) |
| Insert at beginning | O(n) |
| Remove by value | O(n) |
| Search using `in` | O(n) |
| Find index | O(n) |
| Count occurrences | O(n) |
| Sort | O(n log n) |
| Copy a list | O(n) |
| Iterate through list | O(n) |

Important:

- Accessing an element by index is fast.
- Searching for a value requires checking elements.
- Inserting or removing at the beginning shifts other elements.
- Appending is generally efficient because Python lists are dynamic arrays.

## 20. Lists in AI and Backend Development

Lists are used extensively in Python applications.

### Example 1: Processing AI Predictions

```python
predictions = [
    {"label": "spam", "confidence": 0.95},
    {"label": "ham", "confidence": 0.88},
    {"label": "spam", "confidence": 0.72}
]

spam_predictions = [
    prediction
    for prediction in predictions
    if prediction["label"] == "spam"
]

print(spam_predictions)
```

### Example 2: Filtering Documents by Relevance

```python
documents = [
    {"content": "Python basics", "score": 0.92},
    {"content": "Java introduction", "score": 0.45},
    {"content": "Agentic AI concepts", "score": 0.87}
]

relevant_documents = [
    document
    for document in documents
    if document["score"] >= 0.80
]

print(relevant_documents)
```

### Example 3: Storing Agent Tools

```python
agent_tools = [
    "search_web",
    "retrieve_documents",
    "calculate",
    "send_email"
]

for tool in agent_tools:
    print(f"Available tool: {tool}")
```

### Example 4: Preparing Data for an API

```python
users = [
    {"id": 1, "name": "Ammu"},
    {"id": 2, "name": "John"},
    {"id": 3, "name": "Sarah"}
]

active_users = [
    user
    for user in users
    if user["id"] != 2
]

print(active_users)
```

Lists are commonly used to hold collections of records, predictions, retrieved documents, messages, and tool definitions.

---

## 21. Practice Exercises

Complete these exercises independently before moving to the next topic.

1. Create a list containing five programming languages. Print the first and last elements.
2. Create a list of ten numbers. Print only the even numbers.
3. Add three new elements to a list using `append()`, `extend()`, and `insert()`.
4. Remove a specific element using `remove()` and remove the last element using `pop()`.
5. Find the largest, smallest, and average values in a list of numbers.
6. Reverse a list without using the `reverse()` method.
7. Sort a list in ascending and descending order.
8. Create a new list containing the squares of numbers from 1 to 20 using list comprehension.
9. Given a list of student marks, create a new list containing only marks greater than or equal to 50.
10. Given a nested list representing a matrix, print every element using nested loops.
11. Create a copy of a list and demonstrate the difference between assignment and shallow copying.
12. Given a list of dictionaries containing AI predictions, filter predictions with confidence greater than or equal to 0.80.
13. Given a list of document dictionaries, return only documents with a relevance score greater than 0.75.
14. Remove duplicate values from a list while preserving the original order.
15. Flatten a two-dimensional list into a one-dimensional list.

## 22. Key Takeaways

- Lists are ordered, mutable collections.
- List indexing starts at zero.
- Negative indexing accesses elements from the end.
- Slicing extracts portions of a list.
- `append()` adds one object; `extend()` adds elements from an iterable.
- `remove()`, `pop()`, `del`, and `clear()` perform different removal operations.
- `sort()` modifies the original list; `sorted()` returns a new list.
- List comprehension creates lists concisely.
- Assignment creates another reference, not a copy.
- Shallow copies do not independently copy nested mutable objects.
- Deep copies recursively copy nested objects.
- Lists are fundamental for processing collections of data in backend applications, machine learning, and Agentic AI systems.