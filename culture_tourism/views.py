from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import (News, OtherInfo, Promo, Slide, MainArticle, GeneralInfo,
                     Writer, Library, Gallery, Regions, Menu,
                     MostVisited)

from .forms import FeedBackForm


def base(request):
    if request.method == 'POST':
        feedback_form = FeedBackForm(data=request.POST)
        if feedback_form.is_valid():
            feedback_form.save()
    else:
        feedback_form = FeedBackForm()
    return render(request, 'base.html', {'feedback_form': feedback_form})


def index(request):
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    slides = Slide.objects.all()
    news = News.objects.all()[:3]
    main_articles = MainArticle.objects.all()[:5]

    if request.method == 'POST':
        feedback_form = FeedBackForm(data=request.POST)
        feedback_form.save()
    else:
        feedback_form = FeedBackForm()

        return render(request, 'index.html', {
            'info': info_last, 'menus': menus,
            'slides': slides,'all_news': news,
            'main_articles': main_articles,'feedback_form': feedback_form
        })


def feed(request, slug_m=None):
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]


def info_with_sub(request, slug_m=None, slug_sub=None):
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]


def mainarticle(request, pk):
    related_topics = get_object_or_404(MainArticle, pk=pk).subarticle
    content = related_topics.last()
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    clock = timezone.now()


    return render(request, 'big-text.html', {'content': content,
                                             'info': info_last, 'menus': menus, 'related_topics': related_topics,
                                             'all_news': news, 'promo': promo, 'clock': clock,
                                             'most_visited': most_visited, 'gallery': gallery
                                             })
