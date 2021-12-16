from tkinter import *
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk

game = Tk()
game.title('Rock, Paper, Scissors')
game.geometry("600x750")
game.config(bg="white")
game.resizable(0, 0)

game_title = Label(text='Welcome to "Rock Paper Scissors"!', font=('arial', 18, 'bold'), fg='green')
game_title.pack(pady=10)

first = Image.open('First.jpg')
rock = Image.open('Rock.jpg')
paper = Image.open('Paper.jpg')
scissors = Image.open('Scissors.jpg')

first.thumbnail((350, 350), Image.ANTIALIAS)
rock.thumbnail((500, 500), Image.ANTIALIAS)
paper.thumbnail((400, 400), Image.ANTIALIAS)
scissors.thumbnail((400, 400), Image.ANTIALIAS)

first1 = ImageTk.PhotoImage(first)
rock1 = ImageTk.PhotoImage(rock)
paper1 = ImageTk.PhotoImage(paper)
scissors1 = ImageTk.PhotoImage(scissors)

image_list = [rock1, paper1, scissors1]

image_label = tk.Label(game, image=first1, bd=0)
image_label.pack(pady=20)

text_label = Label(text="Choose your weapon:", fg='green', font=('arial', 15, 'bold'), pady=5)
text_label.pack()

user_score = 0
cpu_score = 0
user_choice_value = 0

def play():
    global user_choice_value
    global user_score
    global cpu_score

    user_score_label.config(text=f"Your Score : {user_score}")
    cpu_score_label.config(text=f"CPU Score :  {cpu_score}")

    cpu_choice = randint(0, 2)

    # image_label.config(image=image_list[cpu_choice])

    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":
        user_choice_value = 2

    if user_choice_value == cpu_choice:
        win_lose_label.config(text=f"CPU chose {user_choice.get()}.It's a Tie!Play Again...")
        image_label.config(image=image_list[cpu_choice])
    else:
        if user_choice_value == 0:         #rock
            if cpu_choice == 1:
                cpu_score += 1
                win_lose_label.config(text="CPU chose Paper.Paper covers Rock!You Lose...")
                image_label.config(image=image_list[cpu_choice])
            elif cpu_choice == 2:
                user_score += 1
                win_lose_label.config(text="CPU chose Scissors.Rock smashes Scissors!You Win!!!")
                image_label.config(image=image_list[user_choice_value])
        if user_choice_value == 1:          #paper
            if cpu_choice == 0:
                user_score += 1
                win_lose_label.config(text="CPU chose Rock.Paper cover Rock!You Win!!!")
                image_label.config(image=image_list[user_choice_value])
            elif cpu_choice == 2:
                cpu_score += 1
                win_lose_label.config(text="CPU chose Scissors.Scissors cuts Paper!You Lose...")
                image_label.config(image=image_list[cpu_choice])
        if user_choice_value == 2:         #scissors
            if cpu_choice == 0:
                cpu_score += 1
                win_lose_label.config(text="CPU chose Rock.Rock smashes Scissors!You Lose...")
                image_label.config(image=image_list[cpu_choice])
            elif cpu_choice == 1:
                user_score += 1
                win_lose_label.config(text="CPU chose Paper.Scissors cuts Paper!You Win!")
                image_label.config(image=image_list[user_choice_value])


user_choice = ttk.Combobox(game, value=("Rock", "Paper", "Scissors"), font=('arial', 15))
user_choice.current(0)
user_choice.pack(pady=20)

play_button = Button(game, text="Play!", command=play, fg='green', width=10, height=2, bd=1, bg='#FFC733', font=('arial', 15))
play_button.pack(pady=20)

win_lose_label = Label(game, text="", font=("arial", 15), bg="white", fg='green')
win_lose_label.pack(pady=20)

user_score_label = Label(game, text="", font=("arial", 10))
user_score_label.pack(pady=2)
cpu_score_label = Label(game, text="", font=("arial", 10))
cpu_score_label.pack(pady=2)

game.mainloop()
