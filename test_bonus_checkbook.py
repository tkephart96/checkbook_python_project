# test checkbook script
# imports
import os
import subprocess
import json
import datetime as dt

# variables
# welcome the user
greeting = '~~~ Welcome to your terminal checkbook! ~~~'
# options
op0 = 'What would you like to do?'
op1 = '1) view current balance'
op2 = '2) record a debit (withdraw)'
op3 = '3) record a credit (deposit)'
op4 = '4) transaction history'
op5 = '5) exit'
options = ['', op0, '', op1, op2, op3, op4, op5, '']
# name of balance file
json_name = 'test_bonus_balance.json'
# time
time = dt.datetime.now()
time = str(time)
# trx type
trx_type = ['withdrawal','deposit']
# transaction format
trx_new = {'index':0, 'time':'', 'type':'', 'amount':0.00, 'balance':0.00}
trx_list = []
# app online
online = True

# functions
def balance_json():
    if os.path.exists(json_name) == False:
        trx_new.update({'time':time})
        trx_new.update({'type':'opened'})
        trx_list = []
        trx_list.append(trx_new)
        with open(json_name, 'w') as f:
            json.dump(trx_list, f)
    else:
        trx_list = json.load(open(json_name))
    return

def view_balance(file=json_name):
    bal = 0.00
    if len(trx_list) > 1:
        bal = trx_list[-1]['balance']
    if len(str(bal).split('.')[-1]) < 2:
        zero = 2 - len(str(bal).split('.')[-1])
        bal = str(bal) + ('0' * zero)
    return bal

def debit():
    while True:
        amount = input('\nHow much is the debit? $')
        try:
            amount = float(amount)
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
    trx_deb = trx_new
    trx_deb['index'] = trx_deb.get('index') + 1
    trx_deb.update({'time':time})
    trx_deb.update({'type':'withdrawal'})
    trx_deb.update({'amount':amount})
    trx_deb['balance'] = trx_deb.get('balance') - amount
    trx_list.append(trx_deb)
    with open(json_name, 'w') as f:
        json.dump(trx_list, f)
    return

def credit():
    while True:
        amount = input('\nHow much is the credit? $')
        try:
            amount = float(amount)
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
    trx_cred = trx_new
    trx_cred['index'] = trx_cred.get('index') + 1
    trx_cred.update({'time':time})
    trx_cred.update({'type':'deposit'})
    trx_cred.update({'amount':amount})
    trx_cred['balance'] = trx_cred.get('balance') + amount
    trx_list.append(trx_cred)
    print(trx_list)
    with open(json_name, 'w') as f:
        json.dump(trx_list, f)
    return

def history():
    hist = '\nTransaction history:'
    return hist

def goodbye():
    print('\nGoodbye! Have a nice day.\n')
    online = False
    return

# main code
print('\n', greeting)
while online == True:
    balance_json()
    for op in options:
        print(op)
    choice = input('Your choice? ')
    if choice.isdigit():
        choice = int(choice)
        if choice > 5:
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
            history()
        if choice == 5:
            goodbye()
    else:
        print('Invalid choice! Please choose a valid option.')
        continue
    break