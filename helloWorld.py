user_input = input("Enter some data: ") 
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
