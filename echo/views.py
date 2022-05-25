from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'echo/index.html')


def image(request):
    return render(request, 'echo/echo_image.html')
