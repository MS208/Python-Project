def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 50:
        return 'D'
    else:
        return 'F'

def main():
    print("Student Grading System")
    name = input("Enter Student Name: ")

    subjects = ['Maths', 'Science', 'English', 'History', 'Computer']
    marks = []

    for subject in subjects:
        score = float(input(f"Enter marks for {subject}: "))
        marks.append(score)

    total = sum(marks)
    average = total / len(subjects)
    grade = calculate_grade(average)

    print("\n----- Report Card -----")
    print(f"Name      : {name}")
    print(f"Total     : {total}/500")
    print(f"Average   : {average:.2f}")
    print(f"Grade     : {grade}")
    print("------------------------")

if __name__ == "__main__":
    main()
