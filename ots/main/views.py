from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/accounts/login/")
def homepage(request):
    buses = Article.objects.all().order_by('date')
    return render(request, 'main/homepage.html', {'articles': buses})


@login_required(login_url="/accounts/login/")
def bus_details(request, slug):
    # return HttpResponse(slug)
    buses = Article.objects.get(slug=slug)
    return render(request, 'main/bus_details.html', {'article': buses})


@login_required(login_url="/accounts/login/")
def about(request):
    # return HttpResponse("About")
    return render(request, 'main/about.html')


@login_required(login_url="/account/login/")
def contact(request):
    return render(request, 'main/contact.html')


@login_required(login_url="/account/login/")
def bolaka(request):
    return render(request, 'main/bolaka.html')


