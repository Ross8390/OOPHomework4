
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = float()

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_counter = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for i in self.grades:
            grades_counter += len(self.grades[i])
        self.avg_grade = round(sum(map(sum, self.grades.values())) / grades_counter, 2)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.avg_grade}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.avg_grade < other.avg_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = float()

    def __str__(self):
        grades_counter = 0
        for i in self.grades:
            grades_counter += len(self.grades[i])
        self.avg_grade = round(sum(map(sum, self.grades.values())) / grades_counter, 2)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.avg_grade < other.avg_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                    student.grades[course] += [grade]
            else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя = {self.name}\nФамилия = {self.surname}'
        return res


some_student = Student('Ruoy', 'Eman', 'your gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

other_student = Student('Peter', 'White', 'm')
other_student.courses_in_progress += ['Python']
other_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

other_reviewer = Reviewer('Victor', 'Black')
other_reviewer.courses_attached += ['Python']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

other_reviewer.rate_hw(other_student, 'Python', 10)
other_reviewer.rate_hw(other_student, 'Python', 9)
other_reviewer.rate_hw(other_student, 'Python', 8)

some_lecturer = Lecturer('Oleg', 'Aleksandrov')
some_lecturer.courses_attached += ['Python']

other_lecturer = Lecturer('Alexey', 'Vasin')
other_lecturer.courses_attached += ['Python']

some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 9)
some_student.rate_lecture(some_lecturer, 'Python', 9)

other_student.rate_lecture(some_lecturer, 'Python', 10)
other_student.rate_lecture(some_lecturer, 'Python', 8)
other_student.rate_lecture(some_lecturer, 'Python', 9)

some_student.rate_lecture(other_lecturer, 'Python', 10)
some_student.rate_lecture(other_lecturer, 'Python', 10)
some_student.rate_lecture(other_lecturer, 'Python', 10)

other_student.rate_lecture(other_lecturer, 'Python', 9)
other_student.rate_lecture(other_lecturer, 'Python', 9)
other_student.rate_lecture(other_lecturer, 'Python', 9)

print(f'Студенты:\n\n{some_student}\n\n{other_student}\n')
print()


print(f'Лекторы:\n\n{some_lecturer}\n\n{other_lecturer}\n')
print()

print(f'Результат сравнения студентов: '
      f'{some_student > other_student}')
print()

print(f'Результат сравнения лекторов: '
      f'{some_lecturer > other_lecturer}')
print()

student_list = [some_student, other_student]
lecturer_list = [some_lecturer, other_lecturer]

def student_rating(student_list, course_name):
    sum = 0
    counter = 0
    for s in student_list:
       if s.courses_in_progress == [course_name]:
            sum += s.avg_grade
            counter += 1
    average_for_all = round(sum / counter, 2)
    return average_for_all

def lecturer_rating(lecturer_list, course_name):
    sum = 0
    counter = 0
    for l in lecturer_list:
        if l.courses_attached == [course_name]:
            sum += l.avg_grade
            counter += 1
    average_for_all = round(sum / counter, 2)
    return average_for_all

print(f"Средняя оценка для всех студентов по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print()