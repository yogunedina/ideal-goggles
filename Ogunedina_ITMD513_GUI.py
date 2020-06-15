'''
Author: Yewande Ogunedina
Class: ITMD 513
This Program uses tkinter GUI to create a program to input
the number of each type of coin a user has in their possession and then compute and display the
total dollar and cents value of these coins
'''

#import tkinter
from tkinter import *

#create function
#get user entry 
def user_input(entry):
    try:
        inputValue = int(entry.get())
        return inputValue
    except:
        return None

# create compute function
def compute():
    quarters = user_input(quartersInput)

    #if quarters is none or less than 0, return the dimes input 
    if quarters == None or quarters<0:
        errorField['text']='Invalid input (quarters)'
        return
    dimes = user_input(dimesInput)

    # dimes is none or less than 0 
    if dimes == None or dimes<0:
        errorField['text']='Invalid input(dimes)'
        return
    nickels = user_input(nickelsInput)

    # nickels is none or less than 0 
    if nickels == None or nickels < 0:
        errorField['text'] = 'Invalid input(nickels)'
        return
    #get input pennies from user 
    pennies = user_input(penniesInput)

    # check if pennies is none or pennies less than 0 
    if pennies == None or pennies <0:
        errorField['text'] = 'Invalid inputs(pennies)'
        return

    #update labels with with correct value
    quarters_output['text']='${:.2f}'.format(quarters*0.25)
    dimesOutput['text'] = '${:.2f}'.format(dimes * 0.10)
    nickelsOutput['text'] = '${:.2f}'.format(nickels * 0.05)
    penniesOutput['text'] = '${:.2f}'.format(pennies* 0.01)

    #reset the error field
    errorField['text'] = ''

    #calculate the total
    total=(quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01)
    totalOutput['text'] = '${:.2f}'.format(total)

#creating a tkinter window
root=Tk()

#set the root title window Change Counter
root.title('Change Counter')

#configure the columns in GUI
root.grid_columnconfigure(0, weight=1, uniform="abc")
root.grid_columnconfigure(1, weight=1, uniform="abc")
root.grid_columnconfigure(2, weight=1, uniform="abc")
root.grid_columnconfigure(3, weight=1, uniform="abc")

Label(root,text='Enter the number of each coin type and hit, Compute:').grid(row=0,column=0,columnspan=4)

#quarter value 
Label(root,text='Quarters:').grid(row=1,column=0)
quartersInput=Entry(root)
quartersInput.grid(row=1,column=1)

#create lable for quarter value 
Label(root,text='Quarter value:').grid(row=1,column=2)
quarters_output=Label(root)
quarters_output.grid(row=1,column=3)

#create a label for dime value
Label(root,text='Dimes:').grid(row=2,column=0)
dimesInput=Entry(root)
dimesInput.grid(row=2,column=1)

#create a label dime value
Label(root,text='Dime value:').grid(row=2,column=2)
dimesOutput=Label(root)
dimesOutput.grid(row=2,column=3)

# create a label for pennies
Label(root,text='Pennies:').grid(row=4,column=0)
penniesInput=Entry(root)
penniesInput.grid(row=4,column=1)

#create a label for penny value 
Label(root,text='Penny value:').grid(row=4,column=2)
penniesOutput=Label(root)
penniesOutput.grid(row=4,column=3)
Button(root,text='Compute',command= lambda:compute()).grid(row=5,column=0,columnspan=2)

#create a label for nickel value 
Label(root,text='Nickels:').grid(row=3,column=0)
nickelsInput=Entry(root)
nickelsInput.grid(row=3,column=1)

# create a label for nickel value
Label(root,text='Nickel value:').grid(row=3,column=2)
nickelsOutput=Label(root)
nickelsOutput.grid(row=3,column=3)

#create a label for total change value 
Label(root,text='Total Change value:').grid(row=5,column=2)
totalOutput=Label(root)
totalOutput.grid(row=5,column=3)
          
#label for showing errors
errorField=Label(root)
errorField.grid(row=6,column=0)
root.mainloop()
