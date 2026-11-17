
# ============================================================
# PYTHON CONTROL FLOW - LOOPS
# File: loops.py
# ============================================================


# 1. For loop with a list

languages = ["Python", "Java", "C++"]

print("1. For loop with list")

for language in languages:
    print(language)


# 2. For loop with a tuple

coordinates = (10, 20, 30)

print("\n2. For loop with tuple")

for coordinate in coordinates:
    print(coordinate)


# 3. For loop with a set

unique_languages = {"Python", "Java", "C++"}

print("\n3. For loop with set")

for language in unique_languages:
    print(language)


# 4. For loop with a dictionary

student = {
    "name": "Ammu",
    "age": 24,
    "course": "AI"
}

print("\n4. For loop with dictionary")

for key, value in student.items():
    print(key, ":", value)


# 5. For loop with a string

word = "AGENT"

print("\n5. For loop with string")

for character in word:
    print(character)


# 6. range(stop)

print("\n6. range(stop)")

for number in range(5):
    print(number)


# 7. range(start, stop)

print("\n7. range(start, stop)")

for number in range(2, 7):
    print(number)


# 8. range(start, stop, step)

print("\n8. range(start, stop, step)")

for number in range(0, 11, 2):
    print(number)


# 9. Reverse range

print("\n9. Reverse range")

for number in range(10, 0, -1):
    print(number)


# 10. enumerate()

languages = ["Python", "Java", "C++"]

print("\n10. Enumerate")

for index, language in enumerate(languages):
    print(index, language)


# 11. enumerate() with starting index

print("\n11. Enumerate with start")

for index, language in enumerate(languages, start=1):
    print(index, language)


# 12. While loop

print("\n12. While loop")

count = 1

while count <= 5:
    print(count)
    count += 1


# 13. Countdown using while

print("\n13. Countdown")

count = 10

while count >= 1:
    print(count)
    count -= 1


# 14. Sum of numbers using for loop

print("\n14. Sum using for loop")

total = 0

for number in range(1, 101):
    total += number

print("Total:", total)


# 15. Count matching elements

print("\n15. Count matching elements")

numbers = [10, 20, 10, 30, 10]

count = 0

for number in numbers:

    if number == 10:
        count += 1

print("Occurrences of 10:", count)


# 16. Multiplication table

print("\n16. Multiplication table")

number = 5

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 17. Count vowels

print("\n17. Count vowels")

word = "artificial intelligence"

vowels = "aeiou"
vowel_count = 0

for character in word.lower():

    if character in vowels:
        vowel_count += 1

print("Vowel count:", vowel_count)


# 18. Find largest number without max()

print("\n18. Find largest number")

numbers = [10, 50, 20, 80, 30]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print("Largest:", largest)


# 19. Process multiple documents

print("\n19. Document processing")

documents = [
    "Python is useful for AI",
    "Machine learning uses data",
    "Agents can call tools"
]

for document in documents:
    print("Processing:", document)


# 20. Process conversation messages

print("\n20. Conversation processing")

messages = [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi"},
    {"role": "user", "content": "Explain Python"}
]

for message in messages:
    print(message["role"], message["content"])


# 21. Nested for loops

print("\n21. Nested for loops")

for i in range(1, 4):

    for j in range(1, 3):
        print(i, j)


# 22. Nested multiplication tables

print("\n22. Multiple multiplication tables")

for i in range(1, 4):

    print("Table:", i)

    for j in range(1, 11):
        print(i, "x", j, "=", i * j)


# 23. Nested loops: Compare two collections

print("\n23. Comparing collections")

users = ["Ammu", "Ravi", "John"]
admins = ["Ravi", "David"]

for user in users:

    for admin in admins:

        if user == admin:
            print(user, "is an admin")


# 24. Nested while loops

print("\n24. Nested while loops")

i = 1

while i <= 3:

    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1


# 25. Agent task execution loop

print("\n25. Agent task execution")

task_completed = False
attempts = 0
max_attempts = 3

while not task_completed and attempts < max_attempts:

    attempts += 1

    print("Attempt:", attempts)

    if attempts == 2:
        task_completed = True

print("Task completed:", task_completed)
print("Total attempts:", attempts)


# ============================================================
# END OF LOOPS
# ============================================================
