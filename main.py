"""Case-study #2 USA tax system
Developers:
Malakhov I. (xx%), Lankevich S. (xx%)"""

import math

# Declaring tax rates of the USA:
taxation_rate = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

# Declaring taxable annual income in USA divided in steps by tax rates for different social groups.
single_subject = [9075, 36900, 89350, 186350, 405100, 406750, math.inf]
couple = [18150, 73800, 148850, 226850, 405100, 457600, math.inf]
single_parent = [12950, 49400, 127550, 206600, 405100, 432200, math.inf]

# Choosing the language
language = input('Choose your language:\n1. Russian\n2. English')
while True:
    if (language.lower() == 'english' or language == '2' or language == '2.' or language.lower() == '2. english' or
        language.lower() == '2.english' or language.lower() == 'en' or language.lower() == 'eng'):
        import en_local as loc

        break
    elif (language.lower() == 'russian' or language == '1' or language == '1.' or language.lower() == '1. russian' or
          language.lower() == '1.russian' or language.lower() == 'ru' or language.lower() == 'rus'):
        import ru_local as loc

        break
    language = input('Please, choose language from proposed: ')


# Choosing the social category
def social_category():
    """
    :return: User's current social category
    """
    print(loc.CATEGORY_INPUT)
    category = input()
    while True:
        try:
            category = int(category)
        except ValueError:
            category = input(loc.INPUT_CORRECT_CATEGORY)
        else:
            if category != 1 and category != 2 and category != 3:
                category = input(loc.INPUT_CORRECT_CATEGORY)
            else:
                return category


# Annual income input (by month)
def income_counter():
    """
    :return: Total user's annual income
    """
    total_income = 0
    for month in loc.MONTH_LIST:
        income = input(loc.INPUT_INCOME + month)
        while True:
            try:
                income = int(income)
            except ValueError:
                income = input(loc.INPUT_CORRECT_INCOME)
            else:
                total_income += income
                break
    return total_income


# Setting tax deduction
def tax_deduction():
    """
    :return: Tax deductions
    """
    tax_deductions = input(loc.INPUT_TAX_DEDUCTIONS)
    while True:
        try:
            tax_deductions = int(tax_deductions)
        except ValueError:
            tax_deductions = input(loc.INPUT_CORRECT_TAX_DEDUCTIONS)
        else:
            return tax_deductions


# Calculating taxable part of income
def taxable_sum(total_income, tax_deductions):
    """
    :param total_income: Total user's annual income
    :param tax_deductions: Tax deductions
    :return: Taxable part of user's annual income (after tax deduction)
    """
    annual_income = total_income - tax_deductions
    if annual_income <= 0:
        print(loc.TD_MORE_THEN_INC)
        exit()
    else:
        return annual_income


def tax_calculation(annual_income, taxation_steps):
    """
    :param annual_income: Taxable part of user's annual income (after tax deduction)
    :param taxation_steps: Taxable annual income in USA divided in steps by tax rates.
    :return: Amount of tax paid.
    """
    for i in taxation_steps:
        if i >= annual_income:
            step = taxation_steps.index(i)
            break

    if step == 0:
        total_sum = taxation_rate[step] * (annual_income - 0)
        return total_sum
    else:
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
    category = social_category()
    if category == 1:
        print(loc.TAX_AMOUNT, tax_calculation(taxable_sum(income_counter(), tax_deduction()), single_subject))
    elif category == 2:
        print(loc.TAX_AMOUNT, tax_calculation(taxable_sum(income_counter(), tax_deduction()), couple))
    elif category == 3:
        print(loc.TAX_AMOUNT, tax_calculation(taxable_sum(income_counter(), tax_deduction()), single_parent))


main()
