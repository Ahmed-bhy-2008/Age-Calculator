from datetime import date
print("--- welcome to the age calculator application ---")

# 1. Get birth details from user
birth_year = int(input("Enter birth year (YYYY): "))
birth_month = int(input("Enter birth month (1-12): "))
birth_day = int(input("Enter birth day (1-31): "))

# 2. Get today's date
today=date.today()
birth_date=date(birth_year , birth_month , birth_day)

# 3. Calculate preliminary age
age_in_days =(today-birth_date).days
age_in_years=age_in_days//365
remaining_days=age_in_days%365

print(f"Your exact age is: {age_in_years} years old and {remaining_days} day.")