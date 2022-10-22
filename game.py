import random
from tkinter import *
from tkinter import Label

from PIL import ImageTk, Image

s = Tk()
c, ur = 0, 0

s.title('rock paper scissor')
s.iconbitmap('images/rps.ico')


def playagain_fun2():
    my_.grid_remove()
    com_.grid_remove()
    play_again.grid_remove()
    buttons()


def winner(u, com):
    global printing, ur, c
    if u == com:

        printing = Label(s, text="it's a draw ")
        printing.grid(row=2, column=0, columnspan=3)
    # printing.pack()
    # print("draw")
    elif u == ("rock" and com == "paper") or (u == "paper" and com == "scissor") or (u == "scissor" and com == "rock"):
        printing = Label(s, text="computer won over you ")
        printing.grid(row=2, column=0, columnspan=3)
        c += 1
    # printing.pack()
    # print("com won")

    else:
        printing = Label(s, text="you won over computer ")
        printing.grid(row=2, column=0, columnspan=3)
        ur += 1


def computer_choice():
    a = [("rock", rock_img), ("paper", paper_img), ("scissor", scissor_img)]
    com = random.choice(a)
    return com


def rock_fun():
    global my1, my, comp, vs, comp1
    com = computer_choice()
    my = Label(s, text="your choice")
    my.grid(row=0, column=0)
    my1 = Label(s, image=rock_img)
    my1.grid(row=1, column=0)

    vs = Label(s, image=vs_img)
    vs.grid(row=1, column=1)

    comp = Label(s, text="computer's choice")
    comp.grid(row=0, column=2)
    comp1 = Label(s, image=com[1])
    comp1.grid(row=1, column=2)

    winner("rock", com[0])

    rock.grid_remove()
    paper.grid_remove()
    scissor.grid_remove()
    play()


def paper_fun():
    global my1, my, comp, vs, comp1

    com = computer_choice()
    my = Label(s, text="your choice")
    my.grid(row=0, column=0)
    my1 = Label(s, image=paper_img)
    my1.grid(row=1, column=0)

    vs = Label(s, image=vs_img)
    vs.grid(row=1, column=1)

    comp = Label(s, text="computer's choice")
    comp.grid(row=0, column=2)
    comp1 = Label(s, image=com[1])
    comp1.grid(row=1, column=2)

    winner("paper", com[0])

    rock.grid_remove()
    paper.grid_remove()
    scissor.grid_remove()
    play()


def scissor_fun():
    global my1, my, comp, vs, comp1
    com = computer_choice()
    my = Label(s, text="your choice")
    my.grid(row=0, column=0)
    my1 = Label(s, image=scissor_img)
    my1.grid(row=1, column=0)

    vs = Label(s, image=vs_img)
    vs.grid(row=1, column=1)

    comp = Label(s, text="computer's choice")
    comp.grid(row=0, column=2)
    comp1 = Label(s, image=com[1])
    comp1.grid(row=1, column=2)

    winner("scissor", com[0])

    rock.grid_remove()
    paper.grid_remove()
    scissor.grid_remove()
    play()


def playagain_fun():
    my.grid_remove()
    comp.grid_remove()
    my1.grid_remove()
    comp1.grid_remove()
    printing.grid_remove()
    buttons()
    playagain.grid_remove()
    score.grid_remove()
    vs.grid_remove()


def score_fun():
    global my_, com_, play_again
    score.grid_remove()
    my.grid_remove()
    my1.grid_remove()
    comp.grid_remove()
    comp1.grid_remove()
    vs.grid_remove()
    printing.grid_remove()
    playagain.grid_remove()
    text = "yours score \n" + str(ur)

    my_ = Label(s, text=text)
    my_.grid(row=0, column=0)

    text = "computer's score \n" + str(c)

    com_ = Label(s, text=text)
    com_.grid(row=0, column=2)

    play_again = Button(s, image=play_img, command=playagain_fun2, borderwidth=0)
    play_again.grid(row=3, column=0, columnspan=3)


def play():
    global playagain, score
    playagain = Button(s, image=play_img, command=playagain_fun, borderwidth=0)
    playagain.grid(row=3, column=0, columnspan=3)

    score = Button(s, image=score_img, command=score_fun, borderwidth=0)
    score.grid(row=4, column=0, columnspan=3)


def buttons():
    global rock, paper, scissor, playagain, score
    Label(s).grid(row=0, column=0)
    rock = Button(s, image=rock_img, command=rock_fun, padx=20, borderwidth=0)
    rock.grid(row=1, column=0, rowspan=2)

    paper = Button(s, image=paper_img, command=paper_fun, padx=20, borderwidth=0)
    paper.grid(row=1, column=1, rowspan=2)

    scissor = Button(s, image=scissor_img, command=scissor_fun, padx=20, borderwidth=0)
    scissor.grid(row=1, column=2, rowspan=2)


rock_img = ImageTk.PhotoImage(Image.open("images/rock.png"))

paper_img = ImageTk.PhotoImage(Image.open("images/paper.png"))

scissor_img = ImageTk.PhotoImage(Image.open("images/scissor.png"))

play_img = ImageTk.PhotoImage(Image.open("images/playagain.png"))

vs_img = ImageTk.PhotoImage(Image.open("images/vs.png"))

score_img = ImageTk.PhotoImage(Image.open("images/score1.png"))

exits = Button(s, text="exit", command=s.quit, bg="red", fg="white", borderwidth=0, padx=50, pady=5)
exits.grid(row=5, column=0, columnspan=3)

buttons()
s.mainloop()
