from typing import Text
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import News
from .forms import NewsForm

# Create your views here.
def index(request):
    #get data from DB
    news = News.objects.order_by('-create_time')
    #Create a dictionary containing the db entries in variable called news
    context = {'news': news}
    #Send the redered site with DB data elements from the context dictionary
    #are used in news/index.html
    return render(request, template_name='news/index.html', context = context)

def add(request):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            clear = news.cleaned_data
            newspost = News(**clear)
            newspost.create_time = timezone.now()
            newspost.last_edit_time = timezone.now()
            newspost.save()
            return redirect('view_news')
        else:
            context = {'form': news}
            return render(request, 'news/add.html', context)
    else:
        news = NewsForm()
        context = {'form': news}
        return render(request, 'news/add.html', context)

def get(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news': news}
    return render(request, 'news/view.html', context)

def edit(request, id):
    if request.method == 'POST':
        news = NewsForm(request.POST)
        if news.is_valid():
            clear_data = news.cleaned_data
            old_news = get_object_or_404(News, id=id)
            old_news.author = clear_data['author']
            old_news.topic = clear_data['topic']
            old_news.text = clear_data['text']
            old_news.save()
            return redirect('/news/' + str(id))
        else:
            context = {'form': news}
            return render(request, 'news/edit.html', context)
    else:    
        news_old = get_object_or_404(News, id=id)
        news = NewsForm(initial={'topic': news_old.topic,
        'author': news_old.author, 'text': news_old.text})
        context = {'form': news}
        return render(request, 'news/edit.html', context)

def delete(request, id):
    if request.method == 'POST' and request.user.is_staff and request.user.is_authenticated:
        news = get_object_or_404(News, id=id)
        news.delete()
        return redirect('view_news')
    else:
        return redirect('view_news')