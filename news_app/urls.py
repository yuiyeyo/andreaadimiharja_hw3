from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("articles/<int:id>/", views.article_detail, name="article_detail"),
    path("search/", views.search, name="search"),
]


