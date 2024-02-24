##QUOTE GENERATOR
#import tkinter as tk    ##an inbuilt module ..for GUI implementation
from tkinter import *   #importing all the widgets from tkinter 
import requests         ##the installed python library/module for making HTTP requests,handling responces and managing underlying connection. it is an efficient way to interact with the web services and APIs   
from threading import Thread #to make the program multithreaded and easy for the user to  interact with it.
 
api = "http://api.quotable.io/random"     ##API link from where we will get our quotes, take us to some page where we will find some json

quotes =  [] #list of quotes, everytime we load sth, we will want to add it to the list
quoteNumber = 0 ##so we know number we're are looping through

##create the actual window with tkinter
window = Tk() #to initialize the window
window.title("Quote Generator") #set title of the window
window.geometry("900x300")
window.grid_columnconfigure(0, weight=1) #makes first column take up more space if there is extra room available #give size of the window
window.resizable(False, False) ##this makes the window not resizable by the user ...the first argument determines whether the window can be resized horizontally, and the second determines whether the window can be resized vertically
window.configure(bg='grey')#configure method is used to set various options for the window, such as bg

##function that will get the quotes from the api 
def preload_quotes():
    global quotes
    ##get the quotes from the api
    print("***Loading more quotes***")

    for x in range(10): ##loop through the listed quotes
        random_quote = requests.get(api).json  ##get method for getting requets from the api inside the json file..via the request 
        content = random_quote["content"]
        author = random_quote["author"]
        quote = content + "\n\n" + "By" + author
        print(content)

        quotes.append(quote)  #append the quotes to the quote

    print("***Finished Loading more quotes!***") 

preload_quotes()

def get_random_quote():
    global quotes
    global quote_Label
    global quoteNumber

    quote_Label.configure(text=quotes[quoteNumber])
    quoteNumber = quoteNumber + 1
    print(quoteNumber)

    if quotes[quoteNumber] == quotes[-3]:
        thread =Thread(target=preload_quotes)
        thread.start()


#UI

##create a label widget to display the quote on the screen
quote_Label =  Label(window,
                     text="Click on the button to generate the Quote",
                     #width=30,
                       height=5,
                       wraplength=800, #this makes sure that if the quote exceeds this length, then it goes to next line
                       font=('Helvetica',20),
                       
                     )
quote_Label.grid(row=0,column=0,stick="WE", padx=10, pady=10)

##generate_button
generate_button = Button(window,
                         text="Generate",
                         padx=10,
                         pady=5,
                         bg="#0052cc",
                         fg="#ffffff",
                         font=('Helvetica',16,'bold'),
                         
                         #command=get_random_quote
                         )
generate_button.grid(row=1,column=0,sticky="WE", padx=10, pady=10) ## the stick attribute  allows us to specify which sides (N,S,E,W) ,we would like to place our widget,, WE to center it, between west and east, NS, between North and south. to center!


if __name__ == "__main__": #this makes sure that this code only runs if the script is run directly from this module(not imported)
    window.mainloop()



