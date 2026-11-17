# Python Loop Control – break, continue, pass and Nested Loops

## 1. Introduction

Python provides control statements that change how loops execute.

The three important statements are:

- `break`
- `continue`
- `pass`

Nested loops allow one loop to execute inside another.

## 2. break Statement

`break` immediately terminates the nearest enclosing loop.

```python
for number in range(1, 11):
    if number == 5:
        break

    print(number)
```

Output:

```text
1
2
3
4
```

### Practical use

Stop searching when the first match is found.

```python
users = ["Ravi", "John", "Ammu", "David"]

for user in users:
    if user == "Ammu":
        print("User found")
        break
```

## 3. continue Statement

`continue` skips the remaining statements in the current iteration and moves to the next iteration.

```python
for number in range(1, 6):
    if number == 3:
        continue

    print(number)
```

Output:

```text
1
2
4
5
```

### Practical use

Skip invalid or empty documents.

```python
documents = [
    "Python tutorial",
    "",
    "AI engineering",
    "Machine learning"
]

for document in documents:
    if not document:
        continue

    print(document)
```

## 4. pass Statement

`pass` does nothing. It acts as a placeholder where Python requires a statement.

```python
for number in range(5):
    if number == 3:
        pass

    print(number)
```

It does not skip an iteration or terminate a loop.

### Placeholder function

```python
def execute_agent():
    pass
```

This lets you define the function structure before implementing its behaviour.

## 5. Difference Between break, continue and pass

| Statement | Behaviour |
|---|---|
| break | Terminates the nearest enclosing loop |
| continue | Skips the current iteration |
| pass | Does nothing |

## 6. Nested for Loops

A nested loop is a loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

Output:

```text
1 1
1 2
2 1
2 2
3 1
3 2
```

The inner loop completes its iterations for each outer-loop iteration unless interrupted.

## 7. Nested while Loops

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1
```

Remember to update both counters appropriately.

## 8. break in Nested Loops

A `break` statement terminates only the nearest enclosing loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break

        print(i, j)
```

The inner loop stops when `j == 2`, but the outer loop continues.

To stop both loops, use a separate condition or return from a function when appropriate.

## 9. AI Application Examples

### Stop after finding a relevant document

```python
documents = [
    "Cooking recipes",
    "Python programming guide",
    "Travel information"
]

for document in documents:
    if "Python" in document:
        print("Relevant document:", document)
        break
```

### Skip empty documents

```python
for document in documents:
    if not document.strip():
        continue

    print("Processing:", document)
```

### Bounded agent retry

```python
attempts = 0
max_attempts = 3
task_completed = False

while attempts < max_attempts:
    attempts += 1

    if attempts == 2:
        task_completed = True
        break

if task_completed:
    print("Task successful")
else:
    print("Task failed")
```

Production systems also need exception handling, timeouts and retry policies.

## 10. Common Mistakes

1. Assuming `break` stops every enclosing loop.
2. Assuming `continue` terminates a loop.
3. Assuming `pass` skips an iteration.
4. Forgetting to update counters in nested while loops.
5. Using deeply nested loops when a more efficient approach exists.
6. Failing to limit retry loops.

## 11. Interview Questions

1. What does break do?
2. What does continue do?
3. What does pass do?
4. What is the difference between the three?
5. What is a nested loop?
6. What happens when break is used in an inner loop?
7. How can you stop both nested loops?
8. How can continue be used to filter data?
9. Why is pass useful during development?
10. How can break be used in an agent retry process?

## 12. Completion Checklist

- [ ] I understand break.
- [ ] I understand continue.
- [ ] I understand pass.
- [ ] I can explain their differences.
- [ ] I can write nested for loops.
- [ ] I can write nested while loops.
- [ ] I understand break in nested loops.
- [ ] I can build a bounded retry loop.
- [ ] I can use continue to skip invalid data.