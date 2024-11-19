# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[0]['Combo,Name'])
# print(students[0]['Email'][0])
# print(students[0]['Email'][1])

# # for loops allow us to
# #iterate through the data
# #and perform some function

# #we are iterating through the data
# #and printing the name and email of the students
# #we are also printing a line of underscores to separate the students
# #we are also printing a line of underscores to separate the students
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print(students['HR'])
#     print("_"*25)


# we are asking the user to input their name
# then we are checking if the name is in the data
# if the name is in the data we are printing the name and "this works"
# id = int(input("what is you id?"))
# for student in students:
#     if id == student['CPSID']:
#         print(student['CPSID'])
#         print("this works")


# Let's try to print out the emails of the students:    





################################################################################################################
# # 3.)
# name = input("What is your first name")
# for student in students:
#     if name == student[ "FName"]:
#         print(student["HR"])
#         print("YAY!")
   
################################################################################################################
# # 4.)
# for student in students:
#     if 10 == student['GL']:
#         print (student["Combo,Name"],student['CPSID'])

###############################################################################################################
# # Slide 3 
for student in students:
    if student['CPSID'] == 10000046:
         student['LName'] = "Aguayo",
         student["FName"] = "Giovanni",
print(f"Updated student: {student}") 

###############################################################################################################
# Sldie 4
# Update the dataset in memory (e.g., modify student details)
for student in students:
    if student['CPSID'] == 10000011:  # Example CPSID to update
      student['FName'] = 'UpdatedKaren'
      student['LName'] = 'UpdatedAnderson'
    
# Overwrite the `student_data.py` file with the updated data
with open('student_data.py', 'w') as f:
    f.write("students = [\n")
    for student in students:
        f.write(f"{repr(student)},\n")  # Use repr() to write the dictionary as a string suitable for Python code
    f.write("]\n")

print("student_data.py has been updated.")

###############################################################################################################
# Slide 5
for student in students:
    if student['CPSID'] == 123456:  # Replace with the condition to find the specific student
        del student['MName']  # Deletes the 'MName' key-value pair
        print(f"Updated student: {student}")

# Using a loop to find and remove a student by a specific condition
students = [student for student in students if student['CPSID'] != 123456]  
# Keeps all except the one with CPSID 123456

###############################################################################################################
# Slide 6
# Update a specific entry by index
students[0]['FName'] = 'Gio'  # Updates the first student's first name
students[0]['LName'] = 'Aguayo'
print(students[0])

###############################################################################################################
# Slide 7
# Remove a specific student by index
del students[0]  # Removes the first student in the list

###############################################################################################################
# Slide 8
# Example: Add a 'ContactNumber' field to each student
for student in students:
    student['ContactNumber'] = '123-456-7890'  # Assign a default or specific value

###############################################################################################################
# Slide 9
# Create a new student dictionary
new_student = {
    'CPSID': 987654,
    'Combo,Name': 'Doe, John',
    'FName': 'John',
    'LName': 'Doe',
    'MName': 'Paul',
    'HR': 'B220',
    'GL': 11,
    'Email': ['john.doe@example.com', 'j.doe@example.org']
}

# Add the new student to the list
students.append(new_student)

###############################################################################################################

