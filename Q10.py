#This code gives grades according to marks scored.
total_marks = float(input("Enter your marks (0 to 100): "))

if 91 <= total_marks <= 100:
    grade = "A1"
elif 81 <= total_marks <= 90:
    grade = "A2"
elif 71 <= total_marks <= 80:
    grade = "B1"
elif 61 <= total_marks <= 70:
    grade = "B2"
elif 41 <= total_marks <= 60:
    grade = "C"
elif 33 <= total_marks <= 40:
    grade = "D"
elif 00 <= total_marks <= 32:
    grade = "E"
else:
    grade = "Invalid marks entered" 

print(f"Your marks is: {total_marks}\nYour grade is: {grade}")