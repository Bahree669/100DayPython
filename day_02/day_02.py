""" 
TIP CALCULATOR
"""

greeting = 'Hello to the Tip Calculator'
print(greeting)
print('-' * len(greeting))

bill_total = float(input('Enter the total bill: $'))
tip_percentage = float(input('Tip percentage: '))
person = int(input('How many people to split the bill: '))

tip = (bill_total / person) * (tip_percentage / 100)
total_pay = int(tip) + bill_total / person
print('-' * len(greeting))
print(f"Each person should pay ${total_pay}")
