# FlowFrame
This is a child of the Frame class in Tkinter with a method of add(widget), then all widgets flow in the FlowFrame.

I wanted text flow behavior of widgets in a tkinter Frame.  So I made this object, called a FlowFrame, which inherets
everything from the Frame class in Tkinter, but adds one method "addWidget".  This way, whatever widgets are added to the frame,
they will flow like text.  The widgets currently are set to be sticky="NSEW" but I may give more options in the future.
Also, I have a removeWidgets method, which just removes all widgets from the frame.  I plan to give more methods in the future.
There is a demo called flowFrameDemo.py

<div>
<ul>
  Summary:
  <li>Object: FlowFrame</li>
  <li>Inherets from: Frame</li>
  <li>
  Methods:
    <ul>
      <li>addWidget(widget)</li>
      <li>removeWidgets()</li>
    </ul>
  </li>
  
</ul>
  </div>
