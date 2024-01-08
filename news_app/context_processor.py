from .models import News, Category

def latest_news(request):
    latest_news = News.published.all().order_by("-publish_time")[:10]
    category_all = Category.objects.all()

    context = {
        "latest_news": latest_news,
        "category_all": category_all
    }

    return context