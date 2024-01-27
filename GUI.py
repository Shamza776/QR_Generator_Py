###Graphical user interface
##windows = serves as a container to hold or contain these widgets
##widget = the gui elements: buttons, textboxes, labels, images etc
##simple window 
from tkinter import *   ##when using or creating a gui, we import everything from the tk inter module , which is a python bindng to the Tk GUI toolkit

'''window = Tk() #to instantiate an instance of a window to the variable(can be any name),, the set of brackets to serve as the constructor
window.geometry =("420*420") #geometry of the window
window.title('Shamza first GUI program') #the title function
##icon = PhotoImage(file="fileName") ##the  Photoimage function,  used for adding an image in our application,,using the file option
#should be in the same python  file where we defined our window object
#set icon on the window using the iconphoto function, which has two arguments
###CONFIG FUNCTION -- Use it anytime you want to make a change to the window
window.config(background="blue")
#window.iconphoto(True, icon)   #first argument set to true, the second is the image variable that contains the path of the image
#window.mainloop() #place window on the computer screen also listen to events.....display our window

##let's create labels
#label = an area widget that holds text and/ or an image within a window
#label1 = Label(window) #create label object with parent as 'window'
#label1["text"]="Hello Shamza!" #set the text property of the label 
###or;
window.geometry =("420*420")
photo = PhotoImage(file='image.png') ##image you'll include in the window
label1 = Label(window,
                text='hello Shamza!',
                font=("Arial",20,"bold"),
                  foreground="green",
                    background="black",
                    relief="raised", ##for border functionality
                    bd=10, #border width
                    padx=20,  ##add padding to text, x axis
                    pady=20,  ##add padding to text , y axis
                      image= photo, #will place the image on the window but overlap with text 
                       compound= "bottom" ##placement of the image  
                    ) #parantheses are acting as constructor, use pass in the master container
label1.pack() #add the label to the window (it will be centered by default) or we can set the position
##label1.place(x=0, y=0) ##coordinates set where the widgets will appear, this one will appear at the top left corner of the window
window.mainloop()'''

##use of buttons
window = Tk() ##instantiate the instance of a window
window.geometry = ("420*500") ##set the geometry
label2 = (window,  text ="Enter your name : ", fg = "white", bg = "dark blue")
def  click_func():
    print("Button clicked!")
button1 = Button(window, text = "Click me", command = click_func())
window.mainloop()

