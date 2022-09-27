from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def category_options(request):
  return render(request, 'step1.html')

def developer_form(request):
  return render(request, "developer_form.html")