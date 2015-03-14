from tkinter import *
#-------------------------------------------------------------------
#Tutorial 1 - Windows, labels, and packing
##root = Tk()
##theLabel = Label(root, text="HI")
##theLabel.pack()
##root.mainloop()
#-------------------------------------------------------------------
#Tutorial 2 - Frames and buttons
##root = Tk()
##
##topFrame = Frame(root)
##topFrame.pack()
##bottomFrame = Frame(root)
##bottomFrame.pack(side=BOTTOM)
##
##button1 = Button(topFrame, text = "Button 1", bg="red")
##button2 = Button(topFrame, text = "Button 2", bg="blue")
##button3 = Button(topFrame, text = "Button 3", bg="green")
##button4 = Button(bottomFrame, text = "Button 4", bg="yellow")
##
##button1.pack(side=LEFT)
##button2.pack(side=LEFT)
##button3.pack(side=LEFT)
##button4.pack(side=BOTTOM)
##
##root.mainloop()
#-------------------------------------------------------------------
#Tutorial 3 - Fill
##root = Tk()
##
##one = Label(root, text="Label 1", bg="red", fg="green")
##one.pack()
##two = Label(root, text="Label 2", bg="white",fg="black")
##two.pack(fill=X)
##three = Label(root, text="Label 3", bg="blue", fg="pink")
##three.pack(side=LEFT, fill=Y)
##
##root.mainloop()
#-------------------------------------------------------------------
#Tutorial 4 - Entry fields, Grid formatting, Check boxes
##root = Tk()
##
##label1 = Label(root, text="Name:")
##label2 = Label(root, text="Password:")
##entry1 = Entry(root)
##entry2 = Entry(root)
##
##label1.grid(row=0, sticky=E) #sticky E (right align format, E = East)
##label2.grid(row=1, sticky=E)
##
##entry1.grid(row=0, column=1)
##entry2.grid(row=1, column=1)
##
##c = Checkbutton(root, text="Keep me logged in")
##c.grid(columnspan=2)
##
##root.mainloop()
#-------------------------------------------------------------------
#Tutorial 5 - Binding functions to layouts
#Method 1
##root = Tk()
##
##def helloWorld():
##    print("Hello World!")
##
##button1 = Button(root, text="Print Hello", command=helloWorld)
##button1.pack()
##
##root.mainloop()
##
###Method 2
##root = Tk()
##
##def helloWorld(event):
##    print("Hello World!")
##
##button1 = Button(root, text="Print Hello")
##button1.bind("<Button-1>", helloWorld)
##button1.pack() 
#-------------------------------------------------------------------
#Tutorial 6 & 7 - Binding multiple functions to one widget
##root = Tk()
##
##def leftClick(event):
##    print("Left")
##
##def middleClick(event):
##    print("Middle")
##
##def rightClick(event):
##    print("Right")
##
##frame = Frame(root, width=300, height=200)
### Event is something the user does to the widget, function that gets called
##frame.bind("<Button-1>", leftClick)
##frame.bind("<Button-2>", middleClick)
##frame.bind("<Button-3>", rightClick)
##frame.pack()
##
##root.mainloop()

#-------------------------------------------------------------------
#Tutorial 8 - Using Classes with GUI
##class theClass:
##    def __init__(self, master):
##        frame = Frame(master)
##        frame.pack()
##
##        self.printButton = Button(frame, text="Print the message", command=self.printMessage)
##        self.printButton.pack(side=LEFT)
##
##        self.quitButton = Button(frame, text="Quit", command=frame.quit)
##        self.quitButton.pack(side=LEFT)
##
##    def printMessage(self):
##        print("Wow, this actually works!")
##
##root = Tk()
##test = theClass(root)
##root.mainloop()
#-------------------------------------------------------------------
#Tutorial 14 - Images and Icons
##
##import os
##
##os.chdir("C:\\")
##root = Tk()
##
##photo = PhotoImage(file="airport to hotel.jpg")
##label = Label(root, image=photo)
##label.pack()
##
##root.mainloop()

