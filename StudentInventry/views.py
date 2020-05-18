from django.shortcuts import render
import json

def home(request):
  with open('StudentInventry/all_student_data.json','r') as file:
    file = json.load(file)
  return render(request,'home.html',{'file':file})


def profile(request,Studentname):
  with open('StudentInventry/all_student_data.json','r') as file:
    file = json.load(file)
  return render(request,'profile.html',{'file':file,'Studentname':Studentname})