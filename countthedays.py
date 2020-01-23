from datetime import date    

age = date.today()-date(1990,8,2)

days= (age.days)  
years= days / 365 
leap_years = years / 4 + 1
total_days = days + leap_years

print("Number of years and days is: ") 
print(total_days,("old"))
print(years,("old"))
print(leap_years,("leap years have passed"))




