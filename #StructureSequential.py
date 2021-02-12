
""""
Resolution of a list of structure sequential python exercises

author lucas jesus de moura
lucas.j.m@outlook.com 
version: 0.2
"""
'''
Make a program that displays the message "Hello world" on the screen.
'''
def questionOne():
    return print('hello Word')

'''
Make a Program that asks for a number and then displays the message The number was "number".
'''
def questionTwo():
    number = input('type a number ') 
    return print ('The number entered was',number)

'''
Make a Program that asks for two numbers and prints the sum.
'''
def questionThree():
    firstValue = int(input('Type a number the first value '))
    secondValue = int(input('type a number the second value '))
    return print('The sum of the two numbers is equal to: ',firstValue+secondValue)

'''
Make a Program that asks for the 4 bimonthly notes and shows the mean.
'''
def questionFour():
    notes = input('Type four numbers with spaces (whole numbers integers) ').split()
    values = []
    for x in notes:
        values.append(int(x))
    return print('The notes mean is equal to:',sum(values)/4)
​
'''
Make a Program that converts meters to centimeters
'''
def questionFive():
    value = float(input())
    soma = value *1000/10
    return print(soma)

'''
Make a Program that asks how much you earn per hour and the number 
of hours worked in the month. Calculate and show your total salary for the month.
'''
def questionSix(): 
    valueHour = int(input('Enter the amount charged per hour '))
    hourWork = int(input('Enter the number of hours worked '))
    return print("His total salary is: ",valueHour*hourWork)

