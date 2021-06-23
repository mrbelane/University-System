from django.contrib import admin
from .models import Course, Student, Teacher,TakenLessons

# from .models import Student
# Register your models here.


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(TakenLessons)
