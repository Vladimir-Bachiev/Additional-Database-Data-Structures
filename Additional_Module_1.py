"""
Умышленно не ввожу дополнительные временные переменные:
    1) для тренировки
    2) В целях экономии памяти может пригодиться в больших проектах
Не использую конструкцию for [элемент] in [последовательность]: [тело цикла] ...
    1) Мы этого еще не изучали ;)
    2) Слишком грубо и не раскрывает возможностей Python
    3) Хотел сделать компактное решение задачи
"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'John''ny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

print('Исходный список оценок: \33[1;33m \n', grades, '\33[0;0m \n')

print('Исходный (неупорядоченный) список учеников: \33[1;33m \n', students, '\33[0;0m \n')

students = sorted(students) # Сортировка учеников в алфавитном порядке
print('Упорядочиваем список учеников: \33[1;33m \n', students, '\33[0;0m \n')

grades=list(map(lambda x: sum(x) / len(x), grades)) # Вычисляем среднее арифметическое оценок каждого ученика
print('Вычисляем средний арифметический бал каждого ученика: \33[1;33m \n', grades, '\33[0;0m \n')

students = dict(zip(students, grades)) #Создаем словарь из полученных данных
print('Создаем словарь из полученных данных: \33[1;34m \n', students, '\33[1;31m', type(students),'\33[0;0m')

"""
В принципе можно было это же написать одной строкой:
students = dict(zip(sorted(students), list(map(lambda x: sum(x) / len(x), grades))))
но так мне кажется сложнее читать код
"""
