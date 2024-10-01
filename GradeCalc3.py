""" NAME: Ibrahim Hudson
COURSE:  Comp163
DESCRIPTION:
 This program takes in a user inputted amount of grades and gives you the weighted total per
 category and for your overall grade. After which it will give you your letter grade."""


# DECLARATIONS


global grade, sum_total
# Creates a dict for grades and their value
grade_dict = {
    'A': 90, 'A-': 85,
    'B+': 82, 'B': 78, 'B-': 75,
    'C+': 72, 'C': 68, 'C-': 65,
    'D+': 60, 'D': 55, 'F': 0
}
# Creates dict for assignment type and their value
comp163Cat = {
    'Homework': .10,
    'Program Assignments': .30,
    'Quiz': .15, 'Test': .20,
    'Final Exam': .25
}
# Creates and adds your weighted value to comp163CatGrades from a list that stores temporary values [catGrade]
catGrade = []
comp163CatGrades = {
    'Homework': None,
    'Program Assignments': None,
    'Quiz': None, 'Test': None,
    'Final Exam': None
}
# Outputs user prompt and stores values in their respective dict.
for item in comp163Cat:
    print(f'{item} Category')
    x = float(input(f'Enter grade for Category {item} (\'-1\' to quit): '))
    if item == 'Final Exam':
        catGrade.append(x)
    else:
        while x != -1.0:
            catGrade.append(x)
            x = float(input(f'Enter grade for Category {item} (\'-1\' to quit): '))
# Takes those values and specifically stores the weighted Avg.
    comp163CatGrades[item] = (sum(catGrade) / len(catGrade) * comp163Cat[item])
    catGrade = []
# Outputs the category and weighted totals
for key, value in comp163CatGrades.items():
    print(f'{key} weighted total is {value:.2f}')
# creates a weighted total to determine your letter grade
total_weighted = 0
for key, value in comp163CatGrades.items():
    total_weighted += value
for item in grade_dict:
    if total_weighted >= grade_dict[item]:
        grade = item
        break
# Outputs total weighted & letter grade
print(f'Your weighted total in the class is : {total_weighted:.2f}')
print(f'Your letter grade in the class is : {grade}')
