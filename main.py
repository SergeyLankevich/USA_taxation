"""Case-study #2 USA tax system
Developers:
Malakhov I. (xx%), Lankevich S. (xx%)"""

print('Please, choose language:')
print('1. English')
print('2. Russian')
language = input()
while True:
    if (language.lower() == 'english' or language == '1' or language == '1.' or language.lower() == '1. english' or
        language.lower() == 'en' or language.lower() == 'eng'):
        import en_local as loc
        break
    elif (language.lower() == 'russian' or language == '2' or language == '2.' or language.lower() == '1. russian' or
          language.lower() == 'ru' or language.lower() == 'rus'):
        import ru_local as loc
        break
    language = input('Please, choose language from proposed: ')

import math

# Declaring tax rates of the USA:
taxation_rate = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

# Declaring taxable annual income in USA divided in steps by tax rates for different social groups.
single_subject = [9075, 36900, 89350, 186350, 405100, 406750, math.inf]
couple = [18150, 73800, 148850, 226850, 405100, 457600, math.inf]
single_parent = [12950, 49400, 127550, 206600, 405100, 432200, math.inf]

def tax_calculation(annual_income, taxation_steps):
    """
    :param taxation_steps: Taxable annual income in USA divided in steps by tax rates.
    :return: Amount of tax paid.
    """
    for i in taxation_steps:
        if i == annual_income or i > annual_income:
            step = taxation_steps.index(i)
            break

    initial_taxation = taxation_rate[step] * (annual_income - taxation_steps[step - 1])
    second_sum = 0

    for k in range(1, step + 1):
        if step - k >= 1:
            second_sum += taxation_rate[step - k] * (taxation_steps[step - k] - taxation_steps[step - k - 1])
        else:
            second_sum += taxation_rate[step - k] * (taxation_steps[step - k] - 0)
    total_sum = initial_taxation + second_sum
    return total_sum

def main():
    income = input(loc.INPUT_INCOME)
    while True:
        try:
            income = int(income)
        except ValueError:
            income = input(loc.INPUT_CORRECT_INCOME)
        else:
            break


    tax_deductions = input(loc.INPUT_TAX_DEDUCTIONS)
    while True:
        try:
            tax_deductions = int(tax_deductions)
        except ValueError:
            tax_deductions = input(loc.INPUT_CORRECT_TAX_DEDUCTIONS)
        else:
            break

    print(loc.CATEGORIES)
    print(loc.CATEGORY_1)
    print(loc.CATEGORY_2)
    print(loc.CATEGORY_3)

    category = input()
    while True:
        while True:
            try:
                category = int(category)
            except ValueError:
                category = input(loc.INPUT_CORRECT_CATEGORY)
            else:
                break
        if category != 1 and category != 2 and category != 3:
            category = input(loc.INPUT_CORRECT_CATEGORY)
        else: break


    if category == 1:
        print(tax_calculation(income, single_subject))
    elif category == 2:
        print(tax_calculation(income, couple))
    elif category == 3:
        print(tax_calculation(income, single_parent))

main()