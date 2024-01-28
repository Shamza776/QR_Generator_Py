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
#label2 = (window,  text ="Enter your name : ", fg = "white", bg = "dark blue")

'''count = 0
def  click_func():
    global count
    count += 1
    print("Button clicked  " + str(count) + "  times!" )
button1 = Button(window,
          text = "Click me", 
          command = click_func,
          padx = 20,
           pady= 20, 
            font= ("Comic Sans",20),
             foreground= "black",
              background="white"
                )
button1.pack() ''' ##a button

'''use of the enry widget

def submit():
    value = entry.get() ##get function used to get the value from the entry box
    value
    print('hello ' + value)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0, END)  #delete the whole value input from the entry widget
def backspace ():
    value = entry.get()
    entry.delete(len(value)-1, END)

entry = Entry(window,
              font=("Arial",50),
              fg="green",
              bg="beige",
              show='*'
              )
##insert some default text for our entry widget
#entry.insert(0,'heyyyy')

entry.pack(side="left")
submit_button = Button(window,
                text="submit",
                font=("Arial", 30),
                command=submit,
                padx=10,
                pady=10,
                bd= 1,
                )
submit_button.pack(side = "right")
delete_button = Button(window,
                text="delete",
                font=("Arial", 30),
                command=delete,
                padx=10,
                pady=10,
                bd= 1,
                )
delete_button.pack(side = "right")
backspace_button= Button(window,
                text="backspace",
                font=("Arial", 30),
                command=backspace,
                padx=10,
                pady=10,
                bd= 1,
                )
backspace_button.pack(side = "right") '''

'''check boxes'''

def display():
    if(x.get()==1):  ##if  
        print('you agree')
    else:
        print("you dont agree")
x = IntVar() #function indicating its  a check button variable for an integer,,by default returns a one or zero....BooleanVar...StringVar
check_button = Checkbutton(window,
                           text="terms and conditions",
                            variable = x, ##associate the variable with the check box
                            onvalue=1, ##what will be stored within our variable if its toggled on....True,, "yes"
                            offvalue=0, ##stored in the variable if its toggled off....False,, "no"
                            command= display 
                           )
check_button.pack()






window.mainloop()

