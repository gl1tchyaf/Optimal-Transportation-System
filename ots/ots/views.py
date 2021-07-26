from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def homepage(request):
    return redirect('articles:list')


@login_required(login_url="/accounts/login/")
def about(request):
    # return HttpResponse("About")
    return render(request, 'about.html')
