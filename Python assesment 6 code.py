def calculate_grade(mark):
    """Determine grade for individual subjects or overall average"""
    if mark >= 90:
        return 'A+'
    elif mark >= 80:
        return 'A'
    elif mark >= 70:
        return 'B'
    elif mark >= 60:
        return 'C'
    elif mark >= 50:
        return 'D'
    else:
        return 'F'


def generate_report():
    print("\n--- Generate Student Report Card ---")
    name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))

    subjects = []
    marks = []
    grades = []

    for i in range(num_subjects):
        subject_name = input(f"\nEnter name of subject {i+1}: ")
        
      
        while True:
            try:
                mark = float(input(f"Enter marks for {subject_name} out of 100: "))
                if mark > 100 or mark < 0:
                    print("Marks can't be greater than 100 or less than 0. Please re-enter.")
                    continue
                break
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
        
        grade = calculate_grade(mark)
        subjects.append(subject_name)
        marks.append(mark)
        grades.append(grade)

    total = sum(marks)
    average = total / num_subjects
    final_grade = calculate_grade(average)

    print("\n===== STUDENT REPORT CARD =====")
    print(f"Name: {name}")
    print("-" * 40)
    print(f"{'Subject':15} {'Marks':>10} {'Grade':>10}")
    print("-" * 40)
    for i in range(num_subjects):
        print(f"{subjects[i]:15} {marks[i]:>10.2f} {grades[i]:>10}")
    print("-" * 40)
    print(f"Total Marks: {total:.2f}")
    print(f"Average Percentage: {average:.2f}")
    print(f"Final Grade: {final_grade}")
    print("=" * 40)


def main():
    while True:
        print("\n--- Student Report Card Generator ---")
        print("1. Generate Report Card")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            generate_report()
        elif choice == '2':
            print("Exiting program... Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
