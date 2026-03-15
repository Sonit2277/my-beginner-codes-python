students = {}

def add_student(name, score):
    students[name] = score

def view_all():
    for name, score in students.items():
        print(name, ":", score)

def search_student(name):
    if name in students:
        print(name, ":", students[name])
    else:
        print("Student not found")

def delete_student(name):
    if name in students:
        del students[name]
        print("Deleted")
    else:
        print("Not found")

def class_average():
    if students:
        avg = sum(students.values()) / len(students)
        print("Average:", round(avg, 2))
    else:
        print("No students yet")

def top_student():
    if students:
        top = max(students, key=students.get)
        print("Top student:", top, "with", students[top])
    else:
        print("No students yet")
while True:
    print("\n1. Add  2. View All  3. Search  4. Delete  5. Average  6. Top Student  7. Quit")
    choice = input("Choose: ")
    
    if choice == "1":
        name = input("Name: ")
        score = float(input("Score: "))
        add_student(name, score)
        print("Student added.")
    elif choice == "2":
        view_all()
    elif choice == "3":
        name = input("Name: ")
        search_student(name)
    elif choice == "4":
        name = input("Name: ")
        delete_student(name)
    elif choice == "5":
        class_average()
    elif choice == "6":
        top_student()
    elif choice == "7":
        break