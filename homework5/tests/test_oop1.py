import datetime

import pytest

import homework5.tasks.oop_1 as oop1


@pytest.fixture()
def create_objects():
    teacher = oop1.Teacher("Daniil", "Shadrin")
    student = oop1.Student("Roman", "Petrov")

    expired_homework = oop1.Teacher.create_homework("Learn functions", 0)
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    expired_homework.created = datetime.datetime.strptime(
        "2019-05-26 16:44:30.688762", "%Y-%m-%d %H:%M:%S.%f"
    )

    return teacher, student, expired_homework, oop_homework


def test_Teacher_class(create_objects):
    teacher = create_objects[0]
    assert teacher.last_name == "Daniil"


def test_student_class(create_objects):
    student = create_objects[1]
    assert student.first_name == "Petrov"


def test_homework_create(create_objects):
    expired_homework = create_objects[2]
    assert expired_homework.created == datetime.datetime(
        2019, 5, 26, 16, 44, 30, 688762
    )


def test_homework_deadline(create_objects):
    expired_homework = create_objects[2]
    assert expired_homework.deadline == datetime.timedelta(0)


def test_homework_text(create_objects):
    expired_homework = create_objects[2]
    assert expired_homework.text == "Learn functions"


def test_second_hw_deadline(create_objects):
    second_homework = create_objects[3]
    assert second_homework.deadline == datetime.timedelta(5)


def test_is_not_active(create_objects):
    expired_homework = create_objects[2]
    assert expired_homework.is_active == False


def test_is_active(create_objects):
    second_homework = create_objects[3]
    assert second_homework.is_active == True


def test_doing_active_homework(create_objects):
    st = create_objects[1]
    second_homework = create_objects[3]
    assert isinstance(st.do_homework(second_homework), oop1.HomeWork)


def test_doing_inactive_hw(create_objects, capsys):
    st = create_objects[1]
    expired_homework = create_objects[2]
    st.do_homework(expired_homework)
    captured = capsys.readouterr()
    assert captured.out == "You are late\n"
