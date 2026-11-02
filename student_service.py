from connection import create_connection

def add_student(name,age,course,marks,grade):
    connection = create_connection()
    cursor = connection.cursor()

    query = """INSERT INTO students (name,age,course,marks,grade) VALUES (%s,%s,%s,%s,%s)"""
    values = (name,age,course,marks,grade)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print("Student Added Successfully!")

def view_students():
    connection = create_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM students"""
    cursor.execute(query)
    students = cursor.fetchall()
    if not students:
        print("No students found")
    else:
        print("\n===== Students Details =====")
        print("ID | Name | Age | Course | Marks | Grade")
        print("_" * 55)
        for student in students:
            print(student[0],"|", student[1],"|", student[2],"|", student[3],"|", student[4],"|", student[5])
            cursor.close()
            connection.close()



def search_student(student_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM students WHERE student_id = %s"""
    cursor.execute(query, (student_id,))
    students = cursor.fetchone()
    if students:
        print("\n===== student Details =====")
        print("student ID :", students[0])
        print("Student Name :", students[1])
        print("Student Age :", students[2])
        print("Student Course :", students[3])
        print("Student Marks :", students[4])
        print("Student Grade :", students[5])
    else:
        print("Student not found.")
        cursor.close()
        connection.close()


def update_student(student_id,name,age,course,marks,grade):
    connection = create_connection()
    cursor = connection.cursor()
    query = """UPDATE students SET name = %s, age = %s, course = %s, marks = %s, grade = %s WHERE student_id = %s"""
    values = (name,age,course,marks,grade,student_id)
    cursor.execute(query, values)
    connection.commit()
    print("Student Updated Successfully!")
    cursor.close()
    connection.close()

def delete_student(student_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = """DELETE FROM students WHERE student_id = %s"""
    cursor.execute(query, (student_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student Deleted Successfully!")
    else:
        print("Student not found.")
    cursor.close()
    connection.close()


def change_student_id(old_id,new_id):
    connection = create_connection()
    cursor = connection.cursor()
    query = """UPDATE students SET student_id = %s WHERE student_id = %s"""
    values = (new_id,old_id)
    cursor.execute(query, values)
    connection.commit()
    if cursor.rowcount > 0:
        print("Student ID updated Successfully!")
    else:
        print("Student not found.")
        cursor.close()
        connection.close()
