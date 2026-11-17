# Python Tuples – Complete Notes

## 1. What is a Tuple?

A tuple is a built-in Python data structure used to store multiple values in a single variable.

A tuple is:
- Ordered: elements maintain their insertion order.
- Immutable: elements cannot be changed after creation.
- Allows duplicates: the same value can appear multiple times.
- Allows different data types: integers, strings, floats, booleans, and other objects.
- Iterable: you can loop through its elements.
- Indexable: elements can be accessed using indexes.

### Example

```python
student = ("Ammu", 24, "Artificial Intelligence")

print(student)
print(type(student))
```

Output:

```text
('Ammu', 24, 'Artificial Intelligence')
<class 'tuple'>
```

## 2. Creating Tuples

### Empty tuple

```python
empty_tuple = ()
```

### Tuple with multiple elements

```python
numbers = (10, 20, 30, 40)
```

### Tuple without parentheses

Python also recognises comma-separated values as a tuple.

```python
numbers = 10, 20, 30
print(type(numbers))
```

### Single-element tuple

A comma is compulsory when creating a tuple with one element.

```python
single = (10,)
print(type(single))
```

Without the comma:

```python
single = (10)
print(type(single))
```

This is an integer, not a tuple.

### Tuple with different data types

```python
details = ("Python", 3.13, 100, True)
```

### Tuple constructor

You can convert an iterable into a tuple using `tuple()`.

```python
numbers = tuple([10, 20, 30])
characters = tuple("AI")
```

## 3. Accessing Tuple Elements

Tuples use zero-based indexing.

```python
languages = ("Python", "Java", "C++", "JavaScript")

print(languages[0])   # Python
print(languages[1])   # Java
print(languages[-1])  # JavaScript
print(languages[-2])  # C++
```

- Positive indexing starts at 0.
- Negative indexing starts from -1 at the end.

### Index out of range

```python
languages = ("Python", "Java")

print(languages[5])  # IndexError
```

An index must exist in the tuple.

## 4. Tuple Slicing

Slicing extracts a portion of a tuple.

Syntax:

```python
tuple_name[start:stop:step]
```

The stop index is excluded.

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[2:])    # (30, 40, 50, 60)
print(numbers[:])     # Entire tuple
print(numbers[::2])   # (10, 30, 50)
print(numbers[::-1])  # Reversed tuple
```

Slicing creates a new tuple. It does not modify the original tuple.

## 5. Tuple Immutability

Immutability means that a tuple's elements cannot be replaced, added, or removed after creation.

```python
numbers = (10, 20, 30)

numbers[0] = 100
```

This raises:

```text
TypeError: 'tuple' object does not support item assignment
```

### Why is immutability useful?

- Protects fixed configuration values.
- Prevents accidental modification.
- Makes data more predictable.
- Useful for fixed records and coordinates.
- Can be used as a dictionary key when all contained elements are hashable.

### Important: A tuple can contain a mutable object

```python
data = (10, 20, [30, 40])

data[2].append(50)

print(data)
```

Output:

```text
(10, 20, [30, 40, 50])
```

The tuple still contains the same list object, but the list itself can be modified.

You cannot replace the list:

```python
data[2] = [100, 200]  # TypeError
```

**Key distinction:** Tuple immutability prevents changing the references stored in its positions. It does not automatically make every object inside it immutable.

## 6. Tuple Methods

Tuples have only two main built-in methods.

### count()

Returns the number of times a value occurs.

```python
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))  # 3
print(numbers.count(20))  # 1
```

### index()

Returns the index of the first occurrence of a value.

```python
languages = ("Python", "Java", "Python", "C++")

print(languages.index("Python"))  # 0
print(languages.index("C++"))     # 3
```

If the value does not exist, `index()` raises a `ValueError`.

```python
languages.index("Ruby")  # ValueError
```

## 7. Built-in Functions Used with Tuples

Although tuples have only two methods, Python provides several built-in functions that work with them.

```python
numbers = (10, 20, 30, 40)

print(len(numbers))  # 4
print(max(numbers))  # 40
print(min(numbers))  # 10
print(sum(numbers))  # 100
print(sorted(numbers))  # [10, 20, 30, 40]
```

Important: `sorted()` returns a list, not a tuple.

To get a tuple:

```python
sorted_tuple = tuple(sorted(numbers))
```

Other useful functions:

```python
print(any((False, True, False)))  # True
print(all((True, True, True)))    # True
```

- `any()` returns True if at least one element is truthy.
- `all()` returns True if every element is truthy.

## 8. Tuple Unpacking

Unpacking assigns tuple elements to individual variables.

```python
student = ("Ammu", 24, "AI")

name, age, course = student

print(name)
print(age)
print(course)
```

The number of variables must match the number of elements unless extended unpacking is used.

### Extended unpacking using *

```python
numbers = (10, 20, 30, 40, 50)

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

Notice that the variable assigned using `*` receives a list.

### Ignoring values

```python
student = ("Ammu", 24, "AI")

name, _, course = student
```

The underscore is a naming convention indicating that the value is not needed.

## 9. Tuple Operations

### Concatenation

Combines two tuples.

```python
first = (10, 20)
second = (30, 40)

result = first + second

print(result)
```

Output:

```text
(10, 20, 30, 40)
```

### Repetition

```python
numbers = (1, 2)

print(numbers * 3)
```

Output:

```text
(1, 2, 1, 2, 1, 2)
```

### Membership

```python
languages = ("Python", "Java", "C++")

print("Python" in languages)      # True
print("JavaScript" not in languages)  # True
```

### Comparison

Tuples can be compared lexicographically.

```python
print((1, 2, 3) == (1, 2, 3))  # True
print((1, 2) < (1, 3))         # True
```

Comparison proceeds element by element until a difference is found.

## 10. Nested Tuples

A tuple can contain other tuples.

```python
students = (
    ("Ammu", 85),
    ("Ravi", 90),
    ("John", 78)
)

print(students[0])
print(students[0][0])  # Ammu
print(students[1][1])  # 90
```

Nested tuples are useful for representing structured records.

## 11. Converting Between Lists and Tuples

### List to tuple

```python
numbers_list = [10, 20, 30]

numbers_tuple = tuple(numbers_list)

print(numbers_tuple)
```

### Tuple to list

```python
numbers_tuple = (10, 20, 30)

numbers_list = list(numbers_tuple)

numbers_list.append(40)

print(numbers_list)
```

Use this approach when you need to modify tuple data:

1. Convert the tuple into a list.
2. Modify the list.
3. Convert it back into a tuple if required.

## 12. Tuple as a Dictionary Key

A tuple can be used as a dictionary key if all its elements are hashable.

```python
locations = {
    (51.5072, -0.1276): "London",
    (40.7128, -74.0060): "New York"
}

print(locations[(51.5072, -0.1276)])
```

A list cannot be used as a dictionary key because lists are mutable and unhashable.

A tuple containing a list is also unhashable.

## 13. Tuple vs List

| Feature | Tuple | List |
|---|---|---|
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |
| Ordered | Yes | Yes |
| Mutable | No | Yes |
| Duplicates | Allowed | Allowed |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Methods | Two main methods | Many methods |
| Dictionary key | If all elements are hashable | No |
| Typical use | Fixed data | Changeable data |

### When should you use a tuple?

Use a tuple when:
- The data represents a fixed record.
- Values should not be reassigned.
- You need a hashable collection of values.
- You are returning multiple values from a function.
- You want to represent coordinates or fixed configuration.

### When should you use a list?

Use a list when:
- You need to add or remove elements.
- You need to update values.
- The collection changes during execution.
- You are managing dynamic data.

## 14. Tuples in AI and Agentic AI

Tuples are useful when an AI application needs to represent fixed groups of values.

### Example 1: Model configuration

```python
model_config = ("gpt-model", 0.7, 1000)
```

This could represent:
- Model name
- Temperature
- Maximum output tokens

### Example 2: Coordinates

```python
location = (51.5072, -0.1276)
```

Represents latitude and longitude.

### Example 3: Tool result

```python
tool_result = ("success", "Weather retrieved", 18.5)

status, message, temperature = tool_result
```

### Example 4: Agent execution result

```python
def execute_agent():
    return ("completed", "Task finished", 3)

status, message, steps = execute_agent()
```

A tuple can return multiple values from a function.

For more complex application data, dictionaries or typed models may be clearer than positional tuples.

## 15. Common Mistakes

### Mistake 1: Missing comma in a single-element tuple

```python
value = (10)
print(type(value))  # int
```

Correct:

```python
value = (10,)
print(type(value))  # tuple
```

### Mistake 2: Trying to modify a tuple

```python
numbers = (1, 2, 3)
numbers[0] = 100  # TypeError
```

Convert to a list if modification is required.

### Mistake 3: Confusing index() and count()

```python
numbers = (10, 20, 10)

print(numbers.index(10))  # 0: first position
print(numbers.count(10))  # 2: number of occurrences
```

### Mistake 4: Assuming sorted() returns a tuple

```python
numbers = (30, 10, 20)

result = sorted(numbers)

print(type(result))  # list
```

### Mistake 5: Incorrect unpacking

```python
numbers = (10, 20, 30)

a, b = numbers  # ValueError
```

Use the correct number of variables or extended unpacking.

## 16. Time Complexity

For a tuple containing n elements:

| Operation | Typical time complexity |
|---|---|
| Index access | O(1) |
| Length | O(1) |
| Count | O(n) |
| Index search | O(n) |
| Membership (`in`) | O(n) |
| Iteration | O(n) |
| Concatenation | O(n + m) |
| Slicing of k elements | O(k) |
| Sorting | O(n log n) |

These are typical Python tuple operation complexities.

## 17. Interview Questions

1. What is a tuple in Python?
2. What is the difference between a list and a tuple?
3. Why are tuples immutable?
4. Can a tuple contain duplicate values?
5. Can a tuple contain different data types?
6. How do you create a single-element tuple?
7. What happens if you try to modify a tuple?
8. What is tuple unpacking?
9. What does `*` do in tuple unpacking?
10. What is the difference between `count()` and `index()`?
11. Can tuples be used as dictionary keys?
12. Can a tuple contain a list?
13. Is a tuple containing a list hashable?
14. What does `sorted()` return when given a tuple?
15. How can you convert a tuple into a list?
16. How can a function return multiple values using a tuple?

## 18. Key Takeaways

- A tuple is an ordered, immutable collection.
- Tuples allow duplicate values and mixed data types.
- Indexing and slicing work similarly to lists.
- Tuples have two main methods: `count()` and `index()`.
- A single-element tuple requires a trailing comma.
- Tuple unpacking assigns elements to variables.
- `sorted()` returns a list.
- A tuple can be a dictionary key only when all its elements are hashable.
- A tuple can contain mutable objects, but its element references cannot be reassigned.
- Choose tuples for fixed data and lists for dynamic data.

## 19. Completion Checklist

- [ ] I can create tuples.
- [ ] I understand indexing and negative indexing.
- [ ] I can slice tuples.
- [ ] I understand immutability.
- [ ] I know the difference between `count()` and `index()`.
- [ ] I can use built-in functions with tuples.
- [ ] I can unpack tuples.
- [ ] I understand nested tuples.
- [ ] I can convert between lists and tuples.
- [ ] I understand when to use tuples in AI applications.
- [ ] I can explain tuple vs list in an interview.