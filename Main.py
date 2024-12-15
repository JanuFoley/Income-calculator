def user_info():
    input_hours_worked = float(input("Enter the number of hours worked: "))
    input_hourly_income = int(input("Enter your hourly income: "))
    input_tax_percentage = int(input("Enter the percentage of income you pay in taxes: "))
    calculated_tax_percentage = input_tax_percentage * 0.01

    return input_hours_worked, input_hourly_income, calculated_tax_percentage


def income_calculator(input_hours_worked, calculated_tax_percentage, input_hourly_income):
    total_income = input_hours_worked * input_hourly_income
    income_lost = input_hours_worked * calculated_tax_percentage * input_hourly_income
    net_income = total_income - income_lost
    return net_income, total_income


user_hours_worked, user_hourly_income, final_true_tax_percentage = user_info()
final_net_income, final_total_income = income_calculator(user_hours_worked, final_true_tax_percentage,
                                                         user_hourly_income)

print("Your net income is ", final_net_income, "$")
input("Press enter to exit ")
