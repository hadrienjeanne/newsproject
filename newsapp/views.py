from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key ='7e9207542a564348a755591e7164b421')
    top = newsapi.get_top_headlines()
  
    art = top['articles']
    desc = []
    news = []
    img = []
    urls = []
    source = []
  
    for i in range(len(art)):
        f = art[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        urls.append(f['url'])
        source.append(f['source']['name'])
    mylist = list(zip(news, desc, img, urls, source))

    print(set(mylist))
  
    return render(request, 'index.html', context={"mylist":mylist})