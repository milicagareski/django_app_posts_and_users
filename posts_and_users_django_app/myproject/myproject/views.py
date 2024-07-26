#from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
 # return HttpResponse("Hello world! I am Home page.")
  return render(request, 'home.html')
def aboutPage(request):
  #return HttpResponse("Hello! I am About page.")
  return render(request, 'about.html')