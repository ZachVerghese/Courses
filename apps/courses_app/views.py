from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def index(request):
    all_courses = Course.objects.all()
    context={
        "courses":all_courses
    }
    return render(request, 'courses_app/index.html',context)

def add(request):
    errors= Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request,value)
    else:
        Course.objects.create(
            Name=request.POST['Name'], 
            Description=request.POST['Description']
            )
    return redirect('/')

def destroy(request, course_id):
    Course.objects.get(id=course_id)
    context={
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses_app/destroy.html',context)

def delete(request, course_id):
    c = Course.objects.get(id=course_id)
    c.delete()
    return redirect('/')