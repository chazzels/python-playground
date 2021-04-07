assignmentGrades = []
assignmentCount = int(input("Enter number of grades to process: "))
studentName = input("Enter student name: ")
for i in range(assignmentCount): assignmentGrades.append(int(input('Enter assignment grade (' + str(i+1) + '/' + str(assignmentCount) +'): ')))
print(studentName.title() + " has an average of: " + str(sum(assignmentGrades)/len(assignmentGrades)))