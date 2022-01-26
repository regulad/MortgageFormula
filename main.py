from locale import setlocale, format_string, LC_ALL

setlocale(LC_ALL, '')

house_price: int = int(input("What is the price of your house?\n>"))
tax_price: int = int(input("What is the monthy tax price?\n>") or "1000")
insurance: int = int(input("How much is insurance, monthy?\n>") or "100")
percent: int = int(input("How much of the total is the bank making you pay? (percent, 1-100)\n>") or "20")
interest_rate: int = int(input("What is the interest rate?\n>") or "6")
years: int = int(input("How many years is this loan?\n>") or "30")
real_interest_rate: int = interest_rate  # fixme

loan_amount: int =  house_price * (percent / 100)
print(f"The cost of the house is ${format_string('%d', round(house_price), grouping=True)}.")
print(f"The monthly tax prices are ${format_string('%d', round(tax_price), grouping=True)}.")
print(f"The cost of insurance on the house is ${format_string('%d', round(insurance), grouping=True)}.")
print(f"The interest rate on the loan is {round(interest_rate)}%.")
print(f"If {round(percent)}% is paid upfront over the course of {round(years)} years,")
print(f"The loan amount is ${format_string('%d', round(loan_amount), grouping=True)}.")
difference_of_price: int = house_price - loan_amount
print(f"The difference in price is ${format_string('%d', round(difference_of_price), grouping=True)}.")
base_monthly: int = (difference_of_price / 1000) * real_interest_rate
print(f"The cost before holding costs per month is ${format_string('%d', round(base_monthly), grouping=True)}.")
with_holdings: int = base_monthly + tax_price + insurance
print(f"The cost after holding costs per month is ${format_string('%d', round(with_holdings), grouping=True)}.")
