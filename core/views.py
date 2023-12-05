from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def activacion(request):
    return HttpResponse("Aqui esta el modulo activacion")

def login(request):
    return HttpResponse("Hola, soy login")

