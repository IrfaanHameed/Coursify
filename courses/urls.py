# courses/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/update/<int:pk>/', views.student_update, name='student_update'),
    path('students/delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/create/', views.course_create, name='course_create'),
    path('courses/update/<int:pk>/', views.course_update, name='course_update'),
    path('courses/delete/<int:pk>/', views.course_delete, name='course_delete'),
    path('registrations/', views.registration_list, name='registration_list'),
    path('registrations/create/', views.registration_create, name='registration_create'),
    path('registrations/update/<int:pk>/', views.registration_update, name='registration_update'),
    path('registrations/delete/<int:pk>/', views.registration_delete, name='registration_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
