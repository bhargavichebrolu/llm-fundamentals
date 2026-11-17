# Python Loops – Complete Notes

## 1. Introduction

Loops allow a program to execute a block of code repeatedly.

They are used for:
- Processing collections.
- Iterating through datasets.
- Reading files.
- Processing API responses.
- Handling conversation messages.
- Repeated agent execution.

Python has two main loop types:

1. `for` loop
2. `while` loop

## 2. For Loop

A for loop iterates over an iterable, one element at a time.

Syntax:

```python
for variable in iterable:
    # Code
```

Example:

```python
languages = ["Python", "Java", "C++"]

for language in languages:
    print(language)
```

The loop processes every element in the list.

## 3. Iterating Through Different Data Types

### List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

### Tuple

```python
coordinates = (10, 20, 30)

for coordinate in coordinates:
    print(coordinate)
```

### Set

```python
languages = {"Python", "Java", "C++"}

for language in languages:
    print(language)
```

Set iteration order is not guaranteed.

### Dictionary

```python
student = {
    "name": "Ammu",
    "age": 24
}

for key, value in student.items():
    print(key, value)
```

### String

```python
word = "Python"

for character in word:
    print(character)
```

## 4. range() Function

`range()` generates a sequence of integers.

Three forms:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

### range(stop)

```python
for i in range(5):
    print(i)
```

Output: 0, 1, 2, 3, 4.

### range(start, stop)

```python
for i in range(2, 6):
    print(i)
```

Output: 2, 3, 4, 5.

### range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)
```

Output: 0, 2, 4, 6, 8.

The stop value is excluded.

## 5. enumerate()

`enumerate()` provides both an index and an element during iteration.

```python
languages = ["Python", "Java", "C++"]

for index, language in enumerate(languages):
    print(index, language)
```

Starting at 1:

```python
for index, language in enumerate(languages, start=1):
    print(index, language)
```

Use it when both position and value are required.

## 6. while Loop

A while loop executes repeatedly as long as its condition remains True.

Syntax:

```python
while condition:
    # Code
```

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

The variable changes on each iteration until the condition becomes False.

## 7. Infinite Loops

An infinite loop occurs when a loop's condition never becomes False.

Incorrect:

```python
count = 1

while count <= 5:
    print(count)
```

The count never changes.

Correct:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Always ensure a while loop has a valid termination condition or an explicit exit mechanism.

## 8. for vs while

| Feature | for | while |
|---|---|---|
| Main use | Iterating through an iterable | Repeating while a condition is true |
| Typical example | Processing a list | Retry loop |
| Iterations | Often determined by iterable | Determined by condition |
| Infinite loop risk | Generally lower | Higher if poorly controlled |

## 9. Nested Loops

A nested loop is a loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

The inner loop completes its iterations for each iteration of the outer loop, unless interrupted.

### Multiplication table

```python
for i in range(1, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
```

## 10. Looping Through Collections

### Find the sum

```python
numbers = [10, 20, 30]
total = 0

for number in numbers:
    total += number

print(total)
```

### Count matching values

```python
numbers = [10, 20, 10, 30, 10]
count = 0

for number in numbers:
    if number == 10:
        count += 1

print(count)
```

### Find the largest value without max()

```python
numbers = [10, 50, 20, 80, 30]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)
```

## 11. Looping in AI Applications

### Processing documents

```python
documents = [
    "Python is useful",
    "AI uses data",
    "Agents use tools"
]

for document in documents:
    print("Processing:", document)
```

### Processing conversation messages

```python
messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi"}
]

for message in messages:
    print(message["role"], message["content"])
```

### Agent execution loop

```python
task_completed = False
attempts = 0

while not task_completed and attempts < 3:
    attempts += 1
    print("Attempt:", attempts)

    if attempts == 2:
        task_completed = True

print("Completed:", task_completed)
```

## 12. Common Mistakes

1. Forgetting to update the while-loop counter.
2. Using the wrong range stop value.
3. Incorrect indentation.
4. Modifying a collection while iterating over it.
5. Confusing an iterable with an index.
6. Using nested loops when a more efficient data structure could solve the problem.
7. Creating loops without a termination condition.

## 13. Time Complexity

| Operation | Typical complexity |
|---|---|
| Iterating through n elements | O(n) |
| Nested loops, each over n elements | O(n²) |
| Three nested loops, each over n elements | O(n³) |
| Iterating through a matrix with r rows and c columns | O(r × c) |

Complexity depends on how many times the loop body executes.

## 14. Interview Questions

1. What is a loop?
2. Explain for and while loops.
3. What does range() do?
4. What is the difference between range(5) and range(1, 5)?
5. What does enumerate() return?
6. What is an infinite loop?
7. How do you prevent an infinite while loop?
8. What is a nested loop?
9. What is the time complexity of two nested loops?
10. How do loops process datasets?
11. How can you find the maximum value without max()?
12. How are loops used in AI agent execution?

## 15. Completion Checklist

- [ ] I can write for loops.
- [ ] I can write while loops.
- [ ] I can iterate through lists, tuples, sets and dictionaries.
- [ ] I understand range().
- [ ] I can use enumerate().
- [ ] I can write nested loops.
- [ ] I can calculate sums and counts using loops.
- [ ] I can find a maximum value using a loop.
- [ ] I understand loop termination.
- [ ] I can explain loop use in AI applications.