from django.shortcuts import render
from django.http import HttpResponse


import json

def homepage(request):
    with open('db.sqlite3', encoding='utf-8') as f:
        articles = json.load(f)

    return render(request, 'content/homepage.html', {'articles': articles})

def article(request, id):
    with open('db.sqlite3.json', encoding='utf-8') as f:
        articles = json.load(f)

    article = articles[id]
    return render(request, 'content/article.html', {'article': article})
