from django.urls import path
from .views import news_detail, HomePageView, ContactPageView, TechPageView, \
     aboutPageView, LocalPageView, AbroadPageView, SportPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    path('news/<slug:news>/', news_detail, name="full_news"),
    path('local/', LocalPageView.as_view(), name="local_news"),
    path('abroad/', AbroadPageView.as_view(), name="abroad_news"),
    path('sport/', SportPageView.as_view(), name="sport_news"),
    path('tech/', TechPageView.as_view(), name="tech_news"),
    path('contact', ContactPageView.as_view(), name="contact_page"),
    path('about-us', aboutPageView, name="about_page"),
]