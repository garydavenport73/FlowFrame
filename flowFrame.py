#
# Gary Davenport
# garydavenport73@gmail.com
# 4/29/2021
#
# This Object, FlowFrame inherets from Frame.
# I added methods:
#           'addWidget'
#           'removeWidgets'
# 
# As currently written, all widgets are sticky=NSEW
# 
# Make sure the instance of the frame is made to expand
# into parent container for the FlowFrame to work correctly.
#       
from tkinter import *

class FlowFrame(Frame):
    def __init__(self, *args, **kwargs):
        super(FlowFrame, self).__init__(*args, **kwargs)
        self.widgets=[]
        self.bind("<Configure>", lambda event:self._reorganizeWidgets())

    def addWidget(self, widget):
        self.widgets.append(widget)

    def removeWidgets(self):
        self.widgets=[]

    def _reorganizeWidgets(self):
        rowNum=0
        columnNum=0
        width=0
        i=0
        while i<len(self.widgets):
            width+=self.widgets[i].winfo_width()
            if i==0:self.widgets[i].grid(row=rowNum, column=columnNum, sticky=NSEW)
            elif width >= self.winfo_width():
                rowNum=rowNum+1             
                columnNum = 0               
                width=self.widgets[i].winfo_width()
            else:
                columnNum=columnNum+1
            self.widgets[i].grid(row=rowNum, column=columnNum, sticky=NSEW)
            i+=1

        
        
