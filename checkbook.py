# test checkbook script
# imports
import os
import subprocess

# variables
# welcome the user
greeting = '~~~ Welcome to your terminal checkbook! ~~~'
# options
op0 = 'What would you like to do?'
op1 = '1) view current balance'
op2 = '2) record a debit (withdraw)'
op3 = '3) record a credit (deposit)'
op4 = '4) exit'
options = ['', op0, '', op1, op2, op3, op4, '']
# name of balance file
filename = 'balance.txt'
# app online
online = True

# functions
# handle commas
def handle_commas(s):
    return float(s.replace(',',''))

def balance():
    if os.path.exists(filename) == False:
        with open(filename, 'w') as f:
            f.write('0.00')

def view_balance(file=filename):
    with open(file) as f:
        data = f.read()
        return data

def debit():
    while True:
        amount = input('\nHow much is the debit? $')
        try:
            amount = handle_commas(amount)
            if len(str(amount).split('.')[-1]) > 2:
                print('Invalid amount! Please enter an amount.')
                continue
            if amount < 0.01:
                print('Invalid amount! Please enter an amount.')
                continue
        except ValueError:
            print('Invalid amount! Please enter an amount.')
            continue
        break
    withdraw = float(view_balance()) - amount
    if len(str(withdraw).split('.')[-1]) < 2:
        zero = 2 - len(str(withdraw).split('.')[-1])
        withdraw = str(withdraw) + ('0' * zero)
    with open(filename, 'w') as f:
        f.write(str(withdraw))
    return

def credit():
    while True:
        amount = input('\nHow much is the credit? $')
        try:
            amount = handle_commas(amount)
            if len(str(amount).split('.')[-1]) > 2:
                print('Invalid amount! Please enter an amount.')
                continue
            if amount < 0.01:
                print('Invalid amount! Please enter an amount.')
                continue
        except ValueError:
            print('Invalid amount! Please enter an amount.')
            continue
        break
    deposit = float(view_balance()) + amount
    if len(str(deposit).split('.')[-1]) < 2:
        zero = 2 - len(str(deposit).split('.')[-1])
        deposit = str(deposit) + ('0' * zero)
    with open(filename, 'w') as f:
        f.write(str(deposit))
    return

def goodbye():
    print('\nGoodbye! Have a nice day.\n')
    online = False
    return

# main code
print('\n', greeting)
while online == True:
    balance()
    for op in options:
        print(op)
    choice = input('Your choice? ')
    if choice.isdigit():
        choice = int(choice)
        if choice > 4:
            print('Invalid choice! Please choose a valid option.')
            continue
        if choice == 1:
            print(f'\nYour current balance is ${view_balance()}')
            continue
        if choice == 2:
            debit()
            continue
        if choice == 3:
            credit()
            continue
        if choice == 4:
            goodbye()
    else:
        print('Invalid choice! Please choose a valid option.')
        continue
    break