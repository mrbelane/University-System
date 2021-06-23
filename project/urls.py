from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('students', views.students, name='student'),
    path('teachers', views.teachers, name='teachers'),
    path('availableCourses', views.availableCourses, name='availableCourses'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logoutUser'),

    # سبد خرید
    path('lessons', views.selectUnit, name='selectUnit'),
    path('404', views.notFound, name='404'),

]

