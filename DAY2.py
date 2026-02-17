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


