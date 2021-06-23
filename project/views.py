from django.shortcuts import render, redirect, get_object_or_404
from pip._internal import req

from .models import *
from .forms import *
from django.db.models import Avg, Count, Min, Sum
import logging
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import login
from .Tools import *

logger = logging.getLogger(__name__)


def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    context = {
        'home': 'active'
    }
    return render(request, 'app/home.html', context)


def teachers(request):
    if not request.user.is_authenticated:
        return redirect('login')
    name = "همه اساتید"
    if request.method == 'GET':
        if 'major' in request.GET:
            id = request.GET['major']
            name = f'اساتید رشته {str(majors[int(id)][1])}'
            response = Teacher.filterTeacherByMajor(major=id)
        else:
            response = Teacher.getAllTeacher()

        for item in response:
            item.grade = grades[item.grade][1]
            item.major = majors[item.major][1]
        context = {
            "name": name,
            "teachers": response,
            "teacher": "active"
        }
        return render(request, 'app/teachers.html', context)

    return redirect("/404")


def students(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Student.getAllStudent()
    for item in data:
        item.grade = grades[item.grade][1]

    detail = {}
    if data is not None:
        for major in majors:
            index = major[0]
            name = major[1]
            f = list(filter(lambda x: x.major == index, data))

            detail[index] = {
                'students': f,
                'name': name,
                'major': index
            }

    context = {
        'student': 'active',
        'students': detail,
    }
    return render(request, 'app/students.html', context)


def editProfile(request):
    if request.META.get('HTTP_REFERER') is None:
        messages.warning(request, 'صفحه‌ی مورد نظر یافت نشد.')
        return redirect('/404')

    if not request.user.is_authenticated:
        messages.warning(request, 'session منقضی شده است')
        return redirect('login')

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = editForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            student = Student.getStudentById(request.GET['id'])
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.major = form.cleaned_data['major']
            student.grade = form.cleaned_data['grade']
            student.save()
            messages.success(request, 'اطلاعات با موفقیت ذخیره شد.')

            # redirect to a new URL:
            return redirect('/students')
        else:
            messages.error(request, "خطا در دریافت اطلاعات")
    # if a GET (or any other method) we'll create a blank form
    elif 'id' in request.GET:
        id = request.GET['id']
        print(id)
        response = Student.getStudentById(id)
        context = {
            'form': response,
            'editStudent': 'active'
        }
        return render(request, 'app/editStudent.html', context)

    return redirect('/students')


# دروس ارایه شده
def availableCourses(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'session منقضی شده است')
        return redirect('login')

    if 'ci' in request.GET.keys():
        try:
            current_user = request.user
            student = Student.getStudentByUser(current_user)
            id = request.GET['ci']
            bag = []
            if 'bag' in request.session:
                bag = (request.session['bag'])

            isDuplicate = False
            for item in bag:
                if int(item) == int(id):
                    isDuplicate = True

            takeCourse = list(TakenLessons.filterTakeCourseWithStudent(student))
            for item in takeCourse:
                if int(item.Course.id) == int(id):
                    isDuplicate = True

            if isDuplicate:
                messages.warning(request, 'درس تکراری می‌باشد.')
            else:

                if len(bag) == 0:
                    bag.append(int(id))
                    request.session['bag'] = bag
                    messages.success(request, 'درس با موفقیت به سبد خرید اضافه شد.')
                else:
                    isError = False
                    bagCourse = list(Course.getCourseIdInArray(bag))
                    selectedCourse = Course.getCourseById(id)

                    sum_unit = 0
                    for c in bagCourse:
                        if c.term != selectedCourse.term or c.major != selectedCourse.major:
                            isError = True
                            messages.error(request, 'خطا در انتخاب به دلیل عدم مغایرت ترم یا رشته.')
                            break
                        sum_unit = sum_unit + c.unit

                        if (sum_unit + selectedCourse.unit) > 6:
                            isError = True
                            messages.error(request, 'خطا در انتخاب به دلیل بیش از 6 واحد بودن.')
                            break

                    if not isError:
                        bag.append(int(id))
                        request.session['bag'] = bag
                        messages.success(request, 'درس با موفقیت به سبد خرید اضافه شد.')
        except:
            messages.error(request, 'امکان خرید وجود ندارد .')

    data = Course.getAll()

    l = []
    for major in majors:
        i = major[0]
        name = major[1]
        for term in range(9):
            f = list(filter(lambda x: x.major == i and x.term == term, data))
            if len(f) != 0:
                l.append({
                    'list': f,
                    'name': getNameAvailableTable(name, term),
                })

    context = {
        'availableCourse': 'active',
        'detail': l,
    }
    print(l)
    return render(request, 'app/availableCourses.html', context)


def notFound(request):
    context = {}
    return render(request, 'app/not-found.html', context)


def loginUser(request):
    if request.method == 'GET':
        return render(request, 'app/login_user.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            messages.error(request, 'نام کاربری یا رمز عبور نامعتبر است')
            return render(request, 'app/login_user.html',
                          {'error': 'نام کاربری یا رمز عبور نامعتبر است'})
        else:
            messages.success(request, f' {user.username} عزیز خوش آمدید')
            login(request, user)
            return redirect('home')


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'خروج با موفقیت انجام شد.')
        return redirect('home')


# انتخاب واحد
def selectUnit(request):
    if not request.user.is_authenticated:
        messages.success(request, 'کاربر نامعتبر است')
        return redirect('login')

    current_user = request.user
    try:
        student = Student.objects.get(user=current_user)
    except:
        messages.error(request, 'شما امکان انتخاب واحد ندارید.')
        return redirect("/home")

    # get bag
    bag = []
    if 'bag' in request.session:
        bag = request.session['bag']

    if 'action' in request.GET:
        action = request.GET['action']
        print(action)
        if action == "db":
            id = int(request.GET['ci'])
            bag.remove(id)
            request.session['bag'] = bag

        elif action == "ib":
            courses = list(Course.objects.filter(id__in=bag))
            for course in courses:
                TakenLessons.objects.create(Course=course, Student=student).save()
                student.unit = student.unit + course.unit
                student.save()

                course.number_of_student = course.number_of_student + 1
                course.save()
                messages.success(request, 'درس  با موفقیت به دروس نهایی اضافه شد.')

            bag.clear()
            request.session['bag'] = bag

        elif action == "dt":
            id = request.GET['ci']
            course = Course.objects.get(id=id)
            TakenLessons.objects.get(Course=course, Student=student).delete()
            student.unit = student.unit - course.unit
            student.save()

            course.number_of_student = course.number_of_student - 1
            course.save()
            messages.success(request, 'درس با موفقیت حذف شد.')
    takeCourse = list(TakenLessons.objects.filter(Student=student))

    bagCourse = list(Course.objects.filter(id__in=bag))

    context = {
        'bagCourse': bagCourse,
        'takeCourse': takeCourse,
        'selectUnit': 'active'
    }

    return render(request, 'app/select-unit.html', context)
