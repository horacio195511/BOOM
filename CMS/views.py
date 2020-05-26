from django.shortcuts import render
from CMS.models import NEWS


# Create your views here.

def createNews(request):
    if request.method == 'GET':
        return render(request, 'CMS/createNews.html')
    elif request.method == 'POST':
        title = request.POST['title']
        article = request.POST['article']
        image = request.FILES['image']
        news = NEWS(title=title, article=article, image=image)
        news.save()
        return render(request, 'Action/Success.html', {'action': 'create news'})


def cms(request):
    # TODO: control center for the whole website, got the highest authority to all file
    #   customer account, thing, order and other shit.
    # TODO: build the authorization system
    return render(request, 'CMS/control_center.html')
