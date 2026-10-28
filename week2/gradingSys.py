students = {
    "Samuel": [80, 75, 90],
    "David": [55, 60, 50], 
    "Mary": [35, 40, 30], 
    "John": [65, 70, 68],
    "Ayomide": [80, 82, 89]
    }

# def calculate_grade(average):



for name, scores in students.items():
    total = 0

    for score in scores:
        total += score
    average = total/len(scores)

    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    elif average >= 40:
        grade = "E"
    else:
        grade =  "F"


        # grade = calculate_grade(average)
        # result = "passed" if grade != "F" else "failed"

    print(f"{name} with an average score of {average:.2f} and has a grade of {grade}.")




# for name in students:
#     name = student[0]
#     scoreSum = student[1] + student[2] + student[3]
#     scorelist = students[1:]
#     averageScore = round(scoreSum / len(scorelist), 2)
#     
#     result = "passed" if grade != "F" else "failed"

