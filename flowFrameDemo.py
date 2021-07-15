
from tkinter import *
from flowframe import *

import time

def _destroyWidgets():
    myframe.destroyWidgets()

def main():

    root = Tk()

    root.title("Using Inherited \"FlowFrame\"")

    global myframe
    myframe=Frame(root)
    #make sure frame expands to fill parent window
    myframe.pack(fill="both", expand=1) 

    button=Button(myframe, text="---Button---")

    button.pack()
    root.update()
    time.sleep(2)

    button.grid(sticky=NSEW)
    root.update()
    time.sleep(1)

    myframe.addWidget(button)

    textbox=Text(myframe,width=3,height=2)
    myframe.addWidget(textbox)

    label=Label(myframe,text="Label")
    myframe.addWidget(label,sticky=NSEW)

    entry=Entry(myframe)
    myframe.addWidget(entry, sticky=NSEW)

    radioButton=Radiobutton(myframe,text="radio button")
    myframe.addWidget(radioButton)

    checkButton=Checkbutton(myframe,text="CheckButton")
    myframe.addWidget(checkButton)

    scale_widget = Scale(myframe, from_=0, to=100, orient=HORIZONTAL)
    myframe.addWidget(scale_widget)

    button2=Button(myframe, text="---Remove All---", command=_destroyWidgets)
    myframe.addWidget(button2)

    #myframe.removeWidgets()

    root.mainloop()

main()
