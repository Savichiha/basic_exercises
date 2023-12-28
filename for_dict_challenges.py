# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

from collections import Counter
from operator import itemgetter
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

print(Counter(map(itemgetter('first_name'), students)))


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

name = max(students, key=students.count)
print(f'Самое частое имя среди учеников: {name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

from collections import Counter

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

cl = 1
for item in school_students:
    temp = [i['first_name'] for i in item]
    c = Counter(temp)
    print(f'Самое частое имя в классе {cl}: {c.most_common()[0][0]}')
    cl += 1


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
for x in school:
	print(f"В классе {x['class']}: ", end="")
	men_num=0
	women_num=0
	for y in x['students']:
		if is_male.get(y['first_name'])==False:
			women_num+=1
		if is_male.get(y['first_name'])==True:
			men_num+=1
	answer=(f'{women_num} девочек и {men_num} мальчиков')
	if men_num+women_num==len(x['students']):
		print(answer)
	else:
		print(answer, f"и {len(x['students'])-int(men_num+women_num)}")
		


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
school_values = [list(val.values()) for val in school]
genders_count_by_class = {}
 
for lists in school_values:
  for data in lists:
    if type(data) == str:
      class_name = data
      genders_count_by_class[class_name] = [{"males": 0, "females": 0}]
    else:
      students_count = len(data)
      key_name = list(data[0].keys())[0]
      student_names = [data[i][key_name] for i in range(students_count)]
      for student_name in student_names:
        if is_male[student_name]:
          genders_count_by_class[class_name][0]['males'] += 1
        else:
          genders_count_by_class[class_name][0]['females'] += 1
keys = list(genders_count_by_class.keys())
for idx, key in enumerate(keys):
    if genders_count_by_class[key][0]['males'] > genders_count_by_class[keys[idx-1]][0]['males']:
      print(f"Больше всего мальчиков в классе {key}")
    else:
      print(f"Больше всего мальчиков в классе {keys[idx-1]}")
 
    if genders_count_by_class[key][0]['females'] > genders_count_by_class[keys[idx-1]][0]['females']:
      print(f"Больше всего девочек в классе {key}")
    else:
      print(f"Больше всего девочек в классе {keys[idx-1]}")
    break

