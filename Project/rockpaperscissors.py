from tkinter import *
import customtkinter
from PIL import Image , ImageTk
import random

window = customtkinter.CTk()
window.geometry("1000x1000")
window.title("Rock Paper Scissors")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

options = {"1" : "Rock" , "2" : "Paper" , "3" : "Scissors"}

blankimage = customtkinter.CTkImage(Image.open("C:/project/images/blank.png") , size = (300 , 300))
rockleftimage = customtkinter.CTkImage(Image.open("C:/project/images/rockleft.png") , size = (300 , 300))
rockrightimage = customtkinter.CTkImage(Image.open("C:/project/images/rockright.png") , size = (300 , 300))
paperleftimage = customtkinter.CTkImage(Image.open("C:/project/images/paperleft.png") , size = (300 , 300))
paperrightimage = customtkinter.CTkImage(Image.open("C:/project/images/paperright.png") , size = (300 , 300))
scissorsleftimage = customtkinter.CTkImage(Image.open("C:/project/images/scissorsleft.png") , size = (300 , 300))
scissorsrightimage = customtkinter.CTkImage(Image.open("C:/project/images/scissorsright.png") , size = (300 , 300))

def reset():
    button1.configure(state = NORMAL)
    button2.configure(state = NORMAL)
    button3.configure(state = NORMAL)
    label1.configure(image = blankimage)
    label3.configure(image = blankimage)
    label4.configure(text = "")
    label7.configure(text = "")
    label9.configure(text = "")

def disable():
    button1.configure(state = DISABLED)
    button2.configure(state = DISABLED)
    button3.configure(state = DISABLED)

def rock():
    choice = options[str(random.randint(1 , 3))]
    if choice == "Rock":
        result = "Match Draw"
        label3.configure(image = rockrightimage)
    elif choice == "Scissors":
        result = "Player Wins"
        label3.configure(image = scissorsrightimage)
    else:
        result = "Computer Wins"
        label3.configure(image = paperrightimage)
    label4.configure(text = result)
    label1.configure(image = rockleftimage)
    label7.configure(text = "Rock")
    label9.configure(text = choice)
    disable()

def paper():
    choice = options[str(random.randint(1 , 3))]
    if choice == "Paper":
        result = "Match Draw"
        label3.configure(image = paperrightimage)
    elif choice == "Scissors":
        result = "Computer Wins"
        label3.configure(image = scissorsrightimage)
    else:
        label3.configure(image = rockrightimage)
        result = "Player Wins"
    label4.configure(text = result)
    label1.configure(image = paperleftimage)
    label7.configure(text = "Paper")
    label9.configure(text = choice)
    disable()

def scissors():
    choice = options[str(random.randint(1, 3))]
    if choice == "Rock":
        result = "Computer Wins"
        label3.configure(image = rockrightimage)
    elif choice == "Scissors":
        result = "Match Draw"
        label3.configure(image = scissorsrightimage)
    else:
        result = "Player Wins"
        label3.configure(image = paperrightimage)
    label4.configure(text = result)
    label1.configure(image = scissorsleftimage)
    label7.configure(text = "Scissors")
    label9.configure(text = choice)
    disable()

frame2 = customtkinter.CTkFrame(master = window , height = 300 , width = 300)
frame2.place(relx = 0.2 , rely = 0.35 , anchor = CENTER)
label1 = customtkinter.CTkLabel(master = frame2 , text="" , font=("normal" , 40) , image = blankimage)
label1.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
 
label2 = customtkinter.CTkLabel(master = window , text="VS" , font=("normal" , 40))
label2.place(relx = 0.5 , rely = 0.35 , anchor = CENTER)

frame3 = customtkinter.CTkFrame(master = window , height = 300 , width = 300)
frame3.place(relx = 0.8 , rely = 0.35 , anchor = CENTER)
label3 = customtkinter.CTkLabel(master = frame3, text="", font=("normal" , 40) , image = blankimage)
label3.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

frame3 = customtkinter.CTkFrame(master = window , height = 50 , width = 400)
frame3.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
label4 = customtkinter.CTkLabel(master = frame3 , text="" , font = ("normal" , 40))
label4.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

label5 = customtkinter.CTkLabel(master = window , text = "ROCK PAPER SCISSORS" , font = ("normal" , 40))
label5.place(relx = 0.5 , rely = 0.1 , anchor = CENTER)

label6 = customtkinter.CTkLabel(master = window , text = "Player" , font = ("normal" , 40))
label6.place(relx = 0.2 , rely = 0.6 , anchor = CENTER)

label7 = customtkinter.CTkLabel(master = window , text = "" , font = ("normal" , 40))
label7.place(relx = 0.2 , rely = 0.7 , anchor = CENTER)

label8 = customtkinter.CTkLabel(master = window , text = "Computer" , font = ("normal" , 40))
label8.place(relx = 0.8 , rely = 0.6 , anchor = CENTER)

label9 = customtkinter.CTkLabel(master = window , text = "" , font = ("normal" , 40))
label9.place(relx = 0.8 , rely = 0.7 , anchor = CENTER)

button1 = customtkinter.CTkButton(master = window , text = "Rock" , font = ("normal" , 40) , command = rock)
button1.place(relx = 0.35 , rely = 0.7 , anchor = CENTER)

button2 = customtkinter.CTkButton(master = window , text = "Paper" , font = ("normal" , 40) , command=paper)
button2.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

button3 = customtkinter.CTkButton(master = window , text = "Scissors" , font = ("normal" , 40) , command=scissors)
button3.place(relx = 0.65 , rely = 0.7 , anchor = CENTER)

button4 = customtkinter.CTkButton(master = window , text = "Reset Game" , font = ("normal" , 40) , fg_color = "green" , command = reset)
button4.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)

button5 = customtkinter.CTkButton(master = window , text = "Exit Game" , font = ("normal" , 40) , fg_color = "red" , command = window.destroy)
button5.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

window.mainloop()