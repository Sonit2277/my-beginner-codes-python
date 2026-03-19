import csv

# Write
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "score"])  # header
    # write 5 rows yourself
    writer.writerow(["Alice", 20, 85])
    writer.writerow(["Bob", 22, 90])
    writer.writerow(["Charlie", 19, 78])
    writer.writerow(["David", 21, 92])
    writer.writerow(["Eve", 20, 88])

# Read
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
    print(f"Name: {row[0]}, Age: {row[1]}, Score: {row[2]}")

#find highest score
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    highest_score = 0
    top_student = ""
    for row in reader:
        name, age, score = row
        score = int(score)
        if score > highest_score:
            highest_score = score
            top_student = name

print(f"Top student: {top_student}, Highest score: {highest_score}")


