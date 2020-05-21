from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

import dateutil.parser
import feedparser

def index(request):

    if request.GET.get("url"):

        url = request.GET["url"] #Getting URL

        feed = feedparser.parse(url) #Parsing XML data

        published_sorted = sorted(feed.entries,key=lambda entry: dateutil.parser.parse(entry.published))

    else:

        feed = None

    if request.GET.get('sort') and feed:

            sort = request.GET['sort']

            if sort == '2':
                published_sorted.reverse()
                feed['entries'] = published_sorted

            if sort == '3':
                feed['entries'] = published_sorted

    return render(request, 'home.html', {

    'feed' : feed,

    })
