# Python Functions

## 1. What is a Function?

A function is a reusable block of code designed to perform a specific task.

Functions help:
- Avoid repeating code.
- Organise programs into smaller units.
- Improve readability and maintainability.
- Reuse logic in different parts of an application.

### Syntax

```python
def function_name(parameters):
    # function body
    return result
```

Example:

```python
def greet(name):
    return f"Hello {name}"

print(greet("Ammu"))
```

Output:
```
Hello Ammu
```

## 2. Function Components

- `def`: Keyword used to define a function.
- Function name: Identifies the function.
- Parameters: Variables that receive input.
- Arguments: Actual values passed when calling a function.
- Function body: Code executed by the function.
- `return`: Sends a result back to the caller.

Example:

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Here:
- `a` and `b` are parameters.
- `10` and `20` are arguments.
- `30` is the returned result.

## 3. Return vs Print

### print()
Displays information on the screen. It does not send that value back as the function result.

```python
def add(a, b):
    print(a + b)

result = add(10, 20)
print(result)
```

Output:
```
30
None
```

### return
Sends a value back to the caller so it can be stored or reused.

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

Output:
```
30
```

**Important:** A function without an explicit return statement returns `None`.

## 4. Types of Function Arguments

### A. Positional Arguments

Values are assigned according to their position.

```python
def introduce(name, age):
    return f"My name is {name} and I am {age}"

print(introduce("Ammu", 24))
```

### B. Keyword Arguments

Values are assigned using parameter names.

```python
def introduce(name, age):
    return f"My name is {name} and I am {age}"

print(introduce(age=24, name="Ammu"))
```

### C. Default Arguments

A parameter uses a predefined value if no alternative is supplied.

```python
def greet(name, language="English"):
    return f"Hello {name}, language: {language}"

print(greet("Ammu"))
print(greet("Ammu", "Telugu"))
```

### D. Variable-Length Arguments

**`*args`** collects extra positional arguments into a tuple.

```python
def calculate_total(*numbers):
    return sum(numbers)

print(calculate_total(10, 20, 30, 40))
```

**`**kwargs`** collects extra keyword arguments into a dictionary.

```python
def display_details(**details):
    for key, value in details.items():
        print(key, value)

display_details(name="Ammu", role="AI Engineer")
```

## 5. Useful String Operations in Functions

### split()
Splits a string into a list of words.

```python
text = "Learning Python"
print(text.split())
```

Output: `['Learning', 'Python']`

### len()
Returns the number of items in a collection.

```python
print(len(["Python", "AI", "Agents"]))
```

Output: `3`

### strip()
Removes whitespace from the beginning and end of a string.

```python
text = "  Hello Python  "
print(text.strip())
```

Output: `Hello Python`

### lower()
Converts a string to lowercase.

```python
print("HELLO PYTHON".lower())
```

Output: `hello python`

## 6. Function Composition

Function composition means using the result of one function as the input to another function.

Example:

```python
def clean_text(text):
    return text.strip().lower()

def count_words(text):
    return len(text.split())

def process_text(text):
    cleaned = clean_text(text)
    word_count = count_words(cleaned)
    return cleaned, word_count

cleaned_text, total_words = process_text(
    "  LEARNING AGENTIC AI  "
)

print(cleaned_text)
print(total_words)
```

Output:
```
learning agentic ai
3
```

## 7. Multiple Return Values

Python allows a function to return multiple values.

```python
def get_details():
    return "Python", 3

language, version = get_details()

print(language)
print(version)
```

Technically, Python packs the returned values into a tuple, which can be unpacked into separate variables.

## 8. Practical Applications in Agentic AI

Functions are important in AI applications because they separate individual responsibilities.

Examples:

| Function | Purpose |
|---|---|
| clean_text() | Clean user input |
| count_words() | Count words |
| format_prompt() | Prepare an LLM prompt |
| validate_input() | Check incoming data |
| call_llm() | Send a request to an LLM |
| execute_tool() | Execute a selected tool |

An AI agent can combine many small functions to complete a larger task.

## 9. Token Estimation vs Actual Tokenisation

A rough token estimate can be made using:

```python
def estimate_tokens(text):
    return len(text.split())
```

However, this counts words, not actual model tokens.

Actual tokenisation depends on the tokenizer used by the model. Use a model-compatible tokenizer when accurate token counts are required.

## 10. Key Takeaways

1. Functions make code reusable.
2. Parameters receive inputs; arguments provide values.
3. `return` sends values back to the caller.
4. `print()` displays values.
5. Functions can use positional, keyword and default arguments.
6. `*args` handles extra positional arguments.
7. `**kwargs` handles extra keyword arguments.
8. Functions can call other functions.
9. Python functions can return multiple values.
10. Small reusable functions make AI applications easier to test and maintain.

## 11. Interview Questions

1. What is a function in Python?
2. What is the difference between a parameter and an argument?
3. What is the difference between return and print?
4. What happens if a function has no return statement?
5. What are positional and keyword arguments?
6. What are default arguments?
7. What is the difference between *args and **kwargs?
8. Can a Python function return multiple values?
9. What is function composition?
10. Why are reusable functions useful when developing AI agents?

## 12. Day 1 Completion Checklist

- [ ] Understand function syntax.
- [ ] Understand parameters and arguments.
- [ ] Understand return vs print.
- [ ] Practise positional and keyword arguments.
- [ ] Practise default arguments.
- [ ] Understand *args and **kwargs.
- [ ] Implement five independent coding exercises.
- [ ] Explain function composition.
- [ ] Complete the knowledge quiz.

**Next topic:** Python Data Structures — Lists, Tuples, Dictionaries and Sets.