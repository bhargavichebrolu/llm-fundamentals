# Python Conditional Statements

## 1. Introduction

Conditional statements allow a program to make decisions based on conditions.

A condition evaluates to either `True` or `False`.

They are used in:
- Login validation
- Data validation
- API response handling
- AI agent decision-making
- Tool selection
- Error checking

## 2. if Statement

Executes a block of code when a condition is True.

```python
age = 22

if age >= 18:
    print("Eligible")
```

## 3. if-else Statement

Provides an alternative when the condition is False.

```python
age = 16

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
```

## 4. if-elif-else Statement

Used when multiple conditions need to be checked.

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Fail")
```

Python evaluates conditions from top to bottom and executes the first matching branch.

## 5. Comparison Operators

| Operator | Meaning | Example |
|---|---|---|
| `==` | Equal | `10 == 10` |
| `!=` | Not equal | `10 != 5` |
| `>` | Greater than | `10 > 5` |
| `<` | Less than | `5 < 10` |
| `>=` | Greater than or equal | `10 >= 10` |
| `<=` | Less than or equal | `5 <= 10` |

Comparison operators return Boolean values.

```python
print(10 == 10)  # True
print(10 > 20)   # False
```

Remember:

- `=` assigns a value.
- `==` compares two values.

## 6. Logical Operators

Logical operators combine conditions.

### AND

Both conditions must be True.

```python
age = 22
has_id = True

if age >= 18 and has_id:
    print("Access granted")
```

### OR

At least one condition must be True.

```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")
```

### NOT

Reverses a Boolean value.

```python
is_blocked = False

if not is_blocked:
    print("User can continue")
```

## 7. Nested if Statements

An if statement can be placed inside another if statement.

```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Not eligible")
```

Use nested conditions when a decision depends on another decision. Avoid unnecessary nesting when a combined condition is clearer.

## 8. Membership Operators in Conditions

`in` and `not in` check whether an element exists in a collection.

```python
allowed_roles = ["admin", "manager"]

role = "admin"

if role in allowed_roles:
    print("Permission granted")
```

## 9. Identity Operators

`is` and `is not` check whether two references point to the same object.

```python
value = None

if value is None:
    print("No value provided")
```

Do not use `is` to compare ordinary values such as strings or numbers. Use `==` for value equality.

## 10. Truthy and Falsy Values

Python evaluates some values as False in conditions.

Common falsy values:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`

Most other values are truthy.

Example:

```python
message = ""

if message:
    print("Message exists")
else:
    print("Message is empty")
```

## 11. Conditional Expressions

A conditional expression is a short form of if-else.

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

Use it for simple decisions, not complicated branching logic.

## 12. AI Agent Application

A basic tool-selection example:

```python
user_message = "Calculate 25 + 30"
tool_available = True

if not user_message.strip():
    print("Reject empty input")

elif "calculate" in user_message.lower() and tool_available:
    print("Execute calculator tool")

else:
    print("Use another processing method")
```

Real systems also need input validation, access controls and error handling.

## 13. Common Mistakes

1. Using `=` instead of `==`.
2. Forgetting the colon after a condition.
3. Incorrect indentation.
4. Using `is` instead of `==` for value comparison.
5. Writing conditions in the wrong order.
6. Forgetting to validate numeric input ranges.
7. Creating unnecessarily complicated nested conditions.

## 14. Interview Questions

1. What are conditional statements?
2. Explain if, elif and else.
3. What is the difference between `=` and `==`?
4. Explain AND, OR and NOT.
5. What are nested if statements?
6. What are truthy and falsy values?
7. What is the difference between `is` and `==`?
8. What are membership operators?
9. What is a conditional expression?
10. How do conditions help an AI agent select tools?

## 15. Completion Checklist

- [ ] I understand if statements.
- [ ] I can use if-else.
- [ ] I can use multiple elif conditions.
- [ ] I understand comparison operators.
- [ ] I understand logical operators.
- [ ] I can write nested conditions.
- [ ] I understand truthy and falsy values.
- [ ] I understand membership and identity operators.
- [ ] I can implement a basic AI tool-selection condition.