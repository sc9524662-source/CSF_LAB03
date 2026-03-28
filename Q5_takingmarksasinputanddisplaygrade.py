#5. Program to take marks as input and display grade
marks = int(input("Enter marks: "))
grade = ""
if marks >= 80:
    grade = "A"
else:
     if marks >= 60:
       grade = "B"
     else : 
       if marks >= 40:
        grade = "C"
       else:
        grade = "Fail"
print(f"Grade {grade}")
