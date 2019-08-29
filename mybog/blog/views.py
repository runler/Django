from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def index(request):
    # return HttpResponse("hello 中国")
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def action_page(request):
    title = request.POST.get('title','默认Title')
    content = request.POST.get('content','默认Content')
    article_id = request.POST.get('article_id','0')

    if article_id == '0':
        models.Article.objects.create(title=title,content=content) #对数据库增加数据
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content=content
    article.save()
    return render(request,'blog/article_page.html',{'article':article})
