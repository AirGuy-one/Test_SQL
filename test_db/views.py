from django.shortcuts import render, redirect, HttpResponse
from .models import TestData
from .forms import TestDataForm


def index(request):
    data = TestData.objects.all()
    return render(request, 'index.html', {'data': data})


def about(request):
    return render(request, 'about.html')


def add(request):
    if request.method == "POST":
        form = TestDataForm(request.POST)
        try:
            form.save()
            return redirect('home')
        except:
            form.add_error(None, 'Adding to database with using form error')

    else:
        form = TestDataForm()

    return render(request, 'add.html', {'form': form})


def some(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f"""
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User-agent: {user_agent}</p>
        """)


def user(request):
    age = request.GET.get("age", 18)
    name = request.GET.get("name", "No_name")
    return HttpResponse(f"<h2>Имя: {name}  Возраст: {age}</h2>")


def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

















