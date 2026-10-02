students = {
    "101": {
        "name": "Rahim",
        "cgpa": 3.50,
        "department": "CSE"
    },
    "102": {
        "name": "Karim",
        "cgpa": 3.80,
        "department": "AI"
    },
    "103": {
        "name": "Sakib",
        "cgpa": 3.60,
        "department": "CSE"
    }
}

student_id = input("Enter student ID: ")

if student_id in students:
    print("Name:", students[student_id]["name"])
    print("CGPA:", students[student_id]["cgpa"])
    print("Department:", students[student_id]["department"])
else:
    print("Student not found.")