import datetime

from homework12.db.models import HomeWork, HomeworkResult, Student, Teacher

teacher = Teacher.objects.create(first_name="Roman", last_name="Romanov")
student = Student.objects.create(first_name="Egor", last_name="Egorov")
hw = HomeWork.objects.create(
    text="To do this",
    deadline=datetime.timedelta(7),
    created=datetime.datetime(2021, 5, 1),
)
hw_result = HomeworkResult.objects.create(
    solution="my solution", created=datetime.datetime(2021, 5, 5)
)
hw_result.author = student
hw_result.homework = hw

teacher.save()
student.save()
hw.save()
hw_result.save()
