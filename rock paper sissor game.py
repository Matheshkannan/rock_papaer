import tkinter as tk
import random

# function to check the result of the game
def check_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        result_label.config(text="Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

# function to get the computer's choice
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# function to handle the user's choice
def choose_rock():
    computer_choice = get_computer_choice()
    user_choice = "Rock"
    check_result(user_choice, computer_choice)

def choose_paper():
    computer_choice = get_computer_choice()
    user_choice = "Paper"
    check_result(user_choice, computer_choice)

def choose_scissors():
    computer_choice = get_computer_choice()
    user_choice = "Scissors"
    check_result(user_choice, computer_choice)

# create the window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="#F9A602") # set background color to light gray

# create the labels and buttons
title_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
title_label.pack(pady=10)

rock_btn = tk.Button(root, text="Rock", font=("Arial", 14), command=choose_rock)
rock_btn.pack(pady=10)

paper_btn = tk.Button(root, text="Paper", font=("Arial", 14), command=choose_paper)
paper_btn.pack(pady=10)

scissors_btn = tk.Button(root, text="Scissors", font=("Arial", 14), command=choose_scissors)
scissors_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

root.mainloop()
