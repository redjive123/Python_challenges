Student_ID = input("Enter Student ID: ")
Email_ID = input("Enter Email ID: ")
Password = input("Enter Password: ")
Referral_Code = input("Enter Referral Code: ")
valid = False
#Student ID
if len(Student_ID) != 7:
    valid = False
elif Student_ID[0:3] != "CSE":
    valid = False
elif Student_ID[3] != "-":
    valid = False
elif not Student_ID[4].isdigit():
    valid = False
elif not Student_ID[5].isdigit():
    valid = False
elif not Student_ID[6].isdigit():
    valid = False
#Email
elif "@" not in Email_ID and "." not in Email_ID:
    valid = False
elif Email_ID[0] == "@" and Email_ID[-1] == "@":
    valid = False
elif Email_ID[-4:] != ".edu":
    valid = False
#Password
elif len(Password) < 8:
    valid = False
elif not Password[0].isupper():
    valid = False
elif not Password[0].isalpha():
    valid = False
elif not ("0" in Password or "1" in Password or "2" in Password or "3" in Password or "4" in Password or
          "5" in Password or "6" in Password or "7" in Password or "8" in Password or "9" in Password):
    valid = False
#Referral Code
elif len(Referral_Code) != 6:
    valid = False
elif Referral_Code[0:3] != "REF":
    valid = False
elif not Referral_Code[3].isdigit():
    valid = False
elif not Referral_Code[4].isdigit():
    valid = False
elif Referral_Code[5] != "@":
    valid = False
else:
    valid = True
#Output
if valid == True:
    print("APPROVED")
else:
    print("REJECTED")
