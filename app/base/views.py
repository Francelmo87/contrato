from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def home(request):
    template_name = 'home.html'
    return render(request, template_name)
