# courses/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    STATUS_CHOICES = (
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('not_started', 'Not Started'),
    )

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    # Add other fields as needed

    def __str__(self):
        return self.name

class Registration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} registered for {}".format(self.student.name,self.course.name)
