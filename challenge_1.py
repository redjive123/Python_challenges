full_name = input("Enter Full Name: ")
email = input("Enter Email ID: ")
mobile = input("Enter Mobile Number: ")
age = int(input("Enter Age: "))
valid = True
# 1. Full Name Validation
a=len(full_name)
if full_name[0]==" " or full_name[a-1]==" ":
    valid = False
elif full_name.count(" ") < 1:
    valid = False
# 2. Email Validation
elif "@" not in email or "." not in email:
    valid = False
elif email[0] == "@":
    valid = False
# 3. Mobile Number Validation
elif len(mobile) != 10:
    valid = False
elif not mobile.isdigit():
    valid = False
elif mobile[0] == "0":
    valid = False
# 4. Age Validation
elif age < 18 or age > 60:
    valid = False
if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")
