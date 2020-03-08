from django.shortcuts import render
from CMS.models import NEWS


# Create your views here.

def createNews(request):
    if request.method == 'GET':
        return render(request, 'CMS/createNews.html')
    elif request.method == 'POST':
        title = request.POST['title']
        article = request.POST['article']
        news = NEWS(title=title, article=article)
        news.save()
        return render(request, 'Action/Success.html', {'action': 'create news'})


def cms(request):
    return render(request, 'CMS/control_center.html')
