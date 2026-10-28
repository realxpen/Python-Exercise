students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["Jane", 45, 50, 55]
]

if __name__ == "__main__":
    for student in students:
        name = student[0]
        grades = student[1:]
        grade1 = student[1]
        grade2 = student[2]
        grade3 = student[3]
        average = (grade1+grade2+grade3) / len(grades)
        print(f"{name} - Average: {average:.2f} - Grade: {"A" if average >= 70 else "B" if average >= 60 else "C" if average >= 50 else "D" if average >= 40 else "F"}")

