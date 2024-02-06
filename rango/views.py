from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe


def index(request):
    # about_link = "<a href='/rango/about/'>About</a>"
    # return HttpResponse(f"Rango says hey there partner! {about_link}")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')
