from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MaxValueValidator, MinValueValidator

majors = (
    (0, "کامپیوتر"),
    (1, "برق"),
    (2, "مکانیک"),
)

grades = (
    (0, "کارشناسی"),
    (1, "کارشناسی ارشد"),
    (2, "دکتری"),
)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    student_id = models.CharField(primary_key=True, max_length=100, unique=True, default=0)
    first_name = models.CharField(max_length=100, default="بدون نام")
    last_name = models.CharField(max_length=100, default="بدون نام")
    unit = models.IntegerField(default=0)
    major = models.IntegerField(default=0, choices=majors)
    grade = models.IntegerField(default=0, choices=grades)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def getAllStudent():
        return Student.objects.all()

    @staticmethod
    def getStudentById(id):
        return Student.objects.get(student_id=id)

    @staticmethod
    def getStudentByUser(user:User):
        return Student.objects.get(user=user)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    teacher_id = models.CharField(primary_key=True, max_length=100, unique=True, default=0)
    first_name = models.CharField(max_length=100, default="بدون نام")
    last_name = models.CharField(max_length=100, default="بدون نام")
    major = models.IntegerField(default=0, choices=majors)
    grade = models.IntegerField(default=0, choices=grades)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @staticmethod
    def filterTeacherByMajor(major):
        return Teacher.objects.filter(major=major)

    @staticmethod
    def getAllTeacher():
        return Teacher.objects.all()


class Course(models.Model):
    name = models.CharField(max_length=100, default="بدون نام")
    id = models.AutoField(primary_key=True)
    unit = models.IntegerField(default=1)
    Teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
    )
    number_of_student = models.IntegerField(default=0)

    term = models.IntegerField(default=1,
                               validators=[MaxValueValidator(8), MinValueValidator(1)])
    major = models.IntegerField(default=0, choices=majors)

    def __str__(self):
        return f'{self.name}'

    @staticmethod
    def getCourseById(id):
        return Course.objects.get(id=id)

    @staticmethod
    def getCourseIdInArray(arr):
        return Course.objects.filter(id__in=arr)

    @staticmethod
    def getAll():
        return Course.objects.all()


class TakenLessons(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('Course', 'Student',)

    @staticmethod
    def filterTakeCourseWithStudent(student):
        return TakenLessons.objects.filter(Student=student)
