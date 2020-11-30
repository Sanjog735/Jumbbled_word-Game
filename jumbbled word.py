from tkinter import *
import tkinter.messagebox as tmsg
import random

answers = [
    "python",
    "java",
    "swift",
    "canada",
    "india",
    "america",
    "london",
]

words = [
    "nptoyh",
    "avja",
    "wfsit",
    "cdanaa",
    "aidin",
    "aiearcm",
    "odnlon",
]

num = random.randrange(0,len(words),1)

def default():
    global words,answers,num
    l.config(text=words[num])
def check():
    global words,answers,num
    var = e.get()     # find out the text from the entry widget and set it to a variable
    if var==answers[num]:
        tmsg.showinfo("Success","Congratulation .You Have Chosen the correct Answer ")
        clear()
    else:
        tmsg.showwarning("Error","Sorry! Your answer is wrong ")
        clear()
def clear():
    global words,answers,num
    num = random.randrange(0,len(words))
    l.config(text=words[num])
    e.delete(0,END)

root =Tk()
root.geometry("650x500")
root.configure(background="#FF0099")
root.title("Jumbbled Game")

l = Label(root,text="Lots of Fun",font="Comicsansms 29 bold")
l.pack(fill=BOTH,ipady=10,ipadx=10,pady=28)
text=StringVar()
e = Entry(root,textvariable=text,font="Verdana 24")
e.pack(ipady=5,ipadx=5)
b1 = Button(root,text="Check",font="Comic 16",command=check)
b1.pack(ipadx=5,ipady=5,pady=27)
b1 = Button(root,text="Clear",font="Comic 16",command=clear)
b1.pack(ipadx=5,ipady=5)

default()

root.mainloop()