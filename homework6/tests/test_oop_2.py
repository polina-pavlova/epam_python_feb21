import pytest

import homework6.tasks.oop_2 as oop2


@pytest.fixture()
def create_objects():
    opp_teacher = oop2.Teacher("Daniil", "Shadrin")
    advanced_python_teacher = oop2.Teacher("Aleksandr", "Smetanin")

    lazy_student = oop2.Student("Roman", "Petrov")
    good_student = oop2.Student("Lev", "Sokolov")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")

    return (
        opp_teacher,
        advanced_python_teacher,
        lazy_student,
        good_student,
        oop_hw,
        docs_hw,
        result_1,
        result_2,
        result_3,
    )


def test_Teacher_class(create_objects):
    teacher = create_objects[0]
    assert teacher.last_name == "Daniil"


def test_student_class(create_objects):
    student = create_objects[2]
    assert student.first_name == "Petrov"


def test_do_homework(create_objects):
    result_1 = create_objects[6]
    assert isinstance(result_1, oop2.HomeworkResult)


def test_do_homework_exception(create_objects, capsys):
    good_student = create_objects[3]
    with pytest.raises(TypeError):
        oop2.HomeworkResult(good_student, "fff", "Solution")
        captured = capsys.readouterr()
        assert captured.err == "HomeWork object were expected"


def test_deadline_error(create_objects, capsys):
    hw = oop2.Teacher.create_homework("Deadline test", 0)
    lazy_st = create_objects[2]
    with pytest.raises(oop2.DeadlineError):
        lazy_st.do_homework(hw, "Done")
        captured = capsys.readouterr()
        assert captured.err == "You are late"


def test_check_homework_true(create_objects):
    oop_teacher = create_objects[0]
    result = create_objects[-2]
    assert oop_teacher.check_homework(result) == True


def test_check_homework_false(create_objects):
    oop_teacher = create_objects[0]
    result = create_objects[-1]
    assert oop_teacher.check_homework(result) == False


def test_reset_results(create_objects):
    oop_teacher = create_objects[0]
    advanced_python_teacher = create_objects[1]
    result_1 = create_objects[-3]

    oop_teacher.check_homework(result_1)
    temp_1 = oop_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = oop2.Teacher.homework_done
    assert temp_1 == temp_2


def test_reset_results_clear(create_objects):
    oop_teacher = create_objects[0]
    advanced_python_teacher = create_objects[1]
    result_1 = create_objects[-3]

    oop_teacher.check_homework(result_1)
    advanced_python_teacher.check_homework(result_1)

    oop2.Teacher.reset_results()
    temp = oop2.Teacher.homework_done
    assert len(temp) == 0


def test_reset_results_del(create_objects):
    oop_teacher = create_objects[0]
    result_1 = create_objects[-3]
    result_2 = create_objects[-2]
    oop_hw = create_objects[4]

    oop_teacher.check_homework(result_1)
    oop_teacher.check_homework(result_2)

    oop2.Teacher.reset_results(oop_hw)

    temp = oop2.Teacher.homework_done
    assert isinstance(list(temp.items())[0][0], oop2.HomeWork)
