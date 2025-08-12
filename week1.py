

# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."

# Display the result
print(f"{num1} {operation} {num2} = {result}")


import random

# 1. Personalized Greeting App

print("=== Personalized Greeting App ===")
name = input("What is your name? ")
color = input("What is your favorite color? ")
print(f"Hello, {name}! Your favorite color, {color}, is awesome!\n")

# 2. Simple Quiz Game

print("=== Simple Quiz Game ===")
score = 0

questions = [
    {"question": "What is the capital of France?", "options": ["A) London", "B) Paris", "C) Rome"], "answer": "B"},
    {"question": "Which language is this program written in?", "options": ["A) Python", "B) Java", "C) C++"], "answer": "A"},
    {"question": "What is 5 + 7?", "options": ["A) 10", "B) 11", "C) 12"], "answer": "C"}
]

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").strip().upper()
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

print(f"You got {score} out of {len(questions)} correct!\n")

# -------------------------------
# 3. Random Joke Generator
# -------------------------------
print("=== Random Joke Generator ===")
jokes = [
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "Why do Python programmers wear glasses? Because they can't C!",
    "I told my computer I needed a break, and it said 'No problem – I’ll go to sleep.'",
    "Why was the JavaScript developer sad? Because they didn’t know how to 'null' their feelings."
]

print(random.choice(jokes))
