# courses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, Course, Registration
from .forms import StudentForm, CourseForm, RegistrationForm, RegisterForm
from django.db.models import Count

def dashboard(request):
    total_students = Student.objects.count()
    total_courses = Course.objects.count()
    total_registrations = Registration.objects.count()

    completed_courses = Course.objects.filter(status='completed').count()
    in_progress_courses = Course.objects.filter(status='in_progress').count()
    not_started_courses = Course.objects.filter(status='not_started').count()
    students_per_course = Course.objects.annotate(num_students=Count('registration'))

    radar_data = students_per_course.values('name', 'num_students')

    context = {
        'total_students': total_students,
        'total_courses': total_courses,
        'total_registrations': total_registrations,
        'completed_courses': completed_courses,
        'in_progress_courses': in_progress_courses,
        'not_started_courses': not_started_courses,
        'radar_data': list(radar_data),
        'students_per_course': list(students_per_course),
    }
    return render(request, 'dashboard.html', context)





@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

@login_required
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

@login_required
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})

@login_required
def registration_list(request):
    registrations = Registration.objects.all()
    return render(request, 'registration_list.html', {'registrations': registrations})

@login_required
def registration_create(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration_form.html', {'form': form})

@login_required
def registration_update(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=registration)
        if form.is_valid():
            form.save()
            return redirect('registration_list')
    else:
        form = RegistrationForm(instance=registration)
    return render(request, 'registration_form.html', {'form': form})

@login_required
def registration_delete(request, pk):
    registration = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        registration.delete()
        return redirect('registration_list')
    return render(request, 'registration_confirm_delete.html', {'registration': registration})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
