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
else:  # mgsd
    total = 1.5 * tuition + hostel

print(f"Total Fee for {stype.upper()}: {total}")

# account balance
account_balance=int(input('enter the account balance='))
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

