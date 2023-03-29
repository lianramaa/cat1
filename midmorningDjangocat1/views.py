from django.shortcuts import render

from .forms import RegForm, Hr_employee

def Regform(request):
    submit_button = request.POST.get("btn-reg")
    name = ''
    email = ''
    password = ''
    form = RegForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'submit_button': submit_button,
               'name': name, 'email': email, 'password': password}

    return render(request, 'register.html', context)


def hr_employee(request):
    submit_button = request.POST.get("btn-reg")
    name = ''
    email = ''
    password = ''
    form = hr_employee(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
    context = {'form': form, 'submit_button': submit_button,
               'name': name, 'email': email, 'password': password}

    return render(request, 'employee.html', context)


def index(request):
    return render(request, 'index.html')


def innerpage(request):
    return render(request, 'inner-page.html')


def employee(request):
    return render(request, 'employee.html')




def register(request):
    return render(request, 'register.html')
