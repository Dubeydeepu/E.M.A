from django.http import HttpResponse
from django.shortcuts import render
import datetime
def home(request):
    date = datetime.datetime.now()
    isActive=True
    name="AspiringDjangoDeveloper"
    list_of_programs=[
          'WAP to check even or odd',
          'WAP to check prime number',
          'WAP to print all prime numbers from 1 to 100',
          'WAP to print pascals triangle' 
    ]
    student={
          'student_name':"Sarthak",
          'student_college':"USICT",
          'student_city':"MayurVihar"
    }
    data={
       'date':date,
       'isActive':isActive,
       'name':name,
       'list_of_programs':list_of_programs,
       'student_data':student
    }
    print("test function is called from view")
   # return HttpResponse("<h1>Hello this is index page</h1>"+str(date))
    return render(request,"home.html",data)

def about(request):
   # return HttpResponse("<h1>This is about Page</h1>")
   return render(request,"about.html",{})

def services(request):
   # return HttpResponse("<h1>This is services Page</h1>")
   return render(request,"services.html",{})