from django.shortcuts import render, redirect
from models import course
# Create your views here.

def index(request):
    context = { "courses": course.objects.all(), }
    print course.objects.all()
    return render(request, "courses/index.html", context)

def display(request):
    course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect("/")

def delete(request, num):
    context = {"course": course.objects.get(id=num), }
    return render(request, "courses/delete.html", context)

def final(request, num):
    current = course.objects.get(id=num)
    current.delete()
    return redirect("/")
