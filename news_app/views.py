import random
from django.shortcuts import render, get_object_or_404
from .models import VisualContent
from .models import Article


def base(request):
    articles = Article.objects.all()  
    featured_article = random.choice(articles) if articles else None  

    return render(request, "home.html", {"featured_article": featured_article})


def search(request):
    query = request.GET.get("query", "").strip()  
    articles = Article.objects.filter(headline__icontains=query) if query else []  

    return render(request, "search_results.html", {"query": query, "articles": articles})


#def article_detail(request, id):
#    article = get_object_or_404(Article, article_id=id)  # Ensure `article_id` is correct
#    return render(request, "article.html", {"article": article})  # Use "article.html"

def article_detail(request, id):
    article = get_object_or_404(Article, article_id=id)
    related_articles = Article.objects.exclude(article_id=id)[:3]  

    return render(request, "article.html", {
        "article": article,
        "articles": related_articles,  
    })



def home(request):
    articles = Article.objects.all()
    
    global_visuals = VisualContent.objects.filter(article__isnull=True)

    article_visuals = VisualContent.objects.filter(article__isnull=False)
    

    return render(request, "home.html", {
        "articles": articles,
        "global_visuals": global_visuals,
        "article_visuals": article_visuals,
    })


