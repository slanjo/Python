student_scores = {

    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,

}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇
def write_st_grades(key, value):
    student_grades[key] = value 
    
    
student_grades = {}
for key in student_scores:
    if student_scores[key] >= 91:
        write_st_grades(key, "Outstanding") 

    elif student_scores[key] >= 81:
        write_st_grades(key, "Exceeds Expectations") 

    elif student_scores[key] >= 71:
        write_st_grades(key, "Acceptable")

    else:
        write_st_grades(key, "Fail")

# 🚨 Don't change the code below 👇
print(student_grades)
