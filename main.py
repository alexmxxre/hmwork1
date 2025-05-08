class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = sum([sum(g) for g in self.grades.values()])
        count = sum([len(g) for g in self.grades.values()])
        return total / count if count != 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" + \
               f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n" + \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" + \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = sum([sum(g) for g in self.grades.values()])
        count = sum([len(g) for g in self.grades.values()])
        return total / count if count != 0 else 0

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n" + \
               f"Средняя оценка за лекции: {self.average_grade():.1f}"

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"


# Примеры использования
student1 = Student('Иван', 'Иванов', 'м')
student2 = Student('Мария', 'Петрова', 'ж')

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Python']
student1.finished_courses += ['Git']
student2.finished_courses += ['Git']

lecturer1 = Lecturer('Алексей', 'Смирнов')
lecturer2 = Lecturer('Елена', 'Новикова')

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Ольга', 'Кузнецова')
reviewer2 = Reviewer('Дмитрий', 'Соколов')

reviewer1.courses_attached += ['Python']
reviewer2.courses_attached += ['Python']

# Оценки студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Python', 9)

# Оценки лекторам
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 7)

# Печать объектов
print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Сравнение
print(student1 > student2)
print(lecturer1 > lecturer2)

# Средние оценки
def average_grade_students(students, course):
    total, count = 0, 0
    for student in students:
        grades = student.grades.get(course, [])
        total += sum(grades)
        count += len(grades)
    return total / count if count != 0 else 0

def average_grade_lecturers(lecturers, course):
    total, count = 0, 0
    for lecturer in lecturers:
        grades = lecturer.grades.get(course, [])
        total += sum(grades)
        count += len(grades)
    return total / count if count != 0 else 0

print("Средняя оценка студентов по курсу Python:", average_grade_students([student1, student2], 'Python'))
print("Средняя оценка лекторов по курсу Python:", average_grade_lecturers([lecturer1, lecturer2], 'Python'))
