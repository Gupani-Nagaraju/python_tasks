#Task 1:
std_name = input("Enter student Name: ")
std_Roll = int(input("Enter student Roll Number: "))

subjects = input("Enter subjects seperated by space: ").split()
uniqe_subjects = list(set(subjects))

sub_marks = {}

for subject in uniqe_subjects:
    marks = int(input(f"Enter marks for {subject}: "))
    sub_marks[subject] = marks

print("Studet Name: ",std_name)
print("Student Roll No: ", std_Roll)

print("Unique Subjects are : ",uniqe_subjects)

print("Subject with marks are")

for subjects, marks in sub_marks.items():
    print(f"{subjects} : {marks}")