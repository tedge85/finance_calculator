# This is a program that calculates interest paid on an investment or bond, depending on which option is selected.

import math

# Introduction of service to user:
print('investment - to calculate the amount of interest you\'ll earn on your investment')
print('bond - to calculate the amount you\'ll have to pay on a home loan')

# Option to choose calculation service. Input saved as 'choice'
choice = input('\n\nEnter either \'investment\' or \'bond\' from the menu above to proceed: ')

# 0ptions to choose the service variables for an investment
if choice.lower() == 'investment':
    deposit = input('Please enter the amount of money you wish to deposit: ')
    interest = input('Please enter the interest rate as a percentage (number only): ')
    years = input('Please enter the number of years that you plan on investing: ')
    simple_comp = input('Please enter whether you would like a \'simple\' or \'compound\' investment: ')
    P = int(deposit)
    r = int(interest) / 100
    t = int(years)

    # Control structure that calculates output if 'simple' investment chosen
    if simple_comp.lower() == 'simple':
        A = round(P * (1 + r*t), 2)
        print(f'Your total with simple interest is {A} pounds')

    # Control structure that calculates output if 'compound' investment chosen
    elif simple_comp.lower() == 'compound':
        A = round(P * math.pow((1+r),t), 2)
        print(f'Your total with compound interest is {A} pounds')

# Control structure that decides output if 'bond' chosen
elif choice.lower() == 'bond':
    value = input('Please enter the present value of the house (without currency sign): ')
    interest = input('Please enter the interest rate as a percentage (number only): ')
    months = input('Please enter the number of months that you plan to take to repay the bond: ')
    i = (int(interest) / 100) / 12
    P = int(value)
    n = int(months)
    total = round((i * P) / (1 - (1 + i) ** (-n)), 2)
    print(f'Your monthly repayment is {total} pounds')
