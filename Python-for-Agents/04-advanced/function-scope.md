# Python Function Scope

## 1. What is Scope in Python?

Scope refers to the region of a Python program where a variable can be accessed.

In Python, a variable is not necessarily accessible everywhere. Its accessibility depends on where it is defined.

For example:

```python
def greet():
    message = "Hello Python"
    print(message)

greet()

print(message)  # NameError
```

Output:

```text
Hello Python
NameError: name 'message' is not defined
```

Explanation:

- `message` is created inside the `greet()` function.
- It is a local variable.
- It can be accessed inside `greet()`.
- It cannot be accessed directly outside the function.

**Important:** A variable's scope determines where it can be accessed, not simply where it was created.

---

## 2. The Four Types of Scope in Python

Python follows four levels of scope:

1. Local scope
2. Enclosing scope
3. Global scope
4. Built-in scope

Python searches these scopes using the LEGB rule.

### 2.1 Local Scope

A variable created inside a function belongs to that function's local scope.

```python
def calculate():
    result = 100
    print(result)

calculate()
```

Output:

```text
100
```

Here:

- `result` is a local variable.
- It is accessible inside `calculate()`.
- It cannot be directly accessed outside `calculate()`.

Another example:

```python
def first_function():
    name = "Python"
    print(name)


def second_function():
    print(name)


first_function()
second_function()
```

The second function raises a `NameError` because `name` belongs to the local scope of `first_function()`.

Each function has its own local scope.

### 2.2 Enclosing Scope

An enclosing scope occurs when one function is defined inside another function.

The inner function can access variables defined in the outer function.

```python
def outer():
    message = "Hello from outer function"

    def inner():
        print(message)

    inner()


outer()
```

Output:

```text
Hello from outer function
```

Explanation:

- `outer()` is the enclosing function.
- `inner()` is the nested function.
- `message` belongs to the enclosing scope of `inner()`.
- The inner function can access the outer function's variable.

**Important:** The inner function can read variables from its enclosing function without using any special keyword.

However, modifying an enclosing variable requires additional understanding, covered in the `nonlocal` section.

### 2.3 Global Scope

A variable defined outside all functions belongs to the global scope.

```python
company = "OpenAI"

def display_company():
    print(company)


display_company()
print(company)
```

Output:

```text
OpenAI
OpenAI
```

Here:

- `company` is a global variable.
- It can be accessed inside the function.
- It can also be accessed outside the function.

#### Modifying a global variable

Consider:

```python
count = 0

def increment():
    count = count + 1

increment()
```

This raises an `UnboundLocalError`.

Why?

When Python sees an assignment to `count` inside the function, it treats `count` as a local variable unless told otherwise.

Python therefore tries to read the local `count` before it has been assigned.

To modify the global variable, use the `global` keyword.

```python
count = 0

def increment():
    global count
    count += 1

increment()

print(count)
```

Output:

```text
1
```

The `global` keyword tells Python that `count` refers to the variable defined in the global scope.

**Important:** Avoid excessive use of global variables. They can make programs harder to test, debug and maintain because different parts of the application can modify the same state.

### 2.4 Built-in Scope

Built-in scope contains names provided by Python itself.

Examples:

- `print()`
- `len()`
- `sum()`
- `max()`
- `min()`
- `range()`
- `type()`
- `str()`
- `int()`

You can use these names without defining them yourself.

```python
numbers = [10, 20, 30]

print(len(numbers))
print(sum(numbers))
print(max(numbers))
```

Output:

```text
3
60
30
```

**Important:** Avoid naming your variables after built-in functions.

For example:

```python
list = [1, 2, 3]

print(list)
```

This shadows Python's built-in `list` name. It can cause problems when you later try to use `list()`.

Prefer:

```python
numbers_list = [1, 2, 3]
```

---

## 3. The LEGB Rule

LEGB describes the order Python follows when searching for a variable name.

LEGB stands for:

| Letter | Scope | Meaning |
|---|---|---|
| L | Local | Current function |
| E | Enclosing | Outer function containing the current function |
| G | Global | Module-level variables |
| B | Built-in | Names provided by Python |

Python searches in this order:

**Local → Enclosing → Global → Built-in**

Example:

```python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        name = "Local"
        print(name)

    inner()

outer()
```

Output:

```text
Local
```

Why?

Python finds `name` in the local scope of `inner()` first.

It does not need to search the enclosing, global or built-in scopes.

Now remove the local variable:

```python
name = "Global"

def outer():
    name = "Enclosing"

    def inner():
        print(name)

    inner()

outer()
```

Output:

```text
Enclosing
```

Python cannot find `name` in the local scope of `inner()`, so it searches the enclosing scope.

Now remove the enclosing variable:

```python
name = "Global"

def outer():

    def inner():
        print(name)

    inner()

outer()
```

Output:

```text
Global
```

Python searches the global scope after failing to find the variable in the local and enclosing scopes.

---

## 4. The `global` Keyword

The `global` keyword allows a function to modify a variable defined at the module level.

Example:

```python
total_requests = 0

def record_request():
    global total_requests
    total_requests += 1


record_request()
record_request()
record_request()

print(total_requests)
```

Output:

```text
3
```

Without `global`, an assignment inside the function makes `total_requests` a local variable.

### When should you use `global`?

It can be useful for understanding simple examples and small scripts.

However, in larger applications, prefer:
- Passing values as function arguments.
- Returning updated values.
- Using classes to manage related state.
- Using appropriate state-management mechanisms.

---

## 5. The `nonlocal` Keyword

The `nonlocal` keyword is used inside a nested function when you want to modify a variable belonging to an enclosing function.

It does not refer to the global scope.

Example without `nonlocal`:

```python
def outer():
    count = 0

    def inner():
        count = count + 1
        print(count)

    inner()


outer()
```

This raises an `UnboundLocalError`.

Why?

Python interprets `count` inside `inner()` as a local variable because of the assignment.

But the expression tries to read that local variable before assigning a value to it.

Use `nonlocal`:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)

    inner()


outer()
```

Output:

```text
1
```

The `nonlocal` keyword tells Python to use the variable from the nearest enclosing function scope.

### Multiple calls

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    inner()
    inner()
    inner()

    print(count)


outer()
```

Output:

```text
3
```

All three calls modify the same enclosing variable.

### Difference between `global` and `nonlocal`

| Feature | `global` | `nonlocal` |
|---|---|---|
| Refers to | Module-level variable | Nearest enclosing function variable |
| Used inside | A function | A nested function |
| Modifies | Global variable | Enclosing function variable |
| Requires nested functions? | No | Yes, an enclosing function scope must exist |

Example:

```python
value = 100

def outer():
    value = 50

    def inner():
        nonlocal value
        value += 10

    inner()
    print(value)


outer()
print(value)
```

Output:

```text
60
100
```

The inner function modifies the enclosing `value`, not the global `value`.

---

## 6. Nested Functions and Variable Access

A nested function is simply a function defined inside another function.

```python
def outer():
    message = "Python"

    def inner():
        print(message)

    inner()


outer()
```

The inner function can access variables from the outer function because of Python's lexical scoping rules.

Lexical scoping means that variable accessibility is determined by where functions are defined in the source code.

It is not determined by where those functions are called.

Example:

```python
def outer():
    message = "Hello"

    def inner():
        print(message)

    return inner


function_reference = outer()

function_reference()
```

Output:

```text
Hello
```

Notice that `outer()` has already finished executing before `function_reference()` is called.

The returned inner function still has access to `message`.

This behaviour is the foundation of closures.

Closures are covered separately in `closures.md`.

---

## 7. Common Mistakes

### Mistake 1: Assuming local variables are accessible everywhere

```python
def calculate():
    result = 50

calculate()

print(result)  # NameError
```

Correction: `result` belongs to the local scope of `calculate()`.

### Mistake 2: Modifying a global variable without `global`

```python
count = 0

def increment():
    count += 1
```

Correction:

```python
count = 0

def increment():
    global count
    count += 1
```

### Mistake 3: Using `global` instead of `nonlocal`

```python
def outer():
    count = 0

    def inner():
        global count
        count += 1
```

This does not modify the enclosing `count`.

Correction:

```python
def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
```

### Mistake 4: Shadowing built-in names

```python
sum = 100
```

This shadows Python's built-in `sum()` function in the current scope.

Prefer a descriptive name such as:

```python
total = 100
```

### Mistake 5: Confusing accessing a variable with modifying it

Reading an enclosing variable does not require `nonlocal`.

```python
def outer():
    value = 10

    def inner():
        print(value)

    inner()
```

Modifying an enclosing variable through assignment requires `nonlocal`.

```python
def outer():
    value = 10

    def inner():
        nonlocal value
        value += 5

    inner()
    print(value)
```

---

## 8. Practical Applications

Understanding scope is important when building larger Python applications.

### Backend development

- Understanding local variables inside API endpoint functions.
- Avoiding unexpected shared global state.
- Managing configuration and application state.

### Agentic AI development

- Understanding nested functions used in tool execution.
- Managing variables inside callbacks.
- Understanding closures used in decorators.
- Understanding how functions retain access to configuration and state.

### General software engineering

- Preventing variable-name conflicts.
- Avoiding unintended state changes.
- Writing reusable functions.
- Debugging `NameError` and `UnboundLocalError` exceptions.

---

## 9. Interview Questions

1. What is variable scope in Python?
2. Explain the LEGB rule.
3. What is the difference between local and global scope?
4. What is an enclosing scope?
5. What is the purpose of the `global` keyword?
6. What is the purpose of the `nonlocal` keyword?
7. What is the difference between `global` and `nonlocal`?
8. Can an inner function access variables from an outer function?
9. Why does assigning to a variable inside a function sometimes produce `UnboundLocalError`?
10. What is lexical scoping?

---

## 10. Knowledge Checklist

Before moving to the next topic, make sure you can:

- [ ] Explain what scope means.
- [ ] Identify local, enclosing, global and built-in variables.
- [ ] Explain the LEGB lookup order.
- [ ] Access an enclosing variable from a nested function.
- [ ] Modify a global variable using `global`.
- [ ] Modify an enclosing variable using `nonlocal`.
- [ ] Explain the difference between reading and modifying an enclosing variable.
- [ ] Identify common `NameError` and `UnboundLocalError` situations.
- [ ] Explain how nested functions lead to closures.

**Final takeaway:** Scope determines where Python can find a variable. `global` and `nonlocal` control which existing variable an assignment modifies. Understanding these concepts is essential before learning closures and decorators.
