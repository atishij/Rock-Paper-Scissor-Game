from tkinter import *
from PIL import Image, ImageTk
from random import randint
#main window
root = Tk()
root.title("Rock Scissor Paper")
root.configure(background="#9b59b6")

# picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

# insert picture
user_label = Label(root, image=scissor_img, bg="#9b59b6")
comp_label = Label(root, image=scissor_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

#scores 
playerscore = Label(root,text =0,font=100,bg="#9b59b6",fg="black")
computerscore = Label(root,text =0,font=100,bg="#9b59b6",fg="black")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)

#indicators
user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="black")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root,font=50,bg="#9b59b6",fg="black")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x

#update player score
def updateUserScore():
    score = int(playerscore["text"])
    score +=1
    playerscore["text"] = str(score)

#update computer score    
def updateComputerScore():
    score = int(computerscore["text"])
    score +=1
    computerscore["text"] = str(score)

#check winner 
def checkwin(player,computer):
    if player == computer:
        updateMessage("Tie")  
    elif player == "rock":
        if computer == "paper":
            updateMessage("Computer Wins")
            updateComputerScore()
        else: 
            updateMessage("User wins")    
            updateUserScore()  
    elif player == "paper":
        if computer == "scissor":
            updateMessage("Computer Wins")
            updateComputerScore()
        else: 
            updateMessage("User wins")    
            updateUserScore()          
    elif player == "scissor":
        if computer == "rock":
            updateMessage("Computer Wins")
            updateComputerScore()
        else: 
            updateMessage("User wins")    
            updateUserScore()   
    else:    
        pass           
#update pic
choices = ["rock" , "paper" , "scissor"]
def updatechoice(x):
#for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp) 
#for user

    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    checkwin(x,compChoice)    
#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="#ff3e4d",fg = "black",command = lambda:updatechoice("rock")).grid(row=2,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="#fad02e",fg = "black",command = lambda:updatechoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="#0abde3",fg = "black",command = lambda:updatechoice("scissor")).grid(row=2,column=3)
root.mainloop()