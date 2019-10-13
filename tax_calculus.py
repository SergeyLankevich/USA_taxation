import math

# Declaring tax rates of the USA:
taxation_rate = [0.1, 0.15, 0.25, 0.28, 0.33, 0.35, 0.396]

# Declaring taxable annual income in the USA divided into steps by tax rates for different social groups.
single_subject = [9075, 36900, 89350, 186350, 405100, 406750, math.inf]
couple = [18150, 73800, 148850, 226850, 405100, 457600, math.inf]
single_parent = [12950, 49400, 127550, 206600, 405100, 432200, 432201, math.inf]

# Calculating user's annual income
annual_income = 0
for month in range(12):
    income = float(input())
    annual_income += income


def tax_calculation(taxation_steps):
    """
    :param taxation_steps: Taxable annual income in the USA divided into steps by tax rates.
    :return: Total tax sum paid.
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


# Defining user's category:
category = int(input())
if category == 1:
    tax_calculation(single_subject)
elif category == 2:
    tax_calculation(couple)
elif category == 3:
    tax_calculation(single_parent)
