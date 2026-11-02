from student_service import(add_student, view_students, search_student, update_student, delete_student, change_student_id)

def main():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. change_student_id")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            if not name.strip():
                print("Student name cannot be empty.")
                continue
            try:
               age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. please enter a number.")
                continue
            if age <= 0 or age > 100:
                print("Invalid age. age must be between 1 and 100.")
                continue
            course = input("Enter student course: ")
            if not course.strip():
                print("Student course cannot be empty.")
            try:
                marks = float(input("Enter student marks: "))
            except ValueError:
                print("Invalid marks. please enter a number.")
                continue
            if marks <0 or marks > 1000:
                print("Invalid marks. marks must be between 0 and 1000.")
                continue
            grade = input("Enter student grade: ").upper()
            if grade not in ["A", "B", "C", "D", "E", "F"]:
                print("Invalid grade. Enter A, B, C, D, E, F.")
                continue
            add_student(name, age, course, marks, grade)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to search: "))
            search_student(student_id)
        elif choice == "4":
            try:
                student_id = int(input("Enter student ID to update: "))
            except ValueError:
                print("Invalid student ID. please enter a number.")
                continue
            name = input("Enter student name: ")
            if not name.strip():
                    print("student name cannot be empty.")
                    continue
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. please enter a number.")
                continue
            if age <= 0 or age > 100:
                print("Invalid age. age must be between 1 and 100.")
                continue
            course = input("Enter student course: ")
            if not course.strip():
                    print("Student course cannot be empty.")
            try:
                marks = float(input("Enter student marks: "))
            except ValueError:
                print("Invalid marks. please enter a number.")
                continue
            if marks < 0 or marks > 1000:
                    print("Invalid marks. marks must be between 0 and 1000.")
                    continue
            grade = input("Enter student grade: ").upper()
            if grade not in ["A", "B", "C", "D", "E", "F"]:
                print("Invalid grade. Enter A, B, C, D, E, F.")
                continue
            update_student(student_id, name, age, course, marks, grade)
        elif choice == "5":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == "6":
            try:
                old_id = int(input("Enter old student ID : "))
                new_id = int(input("Enter new student ID : "))
            except ValueError:
                print("Invalid student ID. please enter numbers.")
                continue
            if new_id <=0:
                print("Student ID must be greater than 0.")
                continue
            change_student_id(old_id, new_id)
        elif choice == "7":
            print("Thank you for using student management system!")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main()
