# A CGPA Calculator using grades

print("==========CGPA CALCULATOR==========")
num_courses = int(input("Enter the number of courses taken this semester: "))

total_points = 0
total_units = 0

course_list = []
for i in range(1, num_courses + 1):
    course_title = input(f"\nEnter course title: ")
    # to not allow for repeating/duplicate courses
    while True:
        if course_title in course_list:
            print("You already entered this course. Please enter a different one.")
            course_title = input(f"\nEnter course title: ")
        else:
            break
    course_list.append(course_title)
    print(f"COURSE {i}, {course_title}: ")
    unit = int(input("Enter course unit: "))
    grade = input("Enter grade acquired in the course(in uppercase please): ")

    if grade == "A":
        grade_point = 5
    elif grade == "B":
        grade_point = 4
    elif grade == "C":
        grade_point = 3
    elif grade == "D":
        grade_point = 2
    elif grade == "E":
        grade_point = 1
    else:
        grade_point = 0

    course_point = grade_point * unit
    acheivable_course_point = 5 * unit
    total_points += course_point
    total_units += unit

    print(
        f"Course: {course_title},Grade point: {grade_point},Course point: {course_point}/{acheivable_course_point}")

# Actual CGPA calculation
cgpa = total_points / total_units
total_acheivable_course_point = 5 * total_units

print("\n==========RESULT==========")

print(f"Total points acquired during the semester: {total_points} ")
print(f"Total units offered during the semester: {total_units} ")

print(f"Current CGPA: {cgpa: .2f} ")

# classifying according to degree/class
if cgpa >= 4.50:
    classification = "First Class"
    message = "Congratulations!!! Outstanding Performance. Keep it up."
elif cgpa >= 3.50:
    classification = "Second Class Upper"
    message = "Well done !! Excellent performance. You have a solid foundation to improve further."
elif cgpa >= 2.40:
    classification = "Second Class Lower"
    message = "Good Effort! You can do better."
elif cgpa >= 1.50:
    classification = "Third Class"
    message = "There is room for improvement. Keep pushing forward"
else:
    classification = "Pass"
    message = "Not a good performace.Try harder next semester"

print(f"Class of Degree: {classification}")
print(message)
