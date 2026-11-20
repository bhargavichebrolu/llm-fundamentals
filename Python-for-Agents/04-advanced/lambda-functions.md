# Python Lambda Functions

## 1. What Is a Lambda Function?

A lambda function is a small, anonymous function in Python that is defined using the `lambda` keyword.

Unlike a regular function created using `def`, a lambda function does not require a function name or an explicit `return` statement.

### Regular function

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

Output:

```text
30
```

### Equivalent lambda function

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

Both functions perform the same operation.

The difference is how they are defined.

**Syntax:**

```python
lambda arguments: expression
```

- `lambda`: Keyword used to define the function.
- `arguments`: Inputs accepted by the function.
- `expression`: A single expression whose result is automatically returned.

---

## 2. Understanding Lambda Syntax

Example:

```python
square = lambda number: number * number

print(square(5))
```

Output:

```text
25
```

Explanation:

1. `lambda` creates an anonymous function.
2. `number` is the function parameter.
3. `number * number` is the expression.
4. The expression's result is automatically returned.
5. The function is assigned to the variable `square`.
6. Calling `square(5)` executes the function.

There is no need to write `return`.

---

## 3. Lambda Functions with Different Arguments

### 3.1 No arguments

```python
greet = lambda: "Hello Python"

print(greet())
```

Output:

```text
Hello Python
```

### 3.2 One argument

```python
double = lambda number: number * 2

print(double(10))
```

Output:

```text
20
```

### 3.3 Two arguments

```python
add = lambda a, b: a + b

print(add(10, 20))
```

Output:

```text
30
```

### 3.4 Multiple arguments

```python
calculate = lambda a, b, c: a + b + c

print(calculate(10, 20, 30))
```

Output:

```text
60
```

Lambda functions can accept multiple parameters, but their body must contain only one expression.

---

## 4. Lambda vs Regular Functions

| Feature | Regular function | Lambda function |
|---|---|---|
| Definition | `def` | `lambda` |
| Function name | Usually named | Anonymous by default |
| Body | Multiple statements | One expression |
| Return | Explicit `return` usually used | Automatically returns expression result |
| Documentation | Supports docstrings | No normal function-body docstring |
| Complexity | Suitable for complex logic | Suitable for simple logic |

### Regular function

```python
def calculate_discount(price, discount):
    discounted_price = price - (price * discount / 100)
    return discounted_price
```

### Lambda equivalent

```python
calculate_discount = lambda price, discount: price - (price * discount / 100)
```

Both calculate the discounted price.

For complex calculations, prefer regular functions because they are easier to read, document and maintain.

---

## 5. Lambda Functions with `sorted()`

One of the most common uses of lambda functions is custom sorting.

Consider:

```python
students = [
    ("Alice", 85),
    ("Bob", 92),
    ("Charlie", 78),
    ("David", 95)
]
```

Suppose you want to sort students according to their marks.

```python
students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print(students_sorted)
```

Output:

```text
[
    ('Charlie', 78),
    ('Alice', 85),
    ('Bob', 92),
    ('David', 95)
]
```

### How does it work?

The `sorted()` function accepts a `key` argument.

The key function determines which value should be used for sorting.

```python
key=lambda student: student[1]
```

For every tuple, the lambda function extracts the second element, which represents the student's marks.

Python sorts the tuples using those extracted values.

### Descending order

```python
students_sorted = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)
```

Output:

```text
[
    ('David', 95),
    ('Bob', 92),
    ('Alice', 85),
    ('Charlie', 78)
]
```

---

## 6. Lambda Functions with `map()`

`map()` applies a function to every element in an iterable.

Syntax:

```python
map(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

squared = map(
    lambda number: number ** 2,
    numbers
)

print(list(squared))
```

Output:

```text
[1, 4, 9, 16, 25]
```

Explanation:

- `map()` takes the lambda function.
- It applies the function to each number.
- It returns a map iterator.
- `list()` converts the iterator into a list.

Without lambda:

```python
def square(number):
    return number ** 2

squared = map(square, numbers)
```

Both approaches produce the same result.

---

## 7. Lambda Functions with `filter()`

`filter()` selects elements from an iterable based on a condition.

Syntax:

```python
filter(function, iterable)
```

Example:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)

print(list(even_numbers))
```

Output:

```text
[2, 4, 6, 8]
```

Explanation:

- `filter()` evaluates the lambda function for every element.
- If the condition returns `True`, the element is retained.
- If it returns `False`, the element is excluded.

### Practical example: Filtering AI confidence scores

```python
confidence_scores = [0.45, 0.91, 0.72, 0.38, 0.98]

high_confidence = filter(
    lambda score: score >= 0.8,
    confidence_scores
)

print(list(high_confidence))
```

Output:

```text
[0.91, 0.98]
```

---

## 8. Lambda Functions with `reduce()`

`reduce()` repeatedly combines elements of an iterable into a single accumulated result.

It is available through the `functools` module.

Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(
    lambda accumulated, current: accumulated + current,
    numbers
)

print(total)
```

Output:

```text
15
```

Explanation:

- `accumulated` stores the result so far.
- `current` represents the next element.
- `reduce()` supplies these arguments to the lambda function.
- The returned result becomes the next accumulated value.

`reduce()` is not restricted to addition. The supplied function determines how values are combined.

For ordinary addition, prefer `sum()` because it is clearer.

---

## 9. Lambda Functions with Conditional Expressions

Lambda functions can contain conditional expressions.

Syntax:

```python
lambda arguments: value_if_true if condition else value_if_false
```

Example:

```python
check_number = lambda number: "Even" if number % 2 == 0 else "Odd"

print(check_number(10))
print(check_number(7))
```

Output:

```text
Even
Odd
```

Another example:

```python
classify_score = lambda score: "Pass" if score >= 50 else "Fail"

print(classify_score(75))
print(classify_score(35))
```

Output:

```text
Pass
Fail
```

Remember that a conditional expression is still one expression.

---

## 10. Lambda Functions with Dictionaries

Lambda functions can be stored as dictionary values.

This is useful when selecting operations dynamically.

```python
operations = {
    "add": lambda a, b: a + b,
    "subtract": lambda a, b: a - b,
    "multiply": lambda a, b: a * b,
    "divide": lambda a, b: a / b
}

print(operations["add"](10, 5))
print(operations["multiply"](10, 5))
```

Output:

```text
15
50
```

The dictionary acts as a simple operation registry.

This pattern can also be used to map tool names to functions in an application.

---

## 11. Lambda Functions and Closures

Lambda functions can also capture variables from an enclosing scope.

Example:

```python
def create_multiplier(factor):
    return lambda number: number * factor


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
```

Output:

```text
20
30
```

Here:

- `create_multiplier()` is the enclosing function.
- The lambda function uses `factor`.
- The returned lambda retains access to that variable.
- Each call to `create_multiplier()` creates a separately configured function.

This is an example of a closure created using a lambda function.

---

## 12. Limitations of Lambda Functions

### 12.1 Only one expression

Lambda functions cannot contain multiple statements.

Invalid:

```python
# Invalid lambda syntax

calculate = lambda number:
    result = number * 2
    return result
```

Use a regular function instead:

```python
def calculate(number):
    result = number * 2
    return result
```

### 12.2 Difficult to read when logic becomes complex

Avoid writing long and complicated lambda expressions.

Less readable:

```python
result = lambda x: x * 2 if x > 10 else x + 5 if x > 5 else x
```

More readable:

```python
def calculate(number):
    if number > 10:
        return number * 2

    if number > 5:
        return number + 5

    return number
```

### 12.3 No normal function-body docstring

Regular functions can include docstrings explaining their purpose.

```python
def calculate_tax(amount):
    """Calculate tax for a given amount."""
    return amount * 0.2
```

Lambda functions do not support a normal multi-line function body with a docstring.

### 12.4 Not suitable for complex business logic

For authentication, API processing, data validation or complicated AI workflows, regular functions are usually more appropriate.

---

## 13. When Should You Use Lambda Functions?

Use lambda functions when:

- You need a small, simple function.
- You need a quick sorting key.
- You need a short transformation with `map()`.
- You need a simple filtering condition with `filter()`.
- You need a small callback function.
- You need a short function inside a dictionary.
- You need a simple function to configure a closure.

Use regular functions when:

- You need multiple statements.
- You need detailed documentation.
- You need complex conditions.
- You need exception handling.
- You need reusable business logic.
- You need code that is easier to debug and maintain.

---

## 14. Practical Applications in AI and Backend Development

### Data preprocessing

```python
raw_values = ["  Python ", " Java ", " FastAPI "]

cleaned_values = list(
    map(lambda value: value.strip(), raw_values)
)

print(cleaned_values)
```

Output:

```text
['Python', 'Java', 'FastAPI']
```

### Filtering AI predictions

```python
predictions = [
    {"label": "spam", "confidence": 0.95},
    {"label": "ham", "confidence": 0.62},
    {"label": "spam", "confidence": 0.88}
]

high_confidence_predictions = list(
    filter(
        lambda prediction: prediction["confidence"] >= 0.8,
        predictions
    )
)

print(high_confidence_predictions)
```

### Sorting retrieved documents

```python
documents = [
    {"content": "Document A", "score": 0.75},
    {"content": "Document B", "score": 0.95},
    {"content": "Document C", "score": 0.82}
]

ranked_documents = sorted(
    documents,
    key=lambda document: document["score"],
    reverse=True
)

print(ranked_documents)
```

This is a simple example of ranking retrieved documents by relevance score.

---

## 15. Interview Questions

1. What is a lambda function in Python?
2. What is the difference between `def` and `lambda`?
3. Can lambda functions accept multiple arguments?
4. Can lambda functions contain multiple statements?
5. Why don't lambda functions require an explicit `return`?
6. How can lambda functions be used with `sorted()`?
7. What is the difference between `map()` and `filter()`?
8. How does `reduce()` work with a lambda function?
9. Can lambda functions create closures?
10. When should you prefer a regular function over a lambda?

---

## 16. Knowledge Checklist

- [ ] Understand lambda syntax.
- [ ] Create lambda functions with zero, one and multiple arguments.
- [ ] Understand automatic return values.
- [ ] Explain lambda versus regular functions.
- [ ] Use lambda with `sorted()`.
- [ ] Use lambda with `map()`.
- [ ] Use lambda with `filter()`.
- [ ] Use lambda with `reduce()`.
- [ ] Write conditional expressions inside lambdas.
- [ ] Store lambda functions in dictionaries.
- [ ] Understand lambda functions and closures.
- [ ] Identify when lambda functions should not be used.

**Final takeaway:** Lambda functions are a concise way to define small, single-expression functions. Their biggest practical value is when passing simple behaviour to other functions such as `sorted()`, `map()` and `filter()`.
