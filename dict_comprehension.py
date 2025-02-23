from pprint import pprint as pp

# num_and_square = {}

# for num in range(101):
#     num_and_square[num] = num ** 2

# pp(num_and_square)

# pp({ num: num **2  for num in range(101) })

grades = {"math": {"score": 95, "grade": "A"},
          "science": {"score": 90, "grade": "A-"},
          "history": {"score": 82, "grade": "B-"},
        }

# for subject, details in grades.items():
#     print(f"{subject}: {details["grade"]}")

print(", ".join([ f"{subject}: {details["grade"]}" for subject, details in grades.items()]))