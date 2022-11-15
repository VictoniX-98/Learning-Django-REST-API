from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def api():
    pass

def app_home(request):
    return render(request, 'app_home.html')