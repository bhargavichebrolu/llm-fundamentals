
# ============================================================
# PYTHON CONTROL FLOW - LOOP CONTROL
# File: loop-control.py
# ============================================================


# 1. break statement

print("1. Break statement")

for number in range(1, 11):

    if number == 5:
        break

    print(number)


# 2. continue statement

print("\n2. Continue statement")

for number in range(1, 6):

    if number == 3:
        continue

    print(number)


# 3. pass statement

print("\n3. Pass statement")

for number in range(5):

    if number == 3:
        pass

    print(number)


# 4. Find a user using break

print("\n4. Find a user")

users = ["Ravi", "John", "Ammu", "David"]

for user in users:

    if user == "Ammu":
        print("User found:", user)
        break


# 5. Skip invalid documents using continue

print("\n5. Skip invalid documents")

documents = [
    "Python is useful",
    "",
    "AI agents use tools",
    "",
    "Machine learning"
]

for document in documents:

    if not document.strip():
        continue

    print("Processing:", document)


# 6. pass as a placeholder function

print("\n6. Placeholder functions")


def search_tool():
    pass


def calculator_tool():
    pass


def weather_tool():
    pass


# 7. Nested for loops

print("\n7. Nested for loops")

for i in range(1, 4):

    for j in range(1, 3):
        print(i, j)


# 8. Multiplication tables using nested loops

print("\n8. Multiplication tables")

for i in range(1, 4):

    print("Table:", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)


# 9. Compare two lists using nested loops

print("\n9. Compare two lists")

users = ["Ammu", "Ravi", "John"]
admins = ["Ravi", "David"]

for user in users:

    for admin in admins:

        if user == admin:
            print(user, "is an admin")


# 10. Nested while loops

print("\n10. Nested while loops")

i = 1

while i <= 3:

    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1


# 11. Stop searching after finding a document

print("\n11. Find a relevant document")

documents = [
    "Cooking recipes",
    "Python programming guide",
    "Travel information"
]

for document in documents:

    if "Python" in document:
        print("Relevant document:", document)
        break


# 12. Skip empty documents

print("\n12. Skip empty documents")

documents = [
    "Python tutorial",
    "",
    "AI engineering guide",
    "   ",
    "Machine learning notes"
]

for document in documents:

    if not document.strip():
        continue

    print("Processing:", document)


# 13. Agent retry loop

print("\n13. Agent retry loop")

attempts = 0
max_attempts = 3
task_completed = False

while attempts < max_attempts:

    attempts += 1

    print("Attempt:", attempts)

    # Simulate successful completion on attempt 2.
    if attempts == 2:
        task_completed = True
        break

if task_completed:
    print("Task successful")
else:
    print("Task failed")


# 14. Find the first number divisible by 7 and 11

print("\n14. Find first matching number")

for number in range(1, 201):

    if number % 7 == 0 and number % 11 == 0:
        print("Found:", number)
        break


# 15. Skip multiples of 3

print("\n15. Skip multiples of 3")

for number in range(1, 21):

    if number % 3 == 0:
        continue

    print(number)


# 16. Break in an inner loop

print("\n16. Break in nested loops")

for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            break

        print(i, j)


# 17. Stop nested loops using a flag

print("\n17. Stop both nested loops")

stop_search = False

for i in range(1, 4):

    for j in range(1, 4):

        if i == 2 and j == 2:
            stop_search = True
            break

        print(i, j)

    if stop_search:
        break


# ============================================================
# END OF LOOP CONTROL
# ============================================================
