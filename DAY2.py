# fees calculator
stype = input("Enter Student Type (MSDS, MSH, MGSD): ").strip().lower()
if stype not in ["msds", "msh", "mgsd"]:
    print("Invalid student type entered. Please enter MSDS, MSH, or MGSD.")
    exit()
while True:
    try:
        tuition = float(input("Enter Tuition Fee: "))
        break
    except:
        print("Invalid input! Please enter a numeric value.")
if stype == "msds":
    while True:
        try:
            college = float(input("Enter College Fee: "))
            break
        except:
            print("Invalid input! Please enter a numeric value.")
    hostel = 0
elif stype in ["msh", "mgsd"]:
    while True:
        try:
            hostel = float(input("Enter Hostel Fee: "))
            break
        except:
            print("Invalid input! Please enter a numeric value.")
    college = 0
if stype == "msds":
    total = tuition + college
elif stype == "msh":
    total = tuition + hostel
else: 
    total = 1.5 * tuition + hostel
print(f"Total Fee for {stype.upper()}: {total}")
# result:Enter Student Type (MSDS, MSH, MGSD): msds
#        Enter Tuition Fee: 6000
#        Enter College Fee: 7000
#        Total Fee for MSDS: 13000.0


# account balance
account_balance=50000
withdrawl_amount=int(input('enter the withdrawl amount='))
if (withdrawl_amount>account_balance):
    print('insufficiant fund')
elif (withdrawl_amount>10000):
    print('limit exceeded')
else :
    print('allow withdrawl')
# result
# enter the account balance=5000
# enter the withdrawl amount=5500
# insufficiant fund

# atm withdrawl
account_pin=9486
x=int(input('enter the pin='))
if(x==account_pin):
    print('pin is correct')
    withdrawl_amount=int(input('enter the withdrawl amount='))
    if (withdrawl_amount>account_balance):
        print('insufficiant fund')
    elif (withdrawl_amount>10000):
        print('limit exceeded')
    elif (withdrawl_amount<=0):
        print('invalid amount')
    else :
        print('allow withdrawl')
        balance_amount=account_balance-withdrawl_amount
        print('the balance amount is=',balance_amount)
else:
    print('wrong pin')
# result
# enter the pin=9486
# pin is correct
# enter the withdrawl amount=4000
# allow withdrawl
# the balance amount is=46000

# booking tickets
age=int(input('enter your age='))
show=input('enter the show time(mng,eve)=')
child=150
adult=250
senior=200
if (age<=4):
    print('free entry')
elif (age>=5) and (age<=16):
    if (show == "mng"):
        child_mng=child-50
        print('the ticket price is=',child_mng)
    else:
        print('the ticket price is=',child)

elif (age>=17) and (age<=59):
    if (show == "mng"):
        adult_mng=adult-50
        print('the ticket price is=',adult_mng)
    else:
        print('the ticket price is=',adult)
else:
    if (show == "mng"):
        senior_mng=senior-50
        print('the ticket price is=',senior_mng)
    else:
        print('the ticket price is=',senior)
# result:
# enter your age=21
# enter the show time(mng,eve)=mng
# the ticket price is= 200.0

# loop
odd_sum=0
for i in range(1,100,2):
    print(i)
    odd_sum=odd_sum+i
print('the number of odd sum is:',odd_sum)
# the number of odd sum is=2500
# for even
even_sum=0
for i in range(0,100,2):
    print(i)
    even_sum=even_sum+i
print('the sum of even number is=',even_sum)
# the sum of even number is= 2450
# for 5 tables
for i in range(5,55,5):
    print(i)

# marks calculation
english=int(input('enter the mark of english:'))
tamil=int(input('enter the mark of tamil:'))
maths=int(input('enter the mark of maths:'))
science=int(input('enter the mark of science:'))
social=int(input('enter the mark of social:'))
total_marks=english+tamil+maths+science+social
print('the total marks is=',total_marks)
average=total_marks/5
print('the average percentage is =',average)

# print 5 stars

for i in range(1,10):
    print("*"*i)

# reverse
for i in range(5,0,-1):
    print("*"*i)

# while loop
odd_sum=0
i=1
while i<100:
    print(i)
    odd_sum=odd_sum+i
    i=i+2
# for even
even_sum=0
i=2
while i<100:
    print(i)
    even_sum=even_sum+i
    i=i+2

# foe while stars
i=1
while i<6:
    print("*"*i)
    i=i+1

# # for reverse
i = 5
while i>0:
    print('*' * i)
    i =i-1
# while lopp for 5 multiplictaion
i = 5
while i<55:
    print(i)
    i =i+5

# bus seat booking
seats=10
booked_seat=[]
while seats>0:
    seat_number=int(input('enter your seat(1-10):'))
    if seat_number>seats or seat_number<=0:
        print('seat not available')
    else:
        name=input('enter your name:')
        booked_seat.append((seat_number,name))
        print(f"seat {seat_number} booked for {name}")
        seats=seats-1
if seats==0:
    print('all the seats are bookes')

