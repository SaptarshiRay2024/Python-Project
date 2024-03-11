from tkinter import *
import customtkinter
import random

root = customtkinter.CTk()
root.geometry("1000x1000")
root.title("Rock Paper Scissors")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

options = {"1" : "Rock" , "2" : "Paper" , "3" : "Scissors"}

def reset():
    button1["state"] = ACTIVE
    button2["state"] = ACTIVE
    button3["state"] = ACTIVE
    label1.configure(text = "Player")
    label3.configure(text = "Computer")
    label4.configure(text = "")

def disable():
    button1["state"] = DISABLED
    button2["state"] = DISABLED
    button3["state"] = DISABLED

def rock():
    choice = options[str(random.randint(1 , 3))]
    if choice == "Rock":
        result = "Match Draw"
    elif choice == "Scissors":
        result = "Player Wins"
    else:
        result = "Computer Wins"
    label4.configure(text = result)
    label1.configure(text = "Rock")
    label3.configure(text = choice)
    disable()

def paper():
    choice = options[str(random.randint(1 , 3))]
    if choice == "Paper":
        result = "Match Draw"
    elif choice == "Scissors":
        result = "Computer Wins"
    else:
        result = "Player Wins"
    label4.configure(text = result)
    label1.configure(text = "Paper")
    label3.configure(text = choice)
    disable()

def scissors():
    choice = options[str(random.randint(1, 3))]
    if choice == "Rock":
        result = "Computer Wins"
    elif choice == "Scissors":
        result = "Match Draw"
    else:
        result = "Player Wins"
    label4.configure(text = result)
    label1.configure(text = "Scissors")
    label3.configure(text = choice)
    disable()

frame2 = customtkinter.CTkFrame(master = root , height = 300 , width = 300 , fg_color = "green")
frame2.place(relx = 0.3 , rely = 0.35 , anchor = CENTER)
label1 = customtkinter.CTkLabel(master = frame2 , text="Player" , font=("normal" , 40))
label1.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
 
label2 = customtkinter.CTkLabel(master = root , text="VS" , font=("normal" , 40))
label2.place(relx = 0.5 , rely = 0.35 , anchor = CENTER)

frame3 = customtkinter.CTkFrame(master = root , height = 300 , width = 300 , fg_color = "green")
frame3.place(relx = 0.7 , rely = 0.35 , anchor = CENTER)
label3 = customtkinter.CTkLabel(master = frame3, text="Computer", font=("normal" , 40))
label3.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

frame1 = customtkinter.CTkFrame(master = root , height = 50 , width = 400)
frame1.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)
label4 = customtkinter.CTkLabel(master = frame1 , text="" , font = ("normal" , 20))
label4.pack(pady=20)
label4.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

label5 = customtkinter.CTkLabel(master = root , text = "ROCK PAPER SCISSORS" , font = ("normal" , 40))
label5.pack(pady=20)
label5.place(relx = 0.5 , rely = 0.1 , anchor = CENTER)

button1 = customtkinter.CTkButton(master = root , text = "Rock" , font = ("normal" , 20) , command = rock)
button1.place(relx = 0.4 , rely = 0.7 , anchor = CENTER)

button2 = customtkinter.CTkButton(master = root , text = "Paper" , font = ("normal" , 20) , command=paper)
button2.place(relx = 0.5 , rely = 0.7 , anchor = CENTER)

button3 = customtkinter.CTkButton(master = root , text = "Scissors" , font = ("normal" , 20) , command=scissors)
button3.place(relx = 0.6 , rely = 0.7 , anchor = CENTER)

button4 = customtkinter.CTkButton(master = root , text = "Reset Game" , font = ("normal" , 20) , fg_color = "green" , command = reset)
button4.place(relx = 0.5 , rely = 0.8 , anchor = CENTER)

button5 = customtkinter.CTkButton(master = root , text = "Exit Game" , font = ("normal" , 20) , fg_color = "red" , command = root.destroy)
button5.place(relx = 0.5 , rely = 0.9 , anchor = CENTER)

root.mainloop()