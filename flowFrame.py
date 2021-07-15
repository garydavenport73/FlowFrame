#
# Gary Davenport
# dovedweller@gmail.com
# 7/14/2021
#
# This Object, FlowFrame inherets from Frame.
# I added methods:
#           'addWidget'
#           'destroyWidgets'
# 
# Make sure the instance of the frame is made to expand
# into parent container for the FlowFrame to work correctly.
#       
from tkinter import Frame

class FlowFrame(Frame):
    def __init__(self, *args, **kwargs):
        super(FlowFrame, self).__init__(*args, **kwargs)
        self.widgets=[]
        self.bind("<Configure>", lambda event:self._reorganizeWidgets())

    def addWidget(self, widget, **kwargs):
        #get the names of all widgets and place in list

        self.widgetChildList=[]
        for child in self.children:
            self.widgetChildList.append(child)

        """
        if force==True:
            print("force was True")
            #remove from frame (unpack, ungrid, unplace)
            for child in self.children:    
                try:
                    #print("trying pack info",self.children[child].pack_info())
                    self.children[child].pack_forget()
                    #print(self.children[child], "was packed, will forget and reflow/grid")
                except:
                    pass
                    #print("not packed")
                try:
                    #print("trying grid info",self.children[child].grid_info())
                    if len(self.children[child].grid_info())>0:
                        self.children[child].grid_forget()
                        #print(self.children[child], "was gridded, will forget and reflow/grid")
                except:
                    pass
                    #print("not gridded")
                try:
                    #print("trying place info", self.children[child].place_info())  
                    if len(self.children[child].place_info())>0:
                        self.children[child].place_forget()
                        #print(self.children[child], "was gridded, will forget and reflow/grid")    
                except:
                    pass
                    #print("not placed")
        """
        #add the new widget to the list
        self.widgetChildList.append(widget)
        """
        if force==True:
            for child in self.children:
                self.children[child].grid(kwargs)
        else:
            widget.grid(kwargs)
        """
        widget.grid(kwargs)

    def destroyWidgets(self):
        #get the names of all widgets in the frame and place in list
        self.widgetChildList=[]
        for child in self.children:
            self.widgetChildList.append(child)
        #destroy the widgets    
        for  i in range(len(self.children)):
            self.children[self.widgetChildList[i]].destroy()
        #reset list to empty
        self.widgetChildList=[]
            
    def _reorganizeWidgets(self):
        #set list to empty
        self.widgetChildList=[]
        #make new list based on children
        for child in self.children:
            self.widgetChildList.append(child)

        #algorithm for flow/gridding children based on window width and widgets widths
        rowNumber=0
        columnNumber=0
        width=0
        i=0
        while i<len(self.children):
            width+=self.children[self.widgetChildList[i]].winfo_width()
            if i==0:
                self.children[self.widgetChildList[i]].grid(row=rowNumber, column=columnNumber)
            elif width > self.winfo_width():
                rowNumber=rowNumber+1             
                columnNumber = 0               
                width=self.children[self.widgetChildList[i]].winfo_width()
            else:
                columnNumber=columnNumber+1
            self.children[self.widgetChildList[i]].grid(row=rowNumber, column=columnNumber)
            i+=1

#sets the class Frame to be a FlowFrame, this only works if this script is placed AFTER the import of tkinter import
Frame=FlowFrame
