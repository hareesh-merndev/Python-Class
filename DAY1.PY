APple=10
print(APple)
# data type (4 types)
# int, float, str, bool
# question1 , age calculator
birth_year=2005
Current_year=2026
age=Current_year-birth_year
print('age=',age)
# result = age=21
# food amount calculation
Current_age=21
Maximum_age=70
Amount=200
remaining_year=Maximum_age-Current_age
total_amount=remaining_year*365*Amount
print('total amount of amount=',total_amount,'at the year of =',remaining_year)
# result:total amount of amount= 3577000 at the yaer of = 49
# water consumption 
waater_drink=5
total_water=remaining_year*365*waater_drink
print('total amount of water=',total_water,'at the year of =',remaining_year)
# result:total amount of water= 89425 at the yaer of = 49
# car fuel
total_km=567
car_mileage=23
cost_per_ltr=102
total_fuel_want=total_km/car_mileage
total_cost=total_fuel_want*cost_per_ltr
print('needed fuel per liter=',total_fuel_want,'at the cost of=',total_cost)
# result:needed fuel per liter= 24.652173913043477 at the cost of= 2514.5217391304345
# data usgae
data_usage=2
no_of_days=32
monthly_usage=data_usage*no_of_days
print('no of data used per month=',monthly_usage)
# Result: no of data used per month= 64
# age in days
Current_age=21
age_live=Current_age*365
print('the age i can line is ',age_live)
# Result: the age i can line is 7665
# shopping discount
og_price=1300
discount=12
discount_price=og_price*discount/100
discount_og=og_price-discount_price
print('the discounted price is',discount_og)
# Result: the discounted price is 1144.0
# Topic: Number Comparison
x=int(input('enter a number of x='))
y=int(input('enter a number of y='))
if (x==y):
    print('x and y are same')
elif (x>y):
    print('x is grater than y')
else:
    print('x is smaller than y')
# result: enter a number of x=5
#         enter a number of y=6
#         x is smaller than y
# Topic: Vowel or Consonant
x=input('enter a word=')
if (x=="a" or x=="e" or x=="i" or x=="o" or x=="u"):
    print('it is a vowel')
else:
    print("it is a consonent")
# result : enter a word=i
#          it is a vowel
    # que 3
x=int(input('enter your mark'))
if (x>=90 and x<=99):
    print('your rank is A')
elif (x>=80 and x<=89):
    print('your rank is B')
elif (x>=70 and x<=79):
    print('your rank is C')
elif (x>=60 and x<=69):
    print('your rank is D')
elif (x>=50 and x<=59):
    print('your rank is E')
else:
    print('your rank is fail')
    # profit and loss
x = int(input('Enter the cost price of 1 dozen = '))
y = int(input('Enter the selling price of 1 item = '))
selling_price_dozen = y * 12
if selling_price_dozen > x:
    profit = selling_price_dozen - x
    print('It is profit of Rs.', profit)
elif selling_price_dozen < x:
    loss = x - selling_price_dozen
    print('It is loss of Rs.', loss)
else:
    print('No profit, no loss.')

