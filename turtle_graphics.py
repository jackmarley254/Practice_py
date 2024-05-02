#!/usr/bin/python3
# Kibo FPWP Final Project
import turtle

# Initialize Turtle
t = turtle.Turtle()
t.speed(0)

# Function to draw question box
def draw_box(x, y, width, height, text):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("lightblue")
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(x + width / 2, y - height / 2)
    t.write(text, align="center", font=("Arial", 12, "normal"))

# Function to display question and choices
def display_question(question, choices):
    draw_box(-90, 150, 200, 100, question)
    for i, choice in enumerate(choices):
        draw_box(-100, 40 - i * 40, 200, 30, choice)

# Function to get user input
def get_input():
    answer = turtle.textinput("Quiz", "Enter your choice:")
    return answer

# Function to check answer and display result
def check_answer(answer):
    if answer == "a":
        turtle.write("Correct!", align="center", font=("Arial", 12, "normal"))
    else:
        turtle.write("Incorrect!", align="center", font=("Arial", 12, "normal"))

# Main function
def main():
    # Define quiz question and choices
    question = "What is the capital of France?"
    choices = ["a) Paris", "b) London", "c) Berlin", "d) Rome"]

    # Display question and choices
    display_question(question, choices)

    # Get user input
    answer = get_input()

    # Check answer and display result
    check_answer(answer.lower())

    # Keep the window open until user closes it
    turtle.done()

# Run the program
if __name__ == "__main__":
    main()

