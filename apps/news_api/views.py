from django.shortcuts import render, redirect
from datetime import datetime
import datetime
import requests

# Create your views here.
def index(request):
    url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=fad2a37dcc0940059524bc53c204f3ee')
    response = requests.get(url)
    news_data = response.json()
    articles = news_data['articles']
    # first = response.json()[0]
    context = {
        # 'id': news_data['id'],
        # 'description': news_data['description'],
        'news_data': news_data,
        # 'first': first
    }
    # print response.json()
    # print news_data
    print articles
    return render(request, 'news_api/index.html', context)