# Recursion in Python

## 1. What Is Recursion?

Recursion is a programming technique in which a function calls itself to solve a problem.

Instead of solving the entire problem in one step, a recursive function breaks it into smaller versions of the same problem.

Each recursive call works towards a condition that allows the function to stop.

**Example:**

```python
def countdown(number):
    if number == 0:
        print("Finished")
        return

    print(number)
    countdown(number - 1)


countdown(5)
```

Output:

```text
5
4
3
2
1
Finished
```

The function calls itself with a smaller number until the number reaches zero.

---

## 2. The Two Essential Parts of Recursion

Every correctly designed recursive function needs two essential components.

### 2.1 Base Case

The base case defines the condition at which recursion stops.

Without a base case, the function continues calling itself until Python raises a `RecursionError`.

```python
if number == 0:
    return
```

### 2.2 Recursive Case

The recursive case is where the function calls itself with a smaller or simpler input.

```python
countdown(number - 1)
```

A recursive function must make progress towards its base case.

**Remember:**

- Base case = when to stop.
- Recursive case = how to continue.
- Progress = how each call moves towards stopping.

---

## 3. How Recursion Executes

Consider:

```python
def countdown(number):
    if number == 0:
        print("Finished")
        return

    print(number)
    countdown(number - 1)


countdown(3)
```

Execution:

1. `countdown(3)` prints `3` and calls `countdown(2)`.
2. `countdown(2)` prints `2` and calls `countdown(1)`.
3. `countdown(1)` prints `1` and calls `countdown(0)`.
4. `countdown(0)` reaches the base case and prints `Finished`.
5. The recursive calls return, completing the function.

The calls are nested. Python must complete the deepest call before the earlier calls can finish.

---

## 4. The Call Stack

The call stack is the memory structure Python uses to keep track of active function calls.

When a function calls another function, Python creates a new stack frame containing information such as local variables and where execution should resume.

Recursive calls create multiple stack frames.

For example:

```python
def calculate(number):
    if number == 0:
        return 0

    return number + calculate(number - 1)


print(calculate(3))
```

The calls are:

```text
calculate(3)
    calculate(2)
        calculate(1)
            calculate(0)
```

When the base case returns, execution moves back through the pending calls:

```text
calculate(0) returns 0
calculate(1) returns 1 + 0 = 1
calculate(2) returns 2 + 1 = 3
calculate(3) returns 3 + 3 = 6
```

Output:

```text
6
```

This process is called stack unwinding.

---

## 5. Recursion vs Iteration

Iteration uses loops such as `for` and `while`.

Recursion uses functions that call themselves.

### Iterative example

```python
def factorial_iterative(number):
    result = 1

    for value in range(1, number + 1):
        result *= value

    return result


print(factorial_iterative(5))
```

### Recursive example

```python
def factorial_recursive(number):
    if number == 0 or number == 1:
        return 1

    return number * factorial_recursive(number - 1)


print(factorial_recursive(5))
```

Both produce:

```text
120
```

| Feature | Recursion | Iteration |
|---|---|---|
| Structure | Function calls itself | Uses loops |
| Stopping condition | Base case | Loop condition |
| Memory | Uses call stack frames | Usually uses less call-stack memory |
| Performance | Function-call overhead | Usually faster for simple repetition |
| Readability | Useful for recursive structures | Useful for straightforward repetition |

**Important:** Recursion is not automatically better than iteration. Choose the approach that makes the solution clear and efficient.

---

## 6. Factorial Using Recursion

The factorial of a non-negative integer is the product of all positive integers up to that number.

Mathematical definition:

\[
n! = n \times (n-1) \times \cdots \times 1
\]

Special case:

\[
0! = 1
\]

Python implementation:

```python
def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


print(factorial(5))
```

Output:

```text
120
```

The recursive relationship is:

\[
factorial(n) = n \times factorial(n-1)
\]

---

## 7. Fibonacci Sequence Using Recursion

The Fibonacci sequence is a sequence in which each number is the sum of the previous two numbers.

The first two values are:

\[
F(0)=0,\quad F(1)=1
\]

The recursive relationship is:

\[
F(n)=F(n-1)+F(n-2)
\]

Implementation:

```python
def fibonacci(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(6))
```

Output:

```text
8
```

The first Fibonacci values are:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21
```

### Performance problem

This simple recursive implementation repeatedly calculates the same Fibonacci values.

Its time complexity is exponential, approximately:

\[
O(2^n)
\]

For larger inputs, it becomes inefficient.

Memoization can avoid repeated calculations.

---

## 8. Recursion with Memoization

Memoization is an optimisation technique that stores previously calculated results so they can be reused.

Python provides `functools.cache` and `functools.lru_cache` for caching function results.

Example:

```python
from functools import cache


@cache
def fibonacci(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(40))
```

With caching, each Fibonacci value is calculated only once.

For this implementation:

- Time complexity: \(O(n)\)
- Space complexity: \(O(n)\), including cached results and recursive call stack.

Memoization is particularly useful when recursive calculations contain overlapping subproblems.

---

## 9. Recursive Data Structures

Recursion is useful when working with data structures that contain smaller structures of the same type.

Examples include:

- Trees
- Nested lists
- File directories
- JSON structures
- Graph traversal

### Example: Traversing a nested list

```python
def print_nested_items(items):
    for item in items:
        if isinstance(item, list):
            print_nested_items(item)
        else:
            print(item)


data = [1, 2, [3, 4, [5, 6]], 7]

print_nested_items(data)
```

Output:

```text
1
2
3
4
5
6
7
```

The function checks whether an item is another list.

If it is, the function calls itself to process that nested list.

Otherwise, it processes the item directly.

---

## 10. Tree Traversal Using Recursion

A tree is a hierarchical data structure made up of nodes.

A node can contain references to child nodes.

Example:

```text
        A
       / \
      B   C
     / \
    D   E
```

A recursive function can visit every node.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def traverse(node):
    if node is None:
        return

    print(node.value)

    for child in node.children:
        traverse(child)


root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")

root.children = [node_b, node_c]
node_b.children = [node_d, node_e]

traverse(root)
```

Output:

```text
A
B
D
E
C
```

This is an example of depth-first traversal.

The function visits a node before recursively visiting its children.

---

## 11. Recursion in Agentic AI and Software Engineering

Recursion is not a replacement for every loop or workflow. However, understanding it helps when working with nested structures and recursive problem-solving.

### 11.1 Nested JSON Processing

AI applications frequently receive structured JSON containing nested objects and arrays.

Recursion can process these structures at different levels.

Example:

```python
def extract_values(data):
    results = []

    if isinstance(data, dict):
        for value in data.values():
            results.extend(extract_values(value))

    elif isinstance(data, list):
        for item in data:
            results.extend(extract_values(item))

    else:
        results.append(data)

    return results


response = {
    "user": {
        "name": "Alex",
        "skills": ["Python", "FastAPI"]
    },
    "status": "active"
}

print(extract_values(response))
```

### 11.2 Tree-Based Search

Recursion is commonly used to explore tree structures, such as:

- Search trees
- Document hierarchies
- Parsed expressions
- Nested configuration structures

### 11.3 Agent Workflow Concepts

An agent may need to inspect nested tool results, structured responses, or hierarchical task data.

Recursive functions can help process nested data. However, real agent execution loops should normally have explicit iteration limits, stopping conditions, and error handling rather than uncontrolled recursion.

---

## 12. Common Recursion Errors

### Error 1: Missing Base Case

```python
def example(number):
    return example(number - 1)
```

There is no stopping condition.

This eventually causes:

```text
RecursionError: maximum recursion depth exceeded
```

### Error 2: No Progress Towards the Base Case

```python
def countdown(number):
    if number == 0:
        return

    countdown(number + 1)
```

The function moves away from the base case instead of towards it.

### Error 3: Incorrect Return Statement

Incorrect:

```python
def factorial(number):
    if number == 1:
        return 1

    number * factorial(number - 1)
```

The recursive calculation is performed but its result is not returned.

Correct:

```python
def factorial(number):
    if number == 1:
        return 1

    return number * factorial(number - 1)
```

### Error 4: Excessive Recursion Depth

Python limits how deeply functions can recurse.

Deep recursion can raise `RecursionError`, even when the recursive logic is otherwise correct.

Do not increase the recursion limit as a default solution. Consider iteration or a more suitable algorithm when the problem requires deep traversal.

---

## 13. Time and Space Complexity

Recursion has both execution-time costs and call-stack memory costs.

| Example | Time complexity | Additional space |
|---|---|---|
| Factorial recursion | \(O(n)\) | \(O(n)\) |
| Fibonacci without caching | \(O(2^n)\) | \(O(n)\) |
| Fibonacci with caching | \(O(n)\) | \(O(n)\) |
| Nested list traversal | \(O(n)\) for all elements | Depends on nesting depth |

The complexity depends on how many recursive calls are made and how much work each call performs.

---

## 14. When Should You Use Recursion?

Use recursion when:

1. A problem can naturally be divided into smaller versions of itself.
2. You are processing hierarchical or nested data.
3. You are traversing trees.
4. You are implementing depth-first search.
5. The recursive solution is clearer than an iterative alternative.

Avoid recursion when:

1. A simple loop solves the problem more clearly.
2. The recursion depth may become very large.
3. Repeated recursive calculations create unnecessary overhead.
4. An iterative or dynamic programming solution is more efficient.

---

## 15. Key Concepts to Remember

| Concept | Meaning |
|---|---|
| Recursion | A function calls itself |
| Base case | Condition that stops recursion |
| Recursive case | Function calls itself with a smaller or simpler problem |
| Call stack | Stores active function calls |
| Stack frame | Holds information about one active function call |
| Stack unwinding | Returning through completed recursive calls |
| Memoization | Storing previous results to avoid repeated calculations |
| Tree traversal | Visiting nodes in a hierarchical structure |
| RecursionError | Error caused by exceeding Python's recursion limit |

---

## 16. Practice Tasks

Complete these exercises independently before moving to the practical Python file.

1. Write a recursive function to print numbers from 1 to 10.
2. Write a recursive function to calculate the sum of numbers from 1 to `n`.
3. Implement factorial using recursion.
4. Implement Fibonacci using recursion.
5. Optimise Fibonacci using `functools.cache`.
6. Write a recursive function to reverse a string.
7. Write a recursive function to calculate the sum of all numbers in a nested list.
8. Write a recursive function to find the maximum value in a list.
9. Create a tree and implement depth-first traversal.
10. Explain why the naive recursive Fibonacci implementation is inefficient.

**Completion requirement:** You should be able to identify the base case, recursive case, call sequence, and return sequence for any recursive function you write.