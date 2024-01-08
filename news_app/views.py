from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from .models import News, Category
from .forms import ContactForm
from datetime import datetime

# Create your views here.

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'news/news_full.html', context)

def aboutPageView(request):
    context = {
        
    }
    return render(request, 'news/about_page.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> Bog'langaningiz uchun rahmat! <h2>")
        context ={
            "form" : form
        }
        return render(request, 'news/contact.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:15]
        context['local_news'] = News.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[:5]
        context['abroad_news'] = News.published.all().filter(category__name="Xorij").order_by('-publish_time')[:5]
        context['tech_news'] = News.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name="Sport").order_by('-publish_time')[:5]
        
        return context
    
class TechPageView(ListView):
    model = News
    template_name = 'news/cat_news.html'
    context_object_name = 'Texnologik Yangiliklar'

    def get_context_data(self):
        tech_news = self.model.published.all().filter(category__name="Texnologiya").order_by('-publish_time')[:20]
        context ={
            "cat_news": tech_news,
            "category": "Texnologik Yangiliklar"
        }
        return context

class LocalPageView(ListView):
    model = News
    template_name = 'news/cat_news.html'
    context_object_name = 'Mahalliy Yangiliklar'

    def get_context_data(self):
        local_news = self.model.published.all().filter(category__name="Mahalliy").order_by('-publish_time')[:20]
        context ={
            "cat_news": local_news,
            "category": "Mahalliy Yangiliklar"
        }
        return context
    
class AbroadPageView(ListView):
    model = News
    template_name = 'news/cat_news.html'
    context_object_name = 'Xorij Yangiliklari'

    def get_context_data(self):
        abroad_news = self.model.published.all().filter(category__name="Xorij").order_by('-publish_time')[:20]
        context ={
            "cat_news": abroad_news,
            "category": "Xorij Yangiliklari"
        }
        return context

class SportPageView(ListView):
    model = News
    template_name = 'news/cat_news.html'
    context_object_name = 'Sport Yangiliklari'

    def get_context_data(self):
        sport_news = self.model.published.all().filter(category__name="Sport").order_by('-publish_time')[:20]
        context ={
            "cat_news": sport_news,
            "category": "Sport Yangiliklari"
        }
        return context