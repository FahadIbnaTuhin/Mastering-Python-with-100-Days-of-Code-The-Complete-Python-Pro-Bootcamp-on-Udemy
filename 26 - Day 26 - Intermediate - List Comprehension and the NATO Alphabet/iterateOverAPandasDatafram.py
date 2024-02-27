student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through the dictionaries
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_fram = pandas.DataFrame(student_dict)
print(student_data_fram)

# Loop through a data fram
# for (key, value) in student_data_fram.items():
#     print(value)
# Not totally same like the dictionaries

# Loop through rows of a data fram
for (index, row) in student_data_fram.iterrows():
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "James":
        print(row.score)
