from django.shortcuts import render
from .models import Article


# Create your views here.
def homepage(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'main/homepage.html', {'articles': articles})
