# Python Sets – Complete Notes

## 1. What is a Set?

A set is a built-in Python data structure used to store unique elements.

Example:

```python
numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))
```

Output:

```text
{10, 20, 30, 40}
<class 'set'>
```

A set automatically removes duplicate values.

```python
numbers = {10, 20, 10, 30, 20}

print(numbers)
```

Output:

```text
{10, 20, 30}
```

The displayed order is not guaranteed.

## 2. Characteristics of Sets

A Python set has these characteristics:

1. **Unique elements:** Duplicate values are automatically removed.
2. **Unordered:** Sets do not guarantee a fixed element order.
3. **Mutable:** You can add and remove elements.
4. **No indexing:** You cannot access elements using positions such as `set[0]`.
5. **Iterable:** You can loop through elements.
6. **Hashable elements:** Elements must be hashable, such as strings, integers and suitable tuples.
7. **Mixed data types:** A set can contain different hashable data types.

Example:

```python
data = {10, "Python", 3.14, True}

print(data)
```

Do not depend on the order in which elements are displayed.

## 3. Creating Sets

### Set with elements

```python
numbers = {10, 20, 30, 40}
```

### Empty set

Use `set()` to create an empty set.

```python
empty_set = set()
```

Important:

```python
empty_dict = {}

print(type(empty_dict))  # dict
```

An empty `{}` creates a dictionary, not a set.

### Creating a set using set()

```python
numbers = set([10, 20, 20, 30])

print(numbers)
```

You can create sets from other iterables:

```python
characters = set("hello")
numbers = set((10, 20, 30))
```

## 4. Accessing Set Elements

Sets do not support indexing or slicing.

Incorrect:

```python
numbers = {10, 20, 30}

print(numbers[0])  # TypeError
```

To access elements, use a loop:

```python
for number in numbers:
    print(number)
```

To check whether an element exists, use `in`:

```python
print(20 in numbers)
print(50 in numbers)
```

## 5. Adding Elements

### add()

Adds one element.

```python
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)
```

Adding an existing element does not create a duplicate.

```python
numbers.add(20)

print(numbers)
```

### update()

Adds multiple elements from an iterable.

```python
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)
```

You can provide multiple iterables:

```python
numbers.update([60, 70], (80, 90))
```

## 6. Removing Elements

### remove()

Removes an element.

```python
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)
```

If the element does not exist, `remove()` raises a `KeyError`.

### discard()

Removes an element if it exists.

```python
numbers.discard(100)
```

No error occurs if the element is missing.

### pop()

Removes and returns an arbitrary element.

```python
numbers = {10, 20, 30}

removed = numbers.pop()

print(removed)
print(numbers)
```

Do not assume which element `pop()` will remove.

### clear()

Removes all elements.

```python
numbers.clear()

print(numbers)
```

### Summary

| Method | Purpose |
|---|---|
| `add(x)` | Adds one element |
| `update(iterable)` | Adds multiple elements |
| `remove(x)` | Removes element; raises KeyError if missing |
| `discard(x)` | Removes element if present |
| `pop()` | Removes and returns an arbitrary element |
| `clear()` | Removes all elements |

## 7. Set Union

Union combines all unique elements from two or more sets.

Operator: `|`

Method: `union()`

```python
python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya", "David"}

result = python_students | java_students

print(result)
```

The result contains every unique student from both sets.

Using the method:

```python
result = python_students.union(java_students)
```

## 8. Set Intersection

Intersection returns elements common to both sets.

Operator: `&`

Method: `intersection()`

```python
python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya", "John"}

result = python_students & java_students

print(result)
```

Result:

```text
{'Ravi', 'John'}
```

Using the method:

```python
result = python_students.intersection(java_students)
```

## 9. Set Difference

Difference returns elements that exist in the first set but not in the second.

Operator: `-`

Method: `difference()`

```python
python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya"}

result = python_students - java_students

print(result)
```

Result:

```text
{'Ammu', 'John'}
```

Important: Difference is directional.

```python
print(java_students - python_students)
```

This produces elements in the Java set that are absent from the Python set.

## 10. Symmetric Difference

Symmetric difference returns elements that appear in either set, but not in both.

Operator: `^`

Method: `symmetric_difference()`

```python
python_students = {"Ammu", "Ravi", "John"}
java_students = {"Ravi", "Priya"}

result = python_students ^ java_students

print(result)
```

Result:

```text
{'Ammu', 'John', 'Priya'}
```

The common element `Ravi` is excluded.

## 11. Set Comparison

### issubset()

Checks whether every element of one set exists in another set.

```python
small = {10, 20}
large = {10, 20, 30, 40}

print(small.issubset(large))  # True
```

Operator: `<=`

```python
print(small <= large)
```

### issuperset()

Checks whether a set contains every element of another set.

```python
large = {10, 20, 30, 40}
small = {10, 20}

print(large.issuperset(small))  # True
```

Operator: `>=`

### isdisjoint()

Checks whether two sets have no common elements.

```python
first = {10, 20}
second = {30, 40}

print(first.isdisjoint(second))  # True
```

### Equality

Two sets are equal if they contain the same elements, regardless of order.

```python
print({10, 20, 30} == {30, 20, 10})  # True
```

## 12. Updating Sets Using Set Operations

Set operations can either return a new set or modify an existing one.

| Method | Effect |
|---|---|
| `union()` | Returns a new union set |
| `update()` | Adds elements to the existing set |
| `intersection()` | Returns a new intersection set |
| `intersection_update()` | Keeps only common elements in the existing set |
| `difference()` | Returns a new difference set |
| `difference_update()` | Removes elements found in the other set |
| `symmetric_difference()` | Returns a new symmetric difference set |
| `symmetric_difference_update()` | Updates the existing set |

Example:

```python
first = {10, 20, 30}
second = {20, 30, 40}

first.intersection_update(second)

print(first)
```

Result:

```text
{20, 30}
```

## 13. Set Comprehension

Set comprehension creates a set using a compact expression.

Syntax:

```python
{expression for item in iterable}
```

### Example 1: Squares

```python
squares = {
    number ** 2
    for number in range(1, 6)
}

print(squares)
```

### Example 2: Even numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)
```

### Example 3: Unique lowercase words

```python
words = ["AI", "Python", "AI", "JAVA"]

unique_words = {
    word.lower()
    for word in words
}

print(unique_words)
```

## 14. Removing Duplicates from a List

Sets are frequently used to remove duplicate values.

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers)

print(unique_numbers)
```

Important: Converting to a set does not preserve the original list order.

### Preserve insertion order

Use `dict.fromkeys()` when you need to remove duplicates while keeping the original order.

```python
numbers = [10, 20, 10, 30, 20, 40]

unique_numbers = list(dict.fromkeys(numbers))

print(unique_numbers)
```

Output:

```text
[10, 20, 30, 40]
```

## 15. Frozenset

A frozenset is an immutable version of a set.

```python
permissions = frozenset({"read", "write", "execute"})

print(permissions)
```

You cannot add or remove elements from a frozenset.

```python
# permissions.add("delete")  # AttributeError
```

### Why use frozenset?

- When a fixed collection of unique elements is needed.
- When a set must be used as a dictionary key.
- When a set must be stored inside another set.
- When you want to prevent accidental modification.

Example:

```python
permissions = frozenset({"read", "write"})

roles = {
    permissions: "admin"
}

print(roles[permissions])
```

## 16. Set Restrictions

Set elements must be hashable.

Valid:

```python
data = {10, "Python", (1, 2)}
```

Invalid:

```python
data = {[1, 2], [3, 4]}
```

This raises a `TypeError` because lists are mutable and unhashable.

A tuple is allowed only if all its elements are hashable.

## 17. Sets in AI and Agentic AI

Sets are useful when an application needs to manage unique items or compare collections.

### Example 1: Removing duplicate tools

```python
tools = [
    "search",
    "calculator",
    "search",
    "weather",
    "calculator"
]

unique_tools = set(tools)

print(unique_tools)
```

### Example 2: Permission checking

```python
allowed_permissions = {"read", "search", "summarise"}

requested_permissions = {"read", "search"}

if requested_permissions.issubset(allowed_permissions):
    print("Permission granted")
else:
    print("Permission denied")
```

### Example 3: Comparing available and required tools

```python
available_tools = {"search", "calculator", "weather"}

required_tools = {"search", "weather"}

missing_tools = required_tools - available_tools

print("Missing tools:", missing_tools)
```

### Example 4: Tracking retrieved document IDs

```python
retrieved_documents = {
    "doc_101",
    "doc_102",
    "doc_103"
}

new_documents = {
    "doc_102",
    "doc_104"
}

unique_documents = retrieved_documents | new_documents

print(unique_documents)
```

### Example 5: Finding common skills

```python
python_skills = {"Python", "NumPy", "Pandas", "FastAPI"}
ai_skills = {"Python", "PyTorch", "Pandas", "Transformers"}

common_skills = python_skills & ai_skills

print(common_skills)
```

## 18. Set vs List vs Tuple vs Dictionary

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `{}` | `{key: value}` |
| Ordered | Yes | Yes | No guaranteed order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Allowed | Allowed | Not allowed | Keys unique |
| Indexing | Yes | Yes | No | By key |
| Main purpose | Dynamic collection | Fixed collection | Unique elements | Key-value mapping |

### When should you use each?

**List:** When data needs to be changed, ordered or indexed.

**Tuple:** When data represents a fixed collection.

**Set:** When you need unique elements or mathematical set operations.

**Dictionary:** When you need to map keys to values.

## 19. Set Time Complexity

For typical Python sets:

| Operation | Average time complexity |
|---|---|
| Add | O(1) |
| Remove | O(1) |
| Membership (`in`) | O(1) |
| Discard | O(1) |
| Union | O(n + m) |
| Intersection | O(min(n, m)) typical |
| Difference | O(n) typical |
| Iteration | O(n) |
| Copy | O(n) |

These are typical average-case complexities. Worst-case performance can be different.

## 20. Common Mistakes

### Mistake 1: Creating an empty set using {}

```python
data = {}

print(type(data))  # dict
```

Correct:

```python
data = set()

print(type(data))  # set
```

### Mistake 2: Trying to access elements by index

```python
numbers = {10, 20, 30}

# numbers[0]  # TypeError
```

Use a loop or convert to a list if positional access is required.

### Mistake 3: Using a list as a set element

```python
# data = {[1, 2], [3, 4]}  # TypeError
```

Use tuples when the values are hashable.

### Mistake 4: Assuming remove() and discard() behave identically

```python
numbers = {10, 20}

numbers.discard(100)  # Safe
# numbers.remove(100)  # KeyError
```

### Mistake 5: Assuming set order is stable

```python
numbers = {40, 10, 30, 20}

print(numbers)
```

Never depend on the displayed order. Sort the elements if a predictable order is required:

```python
print(sorted(numbers))
```

Remember that `sorted()` returns a list.

## 21. Interview Questions

1. What is a set in Python?
2. Why does a set remove duplicate values?
3. Are sets ordered?
4. Are sets mutable?
5. Can sets contain lists?
6. Why do sets not support indexing?
7. What is the difference between `add()` and `update()`?
8. What is the difference between `remove()` and `discard()`?
9. What does `pop()` do in a set?
10. Explain union, intersection and difference.
11. What is symmetric difference?
12. What is the difference between subset and superset?
13. What does `isdisjoint()` check?
14. What is set comprehension?
15. What is a frozenset?
16. What is the difference between a set and a frozenset?
17. How can you remove duplicates from a list?
18. How can you preserve list order while removing duplicates?
19. What is the average membership lookup complexity?
20. How can sets be used for permission checking in an AI agent?

## 22. Key Takeaways

- A set stores unique elements.
- Sets are mutable and unordered.
- Sets do not support indexing or slicing.
- Use `set()` to create an empty set.
- Use `add()` for one element and `update()` for multiple elements.
- `remove()` raises an error if an element is missing; `discard()` does not.
- Union combines unique elements.
- Intersection finds common elements.
- Difference finds elements present only in the first set.
- Symmetric difference finds elements present in exactly one set.
- Frozensets are immutable.
- Sets are useful for deduplication, permission checking and comparing collections.

## 23. Completion Checklist

- [ ] I can create empty and non-empty sets.
- [ ] I understand why sets do not allow duplicates.
- [ ] I understand why sets do not support indexing.
- [ ] I can add and remove elements.
- [ ] I understand `remove()` versus `discard()`.
- [ ] I can perform union operations.
- [ ] I can perform intersection operations.
- [ ] I can perform difference operations.
- [ ] I can perform symmetric difference operations.
- [ ] I understand subsets and supersets.
- [ ] I can write set comprehensions.
- [ ] I understand frozensets.
- [ ] I can remove duplicates from a list.
- [ ] I can explain set applications in AI agents.