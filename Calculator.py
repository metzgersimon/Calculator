import tkinter as tk
from tkinter import font as tkFont

# global variables
root = tk.Tk(className='Calculator')
button_font = tkFont.Font(root=root, family='Times', size=20, weight='bold')
entry_font = tkFont.Font(root=root, family='Arial', size=25, weight='bold')
calculation = ''
operator = ''
number1 = ''
number2 = ''
# determines whether a calculation is already done or not
after_calculation = False
# checks if the ANS-button was pressed
ANS = False


# Sets the global operator to the operator currently used
def add_operator(operator_local):
    global operator
    operator = operator_local
    return


# This method does the actual calculation using the basic math operators
def simple_mathematical_operations():
    global calculation
    global operator
    global number1
    global number2
    number1 = float(number1)
    number2 = float(number2)
    if operator == '+':
        calculation = number1 + number2
    elif operator == '-':
        calculation = number1 - number2
    elif operator == 'x':
        calculation = number1 * number2
    elif operator == '÷':
        calculation = number1 / number2
    return calculation


# method is called when the equal-button is pressed to calculate and display the result
def equals():
    # get needed global variables
    global number1
    global number2
    global operator
    global calculation
    global after_calculation

    # get the input of the entry widget and split it into number1, number2 and operator
    calculation_text = result_text.get()
    element_list = calculation_text.split(operator)
    # need to consider whether the ANS-button is pressed or not. If that is the case the last result needs to
    # be set as number1 of the next calculation, which is handled in the pressed-method
    if not ANS:
        number1 = element_list[0]
    number2 = element_list[1]
    # computes the result with the inputted numbers and display the output
    calculation = simple_mathematical_operations()
    result_text.set(calculation)
    # set the variable after_calculation to True to clear the entry widget for future calculations
    after_calculation = True


# method handles the AC-button. It clears the whole entry widget
def clear():
    global calculation
    result_text.set('')
    return


# method creates all buttons needed
def create_buttons(frame):
    global button_font
    # list contains labels of all buttons
    button_list = ['7', '8', '9', 'DEL', 'AC', '4', '5', '6', 'x', '÷', '1', '2', '3', '+',
                   '-', '0', '.', '(-)', 'ANS', '=']
    # 273141
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
    global number1
    global calculation
    global after_calculation
    global ANS
    # list of button-labels that should not be displayed in the entry-widget
    not_to_display = ['DEL', 'AC', '(-)', 'ANS', '=']
    # list of all possible operators
    operators = ['+', '-', 'x', '÷']
    # checks, if the given button should be displayed
    if button not in not_to_display:
        # checks, if the after_calculation variable is set to true. If so, the entry-widget should be cleared
        if after_calculation:
            result_text.set('')
            after_calculation = False
        # checks if the button is an operator
        if button in operators:
            text = result_text.get()
            # adds a 0 at the beginning if an operator is pressed before there is a number
            if len(text) == 0:
                result_text.set(0)
            add_operator(button)
        # adds the pressed button to the entry-widget
        current_text = result_text.get()
        result_text.set(current_text + str(button))
    # if the pressed button is one of those which should not be displayed
    else:
        # the DEL-button deletes just the last character of the calculation
        if button == 'DEL':
            text = result_text.get()
            text = text[:-1]
            result_text.set(text)
        # the AC-button clears the whole input field and sets the after_calculation variable to False
        elif button == 'AC':
            result_text.set('')
            after_calculation = False
        # this button should add an algebraic sign, if there is no number added yet
        elif button == '(-)':
            if result_text.get() == '':
                result_text.set('-')
        # the ANS-button stores the last computed result as new number1 to be able to continue the calculation
        elif button == 'ANS':
            after_calculation = False
            result_text.set('ANS')
            ANS = True
            number1 = calculation
        # the equal-button just calls the equals-method
        elif button == '=':
            equals()
    return


# Create result window
result_text = tk.StringVar()
result_display = tk.Entry(root, font=entry_font, width=24, foreground='white',
                          background="#1E3E5E", textvariable=result_text)
result_display.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipady=15)
result_display.configure(state='normal')

# create the whole frame and start the mainloop
frame1 = tk.Frame(root)
button_frame = create_buttons(frame1)
root.mainloop()
