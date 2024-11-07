student = 0
student_passed = 0
total_grades = 0
grade = []

while True:
    grade_student = (input(f"Enter grade of student {student + 1} [type (done) if done]: "))
    if grade_student.replace('.','',1).isnumeric():
        grade_student = float(grade_student)
        if grade_student < 40 or grade_student > 100:
            print("Invalid grade. Please enter a number between 40 and 100.")
            break
        else:   
            grade.append(grade_student)
            student += 1
            if grade_student >= 75:
                student_passed += 1
                continue                                     
    elif grade_student.lower() == "done":
            average = sum(grade) / student
            passing_percent = student_passed / student  * 100 
            print(f"Average grade: {average:.2f}")
            print(f"Number of student passed: {student_passed}")
            print(f"Passing percentage: {passing_percent:.2f}%")
            break
    else:
        print("Invalid input. Please enter a number between 40 and 100.")
        break