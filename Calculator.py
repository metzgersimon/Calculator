import tkinter as tk
from tkinter import font as tk_font

# gui elements
root = tk.Tk(className='Calculator')
button_font = tk_font.Font(root=root, family='Times', size=20, weight='bold')
entry_font = tk_font.Font(root=root, family='Arial', size=20, weight='bold')
# represents the result of the users input
calculation = 0
# determines whether a calculation is already done or not
after_calculation = False
# checks if the ANS-button was pressed
ANS = False
# represents the last calculated result
ANS_calculation = 0


# method computes the result
def evaluate_calculation():
    global calculation
    # gets the text that is in the entry widget
    computation = result_text.get()
    if ANS:
        computation = computation.replace('ANS', str(ANS_calculation))
    # replaces the multiplication and division operator to be able to compute it
    computation = computation.replace('x', '*').replace('÷', '/')
    # compute the string using the eval function
    calculation = eval(computation)
    return calculation


# method is called when the equal-button is pressed to calculate and display the result
def equals():
    global calculation
    global after_calculation
    global ANS_calculation
    # computes the result with the inputted numbers
    calculation = evaluate_calculation()
    # displays the users input and the result
    result_text.set(result_text.get() + ' = ' + str(calculation))
    # set the variable after_calculation to True to clear the entry widget for future calculations
    after_calculation = True
    # stores the calculation in the ANS_calculation in case the ANS button will be pressed
    ANS_calculation = calculation
    calculation = 0


# method handles the AC-button. It clears the whole entry widget
def clear():
    global after_calculation
    global calculation
    after_calculation = False
    # clears both entry widgets
    result_text.set('')
    # resets the calculation
    calculation = 0
    return


# method creates all buttons needed
def create_buttons(frame):
    global button_font
    # list contains labels of all buttons
    button_list = ['7', '8', '9', 'DEL', 'AC', '4', '5', '6', 'x', '÷', '1', '2', '3', '+',
                   '-', '0', '.', '(-)', 'ANS', '=']
    # creates the buttons in the order of the list above
    row_index = 0
    column_index = 0
    for index in button_list:
        button = tk.Button(frame, text=str(index), font=button_font, width=5, height=3, foreground='white',
                           background='#193450', activebackground='#0E2C5F', activeforeground='white',
                           command=lambda index=index: pressed(index))
        # because one row should consists of five buttons, the column_index must be reset after the fifth button
        # is created in this row and the row_index must be set to the next row
        if column_index == 5:
            row_index += 1
            column_index = 0
        # buttons are organized in a grid with the corresponding row and column indices
        button.grid(row=row_index, column=column_index)
        # after one button is created, the next one should be in the next column
        column_index += 1
    frame.grid(rows=1, column=1)
    return frame


# method is called whenever a button is pressed
def pressed(button):
    global calculation
    global after_calculation
    global ANS
    # list of button-labels that should not be displayed in the entry-widget
    not_to_display = ['DEL', 'AC', '(-)', 'ANS', '=']
    # list of all possible operators
    operators_local = ['+', '-', 'x', '÷']
    # checks, if the given button should be displayed
    if button not in not_to_display:
        # checks, if the after_calculation variable is set to true. If so, the entry-widget should be cleared
        if after_calculation:
            # clear entry widget
            result_text.set('')
            # set the boolean to False again
            after_calculation = False
        # checks if the button is an operator
        if button in operators_local:
            text = result_text.get()
            # adds a 0 at the beginning if an operator is pressed before there is a number
            if len(text) == 0:
                result_text.set(0)
        # adds the pressed button to the entry-widget
        current_text = result_text.get()
        result_text.set(current_text + str(button))
    # if the pressed button is one of those which should not be displayed
    else:
        # the DEL-button deletes just the last character of the calculation
        if button == 'DEL':
            text = result_text.get()
            # removes the last character of the input string
            text = text[:-1]
            # resets the text
            result_text.set(text)
        # the AC-button clears the whole input field and sets the after_calculation variable to False
        elif button == 'AC':
            # calls the clear function
            clear()
        # this button should add an algebraic sign, if there is no number added yet
        elif button == '(-)':
            if result_text.get() == '':
                result_text.set('-')
                calculation *= -1
        # the ANS-button stores the last computed result as new number1 to be able to continue the calculation
        elif button == 'ANS':
            after_calculation = False
            result_text.set('ANS')
            ANS = True
        # the equal-button just calls the equals-method
        elif button == '=':
            # calls the equals function
            equals()
    return


# Create result window
result_text = tk.StringVar()
result_display = tk.Entry(root, font=entry_font, width=28, foreground='white',
                          background="#1E3E5E", textvariable=result_text)
result_display.grid(row=0, column=0, columnspan=5, padx=7, pady=5, ipady=15)
result_display.configure(state='normal')
# create the whole frame and start the mainloop
frame1 = tk.Frame(root)
button_frame = create_buttons(frame1)
root.mainloop()
