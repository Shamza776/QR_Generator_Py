'''##new file....Calculator
#calculator calculating two number inputs

userInput = int(input("Enter a valid  integer: ")) #get user input for the first number
userInput2 = int(input("Enter another valid integer: ")) #get second number from user
sign = ["*", "+", "-", "/"]
operator = int(input("Enter the number of operator you would like to use (1-Multiplication, 2-Addition, 3-Subtraction, 4-Div: "))
#operator = operator.isdigit()
def addition():
    if(userInput and userInput2 ):
        if(operator) :
            print("The sum is ", userInput + userInput2)
    else:
        print("Invalid character")
        return userInput and userInput2

def subtraction():
    if(userInput and userInput2 ):
        if(operator):
            print("The subtraction is ", userInput - userInput2)
    else:
        print("Invalid character")
        return userInput and userInput2

def multiplication():
    if(userInput and userInput2 ):
        if(operator):
            print("The product is ", userInput * userInput2)
    else:
        print("Invalid character")
        return userInput and userInput2

def division():
    if(userInput and userInput2 ):
        if(operator):
            print("The division is ", userInput / userInput2)
    else:
        print("Invalid character")
        return userInput and userInput2

def userEvaluation():
    print(userInput, end =  sign[operator -1 ] )
    print(userInput2 )
    #print(operator)
    if(operator == 1 ):
        multiplication()
    elif ( operator==2):
        addition()
    elif ( operator==3):
        subtraction()
    elif(operator == 4):
        division()
    else:
        print ("Invalid Operator Code Number")
        #return operator
userEvaluation() '''

####GUI CALCULATOR
from tkinter import *


def button_press(num):  ##to display whatever we are typing on the calculator screen.(label)
    global equation_text #access the global variable
    
    equation_text += str(num)   #adds what ever number/symbol we press, as a string
    equation_label.set(equation_text)#updates the label with new text


def equals(): #function to calculate our expression
    global equation_text

    try: ##if a wrong arithmetic problem is attempted..we can catch the error using try ..except  block
        total = str(eval(equation_text)) #pass the expression  and converts to a total and stores it as a string
        equation_label.set(total)       #displays the result in the label
        equation_text = total ##to newly display the total  instead of previous expression after pressing '='
          
    except ZeroDivisionError:
        equation_label.set('Math Error')
        equation_text = "" ##to  display blank after pressing '='

    except SyntaxError:
        equation_label.set("Syntax Error")
        equation_text="" ##to  display blank after pressing '='


def clear(): #function to clear our calculator
    global equation_text
    equation_label.set("") #is set to nothing.. display nothing when the button clear is pressed
    equation_text = ""      #the value of equation_text becomes empty

def backspace(): #function for backspace
    global  equation_text
    equation_text = equation_text[:-1]  #removes last character or takes everything befoe the last character
    equation_label.set(equation_text)

window = Tk()
window.title("Calculator")
window.geometry("500x600")

equation_text = ""

equation_label = StringVar()

label = Label(window,
               textvariable=equation_label, ##content on the label...text acquired from a variable--we use the textValiable attribute instead of text.
               font=("consolas", 20),
               background="white",
               width=24,
               height=2)
label.pack()  ##this is where the results will be diplayed

##we create all the buttons, and place them in a frame for easy  positioning
##a frame is used to hold a group of widgets
frame = Frame(window)
frame.pack()

button1 = Button(frame,
                 text=1,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(1))
button1.grid(row=0,  column=0)

button2 = Button(frame,
                 text=2,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(2))
button2.grid(row=0,  column=1)

button3 = Button(frame,
                 text=3,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,  column=2)

plus = Button(frame,
                 text="+",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("+"))
plus.grid(row=0,  column=3)

button4 = Button(frame,
                 text=4,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,  column=0)

button5 = Button(frame,
                 text=5,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,  column=1)

button6 = Button(frame,
                 text=6,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,  column=2)

minus = Button(frame,
                 text="-",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("-"))
minus.grid(row=1,  column=3)

button7 = Button(frame,
                 text=7,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,  column=0)

button8 = Button(frame,
                 text=8,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,  column=1)

button9 = Button(frame,
                 text=9,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,  column=2)

multiply = Button(frame,
                 text="*",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("*"))
multiply.grid(row=2,  column=3)

decimal = Button(frame,
                 text=".",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("."))
decimal.grid(row=3,  column=0)

button0 = Button(frame,
                 text=0,
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,  column=1)

division = Button(frame,
                 text="/",
                 height=4,
                 width=9,
                 font=35,
                 command=lambda: button_press("/"))
division.grid(row=3,  column=2)

equal = Button(frame,
                 text="=",
                 height=4,
                 width=9,
                 font=35,
                 command=equals)
equal.grid(row=3,  column=3)

clearButton = Button(window,
                 text="clear",
                 height=4,
                 width=12,
                 font=35,
                 command=clear)
clearButton.pack(side=LEFT)
backspaceButton = Button(window,
                 text="XX",
                 height=4,
                 width=12,
                 font=35,
                 command=backspace)
backspaceButton.pack(side=RIGHT)

window.mainloop()