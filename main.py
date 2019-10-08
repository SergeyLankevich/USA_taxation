annual_income = int(input())

# for single subject
if 0 < annual_income <= 9075:
    print(annual_income * 0.1)
elif 9076 <= annual_income <= 36900:
    print(annual_income * 0.15)
elif 36901 <= annual_income <= 89350:
    print(annual_income * 0.25)
elif 89351 <= annual_income <= 186350:
    print(annual_income * 0.28)
elif 186351 <= annual_income <= 405100:
    print(annual_income * 0.33)
elif 405101 < annual_income <= 406750:
    print(annual_income * 0.35)
elif 406751 <= annual_income:
    print(annual_income * 0.396)

# for a couple
if 0 < annual_income <= 18150:
    print(annual_income * 0.1)
elif 18151 <= annual_income <= 73800:
    print(annual_income * 0.15)
elif 73801 <= annual_income <= 148850:
    print(annual_income * 0.25)
elif 148851 <= annual_income <= 226850:
    print(annual_income * 0.28)
elif 226851 <= annual_income <= 405100:
    print(annual_income * 0.33)
elif 405101 < annual_income <= 457600:
    print(annual_income * 0.35)
elif 457601 <= annual_income:
    print(annual_income * 0.396)

# for a single parent
if 0 < annual_income <= 12950:
    print(annual_income * 0.1)
elif 12951 <= annual_income <= 49400:
    print(annual_income * 0.15)
elif 49401 <= annual_income <= 127550:
    print(annual_income * 0.25)
elif 127551 <= annual_income <= 206600:
    print(annual_income * 0.28)
elif 206601 <= annual_income <= 405100:
    print(annual_income * 0.33)
elif 405101 < annual_income <= 432200:
    print(annual_income * 0.35)
elif 432201 <= annual_income:
    print(annual_income * 0.396)



