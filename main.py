house_price: int = int(input("What is the price of your house?\n>"))
tax_price: int = int(input("What is the monthy tax price?\n>"))
insurance: int = int(input("How much is insurance, monthy?\n>"))
percent: int = int(input("How much of the total is the bank making you pay? (percent, 1-100)\n>"))
interest_rate: int = int(input("What is the interest rate?\n>"))
real_interest_rate: int = interest_rate  # fixme

loan_amount: int =  house_price * (percent / 100)
print(f"The loan amount is {loan_amount}.")
difference_of_price: int = house_price - loan_amount
print(f"The difference in price is {difference_of_price}")
base_monthly: int = (difference_of_price / 1000) * real_interest_rate
print(f"The cost before holding costs is {base_monthly}")
with_holdings: int = base_monthly + tax_price + insurance
print(f"The cost after holding costs is {with_holdings}")