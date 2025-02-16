# Get the number of males and females from the user
males = int(input("Enter the number of males: "))
females = int(input("Enter the number of females: "))

# Calculate the total number of students
total_students = males + females

# Calculate the percentage of males and females
male_percentage = (males / total_students) * 100
female_percentage = (females / total_students) * 100

# Display the results
print(f"Total number of students: {total_students}")
print(f"Percentage of males: {male_percentage:.2f}%")
print(f"Percentage of females: {female_percentage:.2f}%")
