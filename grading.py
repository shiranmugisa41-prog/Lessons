# Grading System Program

name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))

total = math + english + science
average = total / 3

# Determine Grade
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

# Pass/Fail
if average >= 50:
    result = "PASS"
else:
    result = "FAIL"

# Output
print("\n----- REPORT CARD -----")
print("name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)
print("Result:", result)