weightedSystem = {'A+': 4.33, 'A': 4.00, 'A-': 3.67, 'B+': 3.33, 'B': 3.00, 'B-': 2.67, 'C+': 2.33, 'C': 2.00, 'C-': 1.33, 'D+': 1.00, 'D': 0.67, 'F': 0.00}

unweightedSystem = {'A': 4.00, 'B': 3.00, 'C': 2.00, 'D': 1.00, 'F': 0.00}

def unweightedCalc(grades, numClassesTaken):
	totalGPA = 0
	finalGPA = 0
	for grade in grades:
		totalGPA += unweightedSystem[grade[0]]
	finalGPA = totalGPA / numClassesTaken
	return round(finalGPA,2)

def weightedCalc(grades, numClassesTaken):
	totalGPA = 0
	finalGPA = 0
	for grade in grades:
		totalGPA += weightedSystem[grade]
	finalGPA = totalGPA / numClassesTaken
	return round(finalGPA,2)

###############################################

print("Welcome to the LFA Weighted and Unweighted GPA Calculator")

numClassesTaken = input("Accurately check your GPA, please enter the number of classes taken during a semeseter: ")

while True:
		try:
			int(numClassesTaken)
		except ValueError:
			numClassesTaken = input("Invalid input. Please enter an valid number: ")
		else:
			break

numClassesTaken = int(numClassesTaken)

print("Please enter your grades one by one to calculate your weighted and unweighted GPA. They should be in the format of A+, A, A-, B+, B, B-, C+, C, C-, D+, D, F")
grades = []
for i in range(numClassesTaken):
	grades.append(0)
	
for i in range(numClassesTaken):
	grade = input("Grade: ")
	while grade not in weightedSystem:
		print("Invalid input, please try again")
		grade = input("Grade: ")
	grades[i] = grade

print(grades)
	
print("Your weighted GPA is: " + str(weightedCalc(grades, numClassesTaken)))
print("Your unweighted GPA is: " + str(unweightedCalc(grades, numClassesTaken)))
		



