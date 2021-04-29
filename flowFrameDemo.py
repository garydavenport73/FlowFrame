from tkinter import *
from flowFrame import *

def main():

    root = Tk()

    root.title("Using Inherited \"FlowFrame\"")

    myframe=FlowFrame(root)
    #make sure frame expands to fill parent window
    myframe.pack(fill="both", expand=1) 

    button=Button(myframe, text="---Button---")
    myframe.addWidget(button)

    textbox=Text(myframe,width=3,height=2)
    myframe.addWidget(textbox)

    label=Label(myframe,text="Label")
    myframe.addWidget(label)

    entry=Entry(myframe)
    myframe.addWidget(entry)

    radioButton=Radiobutton(myframe,text="radio button")
    myframe.addWidget(radioButton)

    checkButton=Checkbutton(myframe,text="CheckButton")
    myframe.addWidget(checkButton)

    scale_widget = Scale(myframe, from_=0, to=100, orient=HORIZONTAL)
    myframe.addWidget(scale_widget)

    #myframe.removeWidgets()

    root.mainloop()

main()