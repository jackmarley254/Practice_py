#!/usr/bin/python3

# Use this exchange rate

NAIRA_PER_DOLLAR = 410.59 # exchange rate as of Nov 10 2021

USD_Value = float(input("Enter amount of USD to convert to NGN: "))
Naira_Value = USD_Value * NAIRA_PER_DOLLAR
print(f"{USD_Value} is {Naira_Value:.2f} NGN")
