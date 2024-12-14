import math


def user_info():
    hours_worked = float(input("Enter the number of hours worked: "))
    hourly_income = int(input("Enter your hourly income: "))
    tax_percentage = int(input("Enter the percentage of income you pay in taxes: "))
    true_tax_percentage = tax_percentage * 0.01

    return hours_worked, hourly_income, true_tax_percentage


def income_calculator(hours_worked, true_tax_percentage, hourly_income):
    total_income = hours_worked * hourly_income
    income_lost = hours_worked * true_tax_percentage * hourly_income
    net_income = total_income - income_lost
    return net_income, total_income

hours_worked, hourly_income, true_tax_percentage = user_info()
net_income, total_income = income_calculator(hours_worked, true_tax_percentage, hourly_income)

print("Your net income is ", net_income, "$")
