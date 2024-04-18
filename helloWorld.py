user_input = input("Enter your name: ") 
print("You entered:", user_input) 

from datetime import datetime


def calculate_age(birth_date_str):
    try:
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - birth_date.year - ((current_date.month, current_date.day) < (birth_date.month, birth_date.day))
        return age
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

birth_date_str = input("Enter your date of birth (YYYY-MM-DD): ")
age = calculate_age(birth_date_str)
if age is not None:
    print("Your age is:", age)


    def convert_currency(amount_str, exchange_rate_str):
        try:
            amount = float(amount_str)
            exchange_rate = float(exchange_rate_str)
            converted_amount = amount * exchange_rate
            return converted_amount
        except ValueError:
            print("Invalid input. Please enter a valid number.")


currency_from = input("Enter the currency you want to convert from: ")
currency_to = input("Enter the currency you want to convert to: ")
exchange_rate_str = input("Enter the exchange rate: ")
amount_str = input("Enter the amount you want to convert: ")

converted_amount = convert_currency(amount_str, exchange_rate_str)
if converted_amount is not None:
    print(f"{amount_str} {currency_from} is equal to {converted_amount} {currency_to}")

