"""
В этом задании будем улучшать нашу систему классов из задания прошлой лекции
(Student, Teacher, Homework)
Советую обратить внимание на defaultdict из модуля collection для
использования как общую переменную


1. Как то не правильно, что после do_homework мы возвращаем все тот же
объект - будем возвращать какой-то результат работы (HomeworkResult)

HomeworkResult принимает объект автора задания, принимает исходное задание
и его решение в виде строки
Атрибуты:
    homework - для объекта Homework, если передан не этот класс -  выкинуть
    подходящие по смыслу исключение с сообщением:
    'You gave a not Homework object'

    solution - хранит решение ДЗ как строку
    author - хранит объект Student
    created - c точной датой и временем создания

2. Если задание уже просрочено хотелось бы видеть исключение при do_homework,
а не просто принт 'You are late'.
Поднимайте исключение DeadlineError с сообщением 'You are late' вместо print.

3. Student и Teacher имеют одинаковые по смыслу атрибуты
(last_name, first_name) - избавиться от дублирования с помощью наследования

4.
Teacher
Атрибут:
    homework_done - структура с интерфейсом как в словаря, сюда поподают все
    HomeworkResult после успешного прохождения check_homework
    (нужно гаранитровать остутствие повторяющихся результатов по каждому
    заданию), группировать по экземплярам Homework.
    Общий для всех учителей. Вариант ипользования смотри в блоке if __main__...
Методы:
    check_homework - принимает экземпляр HomeworkResult и возвращает True если
    ответ студента больше 5 символов, так же при успешной проверке добавить в
    homework_done.
    Если меньше 5 символов - никуда не добавлять и вернуть False.

    reset_results - если передать экземпряр Homework - удаляет только
    результаты этого задания из homework_done, если ничего не передавать,
    то полностью обнулит homework_done.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime
from collections import defaultdict
from dataclasses import dataclass


class DeadlineError(Exception):
    def __init__(self, message="You are late"):
        self.message = message


class HomeWork:
    __slots__ = ["text", "deadline", "created"]

    def __init__(self, text, deadline):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = datetime.datetime.now()

    @property
    def is_active(self):
        return (self.deadline + self.created) > datetime.datetime.now()


class HomeworkResult:
    def __init__(self, student, homework, solution):
        if isinstance(homework, HomeWork):
            self.author = student
            self.homework = homework
            self.solution = solution
            self.created = datetime.datetime.now()
        else:
            raise TypeError("HomeWork object were expected")


@dataclass
class Human:
    __slots__ = ["first_name", "last_name"]
    last_name: str
    first_name: str


class Student(Human):
    def do_homework(self, homework, solution):
        if homework.is_active:
            return HomeworkResult(self, homework, solution)
        raise DeadlineError


class Teacher(Human):

    homework_done = defaultdict(list)

    @staticmethod
    def create_homework(text, deadline):
        return HomeWork(text, deadline)

    @staticmethod
    def check_homework(homework):
        if len(homework.solution) > 5:
            if homework not in Teacher.homework_done[homework.homework]:
                Teacher.homework_done[homework.homework].append(homework)
            return True

        return False

    @staticmethod
    def reset_results(homework=None):
        if homework:
            del Teacher.homework_done[homework]
        else:
            Teacher.homework_done.clear()
