'''quote generator'''
from tkinter import *

##the 1st function,,,
#processing of the quotes to be diplayed

##the 2nd function,,
#function of how the quote is going to b displayed

##the GUI concept
window = Tk()
window.title("Calculator")
window.geometry("500x600")

label = Label(
    window,
    width=50,
    height=10,
    background="grey"
)
label.pack()
button = Button(
    window,
    text="Generate Quote",
    background="blue",
    width=20,
    border=2
    
)
button.pack()

window.mainloop()
