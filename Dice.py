from PIL import ImageTk
import PIL.Image
import random 

from tkinter import *

root = Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(bg = "#fadadd")

#Pic = ImageTk.PhotoImage(PIL.Image.open("dice.webp"))
Pic = PIL.Image.open("dice.webp")
size=(100,100)
Pic = Pic.resize(size)
Pic = ImageTk.PhotoImage(Pic)

Vihaan = Label(root, text ="Vihaan's Endless Dice Game", bg="#fadadd", font = ("Comic Sans MS",20,"bold"))
Vihaan.place(relx = 0.5, rely = 0.1, anchor=CENTER)
p1=Label(root, text="Player 1", bg="dark green",padx=5,pady=5, fg="goldenrod3", font = ("Comic Sans MS",13,"bold"))
p1.place(relx=0.1, rely=0.3, anchor=CENTER)
p2=Label(root, text="Player 2", bg="dark green", fg="goldenrod3",padx=5,pady=5, font = ("Comic Sans MS",13,"bold"))
p2.place(relx=0.9, rely=0.3, anchor=CENTER)

p1_score=Label(root, bg="dark green",padx=5,pady=5, fg="goldenrod3", font = ("Comic Sans MS",13,"bold"))
p1_score.place(relx=0.1, rely=0.4, anchor=CENTER)
p2_score=Label(root, bg="dark green", fg="goldenrod3",padx=5,pady=5, font = ("Comic Sans MS",13,"bold"))
p2_score.place(relx=0.9, rely=0.4, anchor=CENTER)



random_label=Label(root, bg="dark green",padx=5,pady=5, fg="goldenrod3", font = ("Georgia",15,"bold"))
random_label.place(relx=0.5, rely=0.5, anchor=CENTER)

p1score = 0

def Player1():
    global p1score
    r1 = random.randint(1,6)
    random_label["text"] = "Player 1 rolled the dice and got " + str(r1)
    p1score = p1score + r1
    p1_score["text"] = str(p1score)
    
    
btn1 = Button(root, image = Pic, command = Player1, bg = "#34c6eb")
btn1.place(relx = 0.1, rely = 0.6, anchor=CENTER)


p2score = 0

def Player2():
    global p2score
    r2 = random.randint(1,6)
    random_label["text"] = "Player 2 rolled the dice and got " + str(r2)
    p2score = p2score + r2
    p2_score["text"] = str(p2score)
    
    
btn2 = Button(root, image = Pic, command = Player2, bg = "#34c6eb")
btn2.place(relx = 0.9, rely = 0.6, anchor=CENTER)


root.mainloop()

