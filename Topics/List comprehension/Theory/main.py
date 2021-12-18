strings = '123456789'

for s in strings:
    (walrus or (walrus := list())).append(float(s))
print(walrus)

school = [["Mary", "Jack", "Tiffany"],
          ["Brad", "Claire"],
          ["Molly", "Andy", "Carla"]]

for class_group in school:
    (class_list or (class_list := list())).append(class_group)


for class_group in school:
    for student in class_group:
        (student_list or (student_list := list())).append(student)

print(student_list)
