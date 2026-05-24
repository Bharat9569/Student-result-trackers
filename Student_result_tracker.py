import json
import os


class Subject:
    def __init__(self, subject_name, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100")

        self.subject_name = subject_name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        elif self.marks >= 40:
            return 'E'
        else:
            return 'FAIL'

    def to_dict(self):
        return {
            "subject_name": self.subject_name,
            "marks": self.marks
        }


class Student:
    id_counter = 100

    def __init__(self, name):
        self.id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.subjects = []

    def add_subject(self, subject_name, marks):
        subject = Subject(subject_name, marks)
        self.subjects.append(subject)

    def total_marks(self):
        return sum(sub.marks for sub in self.subjects)

    def percentage(self):
        if len(self.subjects) == 0:
            return 0

        return self.total_marks() / len(self.subjects)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "subjects": [sub.to_dict() for sub in self.subjects]
        }


class ResultManager:
    def __init__(self):
        self.students = []
        self.load_db()

    def save_db(self):
        try:
            data = []

            for student in self.students:
                data.append(student.to_dict())

            with open("student.json", "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print("Error saving file:", e)

    def load_db(self):
        try:
            if not os.path.exists("student.json"):
                return

            with open("student.json", "r") as file:
                data = json.load(file)

            for stu in data:
                student = Student(stu["name"])
                student.id = stu["id"]

                for sub in stu["subjects"]:
                    student.subjects.append(
                        Subject(sub["subject_name"], sub["marks"])
                    )

                self.students.append(student)

            if self.students:
                Student.id_counter = max(
                    stu.id for stu in self.students
                ) + 1

        except Exception as e:
            print("Error loading file:", e)

    def check_student(self, student_id):
        for stu in self.students:
            if stu.id == student_id:
                return stu

        return None

    def add_student(self):
        try:
            name = input("Enter student name: ")

            student = Student(name)
            self.students.append(student)

            print(f"Student Added Successfully.")
            print(f"Student ID: {student.id}")

            self.save_db()

        except Exception as e:
            print(e)

    def remove_student(self):
        try:
            student_id = int(input("Enter Student ID: "))

            student = self.check_student(student_id)

            if student:
                self.students.remove(student)
                self.save_db()
                print("Student Removed Successfully.")
            else:
                print("Student Not Found")

        except Exception as e:
            print(e)

    def add_subject_marks(self):
        try:
            student_id = int(input("Enter Student ID: "))

            student = self.check_student(student_id)

            if student:
                subject_name = input("Enter Subject Name: ")
                marks = int(input("Enter Marks: "))

                student.add_subject(subject_name, marks)

                self.save_db()

                print("Subject Added Successfully")

            else:
                print("Student Not Found")

        except ValueError:
            print("Invalid Input")

    def view_result(self):
        try:
            student_id = int(input("Enter Student ID: "))

            student = self.check_student(student_id)

            if student:

                print("\n===== RESULT =====")
                print(f"ID: {student.id}")
                print(f"Name: {student.name}")

                print("\nSubjects:")

                for sub in student.subjects:
                    print(
                        f"{sub.subject_name} : "
                        f"{sub.marks} "
                        f"({sub.grade()})"
                    )

                print("\nTotal:", student.total_marks())
                print(
                    "Percentage:",
                    round(student.percentage(), 2)
                )

            else:
                print("Student Not Found")

        except Exception as e:
            print(e)

    def view_all_students(self):
        if not self.students:
            print("No students found")
            return

        print("\n===== STUDENTS =====")

        for stu in self.students:
            print(f"ID: {stu.id} | Name: {stu.name}")

    def menu(self):
        while True:

            print("\n*** STUDENT RESULT TRACKER ***")

            print("1. Add Student")
            print("2. Remove Student")
            print("3. Add Subject Marks")
            print("4. View Result")
            print("5. View All Students")
            print("6. Exit")

            try:
                choice = int(input("Enter Choice: "))

                if choice == 1:
                    self.add_student()

                elif choice == 2:
                    self.remove_student()

                elif choice == 3:
                    self.add_subject_marks()

                elif choice == 4:
                    self.view_result()

                elif choice == 5:
                    self.view_all_students()

                elif choice == 6:
                    print("Exiting...")
                    break

                else:
                    print("Enter valid choice")

            except ValueError:
                print("Enter number only")


manager = ResultManager()
manager.menu()