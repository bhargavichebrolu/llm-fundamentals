
# ==========================================
# Day 1: Python Functions and Reusable Code
# ==========================================


# Exercise 1: Word Counter
def count_words(text):
    words = text.split()
    return len(words)


# Exercise 2: Token Estimator
def estimate_tokens(text):
    estimated_tokens = len(text.split())
    return estimated_tokens


# Exercise 3: Prompt Formatter
def format_prompt(role, question):
    prompt = f"You are a {role}. Answer this question: {question}"
    return prompt


# Exercise 4: Text Cleaner
def clean_text(text):
    cleaned = text.strip().lower()
    return cleaned


# Exercise 5: Combine Functions
def process_text(text):
    cleaned = clean_text(text)
    word_count = count_words(cleaned)

    return cleaned, word_count


# ==========================================
# Testing all five functions
# ==========================================

# Exercise 1
print("Exercise 1: Word Counter")
print(count_words("I am learning Python"))


# Exercise 2
print("\nExercise 2: Token Estimator")
print(estimate_tokens("Agentic AI is interesting"))


# Exercise 3
print("\nExercise 3: Prompt Formatter")
print(format_prompt("Python tutor", "Explain functions"))


# Exercise 4
print("\nExercise 4: Text Cleaner")
print(clean_text("  HELLO PYTHON  "))


# Exercise 5
print("\nExercise 5: Combined Functions")
cleaned_text, total_words = process_text(
    "  LEARNING AGENTIC AI  "
)

print("Cleaned text:", cleaned_text)
print("Word count:", total_words)
