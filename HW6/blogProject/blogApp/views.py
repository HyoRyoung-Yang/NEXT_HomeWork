from django.shortcuts import render, redirect
from .models import Article
import time

# Create your views here.
def index(request):
    movie_number = Article.objects.filter(category="movie").count()
    drama_number = Article.objects.filter(category="drama").count()
    programming_number = Article.objects.filter(category="programming").count()
    print(movie_number)
    print(drama_number)
    print(programming_number)
    return render(request, 'index.html', {'mn':movie_number, 'dn':drama_number, 'pn':programming_number})

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})

def new(request):
    if request.method == 'POST':
    #POST 요청일 경우
        print(request.POST) #data확인
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            a_time = time.ctime(time.time()),
        )
        return redirect('detail', article_pk=new_article.pk)
    
    #POST 요청이 아닐 경우
    return render(request, 'new.html')

def movie(request):
    articles_m = Article.objects.filter(category="movie")
    return render(request, 'movie.html', {'articles': articles_m})

def drama(request):
    articles_d = Article.objects.filter(category="drama")
    return render(request, 'drama.html', {'articles': articles_d})

def programming(request):
    articles_p = Article.objects.filter(category="programming")
    return render(request, 'programming.html',{'articles': articles_p})