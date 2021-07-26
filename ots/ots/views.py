from django.http import HttpResponse
from django.shortcuts import render, redirect


def homepage(request):
    return redirect('articles:list')


def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')
