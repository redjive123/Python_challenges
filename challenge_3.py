n = int(input("Enter number of students: "))
marks = [0] * n
for i in range(n):
    marks[i] = int(input("Enter marks: "))
valid_count = 0
fail_count = 0
for mark in marks:
    if mark < 0 or mark > 100:
        print(str(mark) + " → Invalid")
    elif mark >= 90:
        print(str(mark) + " → Excellent")
        valid_count = valid_count + 1
    elif mark >= 75:
        print(str(mark) + " → Very Good")
        valid_count = valid_count + 1
    elif mark >= 60:
        print(str(mark) + " → Good")
        valid_count = valid_count + 1
    elif mark >= 40:
        print(str(mark) + " → Average")
        valid_count = valid_count + 1
    else:
        print(str(mark) + " → Fail")
        valid_count = valid_count + 1
        fail_count = fail_count + 1
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)
