from tkinter import *
from flowframe import *

def main():

    buttonArray=[]
    root = Tk()

    myframe=FlowFrame(root, mode="grid")
    #make sure frame expands to fill parent window
    myframe.pack(fill="both", expand=1) 

    buttonMakePlace=Button(myframe, text="---Use Place---",command=myframe.organizeWidgetsWithPlace)
    myframe.addWidget(buttonMakePlace, sticky=NSEW)

    buttonMakeGrid=Button(myframe, text="---Use Grid---", command=myframe.organizeWidgetsWithGrid)
    myframe.addWidget(buttonMakeGrid, sticky=NSEW)

    buttonDestroy=Button(myframe,text="---Destroy---", command = myframe.destroyWidgets)

    for i in range(10):
        buttonArray.append(Button(myframe,text=str(i)))

    root.mainloop()

main()
