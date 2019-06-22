from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Elyor'}) # Here is "Elyor" is a dynamic name


def add(request):

    val1 = int(request.POST['num1'])

    val2 = int(request.POST['num2'])

    Sum = val1 + val2

    return render(request, 'result.html', {'result': Sum})
