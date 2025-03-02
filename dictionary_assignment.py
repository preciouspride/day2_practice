from pprint import pprint as pp

students = {
    "1001": {
        "grades": {
            "math": {"score": 88, "grade": "B+"},
            "science": {"score": 92, "grade": "A"},
            "history": {"score": 85, "grade": "B"},
        }
    },
    "1002": {
        "grades": {
            "math": {"score": 76, "grade": "C"},
            "science": {"score": 81, "grade": "B-"},
            "history": {"score": 89, "grade": "B+"},
        }
    },
    "1003": {
        "grades": {
            "math": {"score": 95, "grade": "A"},
            "science": {"score": 90, "grade": "A-"},
            "history": {"score": 82, "grade": "B-"},
        }
    },
    "1004": {
        "grades": {
            "math": {"score": 79, "grade": "C+"},
            "science": {"score": 85, "grade": "B"},
            "history": {"score": 91, "grade": "A-"},
        }
    },
    "1005": {
        "grades": {
            "math": {"score": 92, "grade": "A-"},
            "science": {"score": 87, "grade": "B+"},
            "history": {"score": 80, "grade": "B-"},
        }
    },
    "1006": {
        "grades": {
            "math": {"score": 85, "grade": "B"},
            "science": {"score": 89, "grade": "B+"},
            "history": {"score": 78, "grade": "C+"},
        }
    },
    "1007": {
        "grades": {
            "math": {"score": 90, "grade": "A-"},
            "science": {"score": 92, "grade": "A"},
            "history": {"score": 88, "grade": "B+"},
        }
    },
    "1008": {
        "grades": {
            "math": {"score": 82, "grade": "B-"},
            "science": {"score": 86, "grade": "B"},
            "history": {"score": 84, "grade": "B"},
        }
    },
    "1009": {
        "grades": {
            "math": {"score": 93, "grade": "A"},
            "science": {"score": 88, "grade": "B+"},
            "history": {"score": 79, "grade": "C+"},
        }
    },
    "1010": {
        "grades": {
            "math": {"score": 77, "grade": "C"},
            "science": {"score": 80, "grade": "B-"},
            "history": {"score": 90, "grade": "A-"},
        }
    }
}


## Create a for loop that will print out each student's grade for each subject:
# For example the output should be like: 
# math: C, science: B-, history: A-
# math: A, science: B=, history: C+

# for k, v in students.items():
#     print(f'Key => {k}')
#     print(f'Name & Subjects => {v["name"]}: {v["grades"]}')

# for _id, student in students.items():
#     name = student["name"]
#     grades = ", ".join(f"{subject}: {details['grade']}" for subject, details in student["grades"].items())
#     print(f"{name}: {grades}")

for student_grade in students.values():
    for subject in student_grade.values():
        for subj, result in subject.items():
            print(f"{subj}: {result["grade"]}", end=" ")
        print("\n", end="")