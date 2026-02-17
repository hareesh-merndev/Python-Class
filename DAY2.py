# Function to safely get a numeric input
def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Function to calculate fee based on student type
def calculate_fee(tuition_fee, college_fee, hostel_fee, student_type):
    student_type = student_type.lower()  # case-insensitive
    if student_type == "msds":
        return tuition_fee + college_fee
    elif student_type == "msh":
        return tuition_fee + hostel_fee
    elif student_type == "mgsd":
        return 1.5 * tuition_fee + hostel_fee
    else:
        return None  # invalid student type

# Input student type first
student_type = input("Enter Student Type (MSDS, MSH, MGSD): ").strip().lower()

# Input fees based on student type
tuition_fee = get_float("Enter Tuition Fee: ")

# Only ask for fees that are relevant
if student_type == "msds":
    college_fee = get_float("Enter College Fee: ")
    hostel_fee = 0  # Not needed
elif student_type in ["msh", "mgsd"]:
    hostel_fee = get_float("Enter Hostel Fee: ")
    college_fee = 0 if student_type == "msh" else 0  # College fee only needed for MSDS
else:
    print("Invalid student type entered. Please enter MSDS, MSH, or MGSD.")
    exit()  # Stop program if invalid type

# Calculate the total fee
total_fee = calculate_fee(tuition_fee, college_fee, hostel_fee, student_type)

# Display the result
print(f"Total Fee for {student_type.upper()}: {total_fee}")
