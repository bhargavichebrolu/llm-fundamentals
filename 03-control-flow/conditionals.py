
# ============================================================
# PYTHON CONTROL FLOW - CONDITIONAL STATEMENTS
# File: conditionals.py
# ============================================================


# 1. Boolean values

is_active = True
is_blocked = False

print("1. Boolean values")
print(is_active)
print(is_blocked)
print(type(is_active))


# 2. Basic if statement

temperature = 30

print("\n2. If statement")

if temperature > 25:
    print("It is hot")


# 3. If-else statement

age = 17

print("\n3. If-else")

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")


# 4. If-elif-else statement

marks = 85

print("\n4. If-elif-else")

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")


# 5. Comparison operators

number = 10

print("\n5. Comparison operators")
print(number == 10)
print(number != 5)
print(number > 5)
print(number < 20)
print(number >= 10)
print(number <= 10)


# 6. Logical AND

age = 22
has_id = True

print("\n6. Logical AND")

if age >= 18 and has_id:
    print("Access granted")
else:
    print("Access denied")


# 7. Logical OR

is_admin = False
is_manager = True

print("\n7. Logical OR")

if is_admin or is_manager:
    print("Access granted")
else:
    print("Access denied")


# 8. Logical NOT

is_blocked = False

print("\n8. Logical NOT")

if not is_blocked:
    print("User can continue")


# 9. Combining logical operators

age = 24
has_account = True
is_blocked = False

print("\n9. Combined conditions")

if age >= 18 and has_account and not is_blocked:
    print("Account access granted")
else:
    print("Access denied")


# 10. Short-circuit evaluation

user = None

print("\n10. Short-circuit evaluation")

if user is not None and user["active"]:
    print("Active user")
else:
    print("User is unavailable or inactive")


# 11. Nested if statements

age = 25
has_id = True

print("\n11. Nested conditions")

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("ID required")
else:
    print("Not eligible")


# 12. Membership operators

allowed_roles = ["admin", "manager", "developer"]
role = "admin"

print("\n12. Membership operators")

if role in allowed_roles:
    print("Permission granted")

if "guest" not in allowed_roles:
    print("Guest role is not allowed")


# 13. Dictionary membership

student = {
    "name": "Ammu",
    "age": 24
}

print("\n13. Dictionary membership")

print("name" in student)
print("Ammu" in student)
print("Ammu" in student.values())


# 14. Identity operators

value = None

print("\n14. Identity operators")

if value is None:
    print("No value provided")

first = [10, 20, 30]
second = [10, 20, 30]

print(first == second)
print(first is second)


# 15. Truthy and falsy values

print("\n15. Truthy and falsy values")

print(bool(10))
print(bool(0))
print(bool("Python"))
print(bool(""))
print(bool([]))
print(bool([1, 2]))
print(bool(None))


# 16. Checking an empty message

message = ""

print("\n16. Empty message validation")

if message:
    print("Message exists")
else:
    print("Message is empty")


# 17. Conditional expression

age = 20

print("\n17. Conditional expression")

status = "Adult" if age >= 18 else "Minor"

print(status)


# 18. Function with conditional logic

def calculate_grade(marks):

    if marks < 0 or marks > 100:
        return "Invalid marks"

    elif marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    else:
        return "Fail"


print("\n18. Grade calculator")
print(calculate_grade(85))
print(calculate_grade(105))


# 19. Input validation function

def validate_message(message):

    if not isinstance(message, str):
        return False

    if not message.strip():
        return False

    return True


print("\n19. Message validation")
print(validate_message("Explain Python"))
print(validate_message(""))
print(validate_message(123))


# 20. AI application: Tool selection

user_message = "Calculate 25 + 30"
tool_available = True

print("\n20. AI tool selection")

if not user_message.strip():
    print("Reject empty input")

elif "calculate" in user_message.lower() and tool_available:
    print("Execute calculator tool")

else:
    print("Process using another method")


# 21. AI application: Permission validation

allowed_tools = {"search", "calculator", "weather"}

requested_tool = "calculator"

print("\n21. Tool permission")

if requested_tool in allowed_tools:
    print("Tool is permitted")
else:
    print("Tool is not permitted")


# 22. AI application: API response handling

response = {
    "status": "success",
    "data": "Python information"
}

print("\n22. API response")

if response.get("status") == "success":
    print("Process response:", response.get("data"))
else:
    print("Request failed")


# 23. AI application: Task routing

task = {
    "type": "calculation",
    "input": "25 + 30"
}

print("\n23. Agent task routing")

if task["type"] == "search":
    print("Route to search tool")

elif task["type"] == "calculation":
    print("Route to calculator tool")

elif task["type"] == "weather":
    print("Route to weather tool")

else:
    print("Unknown task")


# ============================================================
# END OF CONDITIONAL STATEMENTS
# ============================================================
