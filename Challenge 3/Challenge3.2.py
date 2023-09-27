class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"

def sort_students(student_list):
    # Sort the student_list based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Test the function with different input lists of students
students1 = [
    Student("billa", "A101", 3.9),
    Student("Ranga", "B102", 3.7),
    Student("bhasha", "C103", 4.0),
]

students2 = [
    Student("David", "D104", 3.8),
    Student("Ravi", "E105", 3.5),
    Student("Karthi", "F106", 3.9),
]

sorted_students1 = sort_students(students1)
sorted_students2 = sort_students(students2)

print("Sorted Students List 1:")
for student in sorted_students1:
    print(student)

print("\nSorted Students List 2:")
for student in sorted_students2:
    print(student)
