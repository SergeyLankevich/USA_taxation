import ru_local as loc

def non_negative(x):
    if x >= 0: return x
    else: return 0

def single_subject(income):
    return round((non_negative(income - 406750) * 0.396 + non_negative(income % 406751 - 405100) * 0.35 +
            non_negative(income % 405101 - 186350) * 0.33 + non_negative(income % 186351 - 89350) * 0.28 +
            non_negative(income % 89351 - 36900) * 0.25 + non_negative(income % 36901 - 9075) * 0.15 +
            non_negative(income % 9076) * 0.1) * 100) / 100

def couple():
    pass

def single_parent():
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
