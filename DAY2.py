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
elif (age>=5) or (age<=16):
    if (show == "mng"):
        child_mng=0.5*child
        print('the ticket price is=',child_mng)
    else:
        print('the ticket price is=',child)

elif (age>=17) or (age<=59):
    if (show == "mng"):
        adult_mng=0.5*adult
        print('the ticket price is=',adult_mng)
    else:
        print('the ticket price is=',adult)
else:
    if (show == "mng"):
        senior_mng=0.5*senior
        print('the ticket price is=',senior_mng)
    else:
        print('the ticket price is=',senior)

