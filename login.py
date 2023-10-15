# Initialize variables
grades = []
highest_grade = None

# Input loop to read grades
while True:
	try:
		grade = input("Enter a grade (or -1 to finish): ")
		grade = int(grade)

		if grade == -1:
			break  # Exit the loop when -1 is entered

		if highest_grade is None or grade > highest_grade:
			highest_grade = grade

		grades.append(grade)
	except ValueError:
		print("Invalid input. Please enter a valid grade.")

# Check if any grades were entered
if not grades:
	print("No grades entered.")
else:
	print(f"Grades entered: {grades}")
	print(f"The highest grade is: {highest_grade}")
