from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/accounts/login/")
def homepage(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'main/homepage.html', {'articles': articles})


@login_required(login_url="/accounts/login/")
def articles_details(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'main/article_details.html', {'article': article})





