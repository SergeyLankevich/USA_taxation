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
        #TODO: Sergey
        import en_local as loc
        break
    elif (language.lower() == 'russian' or language == '2' or language == '2.' or language.lower() == '1. russian' or
          language.lower() == 'ru' or language.lower() == 'rus'):
        import ru_local as loc
        break
    language = input('Please, choose language from proposed: ')

def non_negative(x):
    """

    :param x: the number
    :return: x if x > 0, else 0
    """
    if x >= 0: return x
    else: return 0

def single_subject(income):
    """

    :param income: user's annual income
    :return: tax amount
    """
    return round((non_negative(income - 406750) * 0.396 + non_negative(income % 406751 - 405100) * 0.35 +
            non_negative(income % 405101 - 186350) * 0.33 + non_negative(income % 186351 - 89350) * 0.28 +
            non_negative(income % 89351 - 36900) * 0.25 + non_negative(income % 36901 - 9075) * 0.15 +
            non_negative(income % 9076) * 0.1) * 100) / 100

def couple():
    #TODO: Sergey
    pass

def single_parent():
    #TODO: Sergey
    pass

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
    print(loc.TAX_AMOUNT, single_subject(income - tax_deductions))
elif category == 2:
    print(loc.TAX_AMOUNT, couple(income - tax_deductions))
elif category == 3:
    print(loc.TAX_AMOUNT, single_subject(income - tax_deductions))
