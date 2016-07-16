from django.db.models import Count
from django.shortcuts import render, redirect, render_to_response
from django.shortcuts import get_object_or_404
from django.utils import timezone
import time
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from django.views.generic import DetailView
from .forms import FeedBackForm, SearchForm
from django.db.models import Q
from taggit.models import Tag


class NewsDetailView(DetailView):
    model = News
    template_name = 'news.html'

    def get_object(self, queryset=None):
        return News.objects.get(slug=self.kwargs['title'])

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        all_news = []
        try:
            all_news = News.objects.all()
            last_news = News.objects.get(slug=self.kwargs['title'])
        except Exception:
            all_news.append(News())
            last_news = News()

        context['all_news'] = all_news
        context['content'] = last_news
        return context


def feedback(request):
    if request.method == 'POST':
        feedback_form = FeedBackForm(request.POST)
        if feedback_form.is_valid():
            feedback_form.save()


def index(request):
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    slides = Slide.objects.all()
    news = News.objects.all()[:3]
    main_articles = MainArticle.objects.all()[:5]

    if "search_web" in request.POST:
        search_form = SearchForm(data=request.POST)
        if search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            resultsN = News.objects.filter(Q(news_title__icontains=search_query) | Q(news_body__icontains=search_query)).order_by('news_created')
            resultsS = SubArticle.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
            resultsR = Regions.objects.filter(Q(region_name__icontains=search_query) | Q(region_description__icontains=search_query))
            resultsW = Writer.objects.filter(Q(description__icontains=search_query) | Q(name__icontains=search_query))
            return render(request, 'search.html', {'searchN': resultsN, 'searchS': resultsS, 'searchR': resultsR, 'searchW': resultsW})
    else:
        search_form = SearchForm()

    feedback_form = FeedBackForm()

    return render(request, 'index.html', {'search_form': search_form,
        'info': info_last, 'menus': menus, 'feedback_form': feedback_form,
        'slides': slides,'all_news': news,
        'main_articles': main_articles
    })


def mainarticle(request, pk):
    main_article = get_object_or_404(MainArticle, pk=pk)
    content = main_article.subarticle.last()
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    clock = timezone.now()

    post_tags_ids = content.tags.values_list('id', flat=True)
    related_topics = SubArticle.objects.filter(tags__in=post_tags_ids).exclude(id=content.id)
    related_topics = related_topics.annotate(same_tags=Count('tags')).order_by('-same_tags', '-created')

    return render(request, 'big-text.html', {'content': content, 'middle':main_article.b_tild,
                                             'info': info_last, 'menus': menus, 'related_topics': related_topics,
                                             'all_news': news, 'promo': promo, 'clock': clock,
                                             'most_visited': most_visited, 'gallery': gallery,
                                             'second': '{}'.format(main_article.b_tild)
                                             })


def maqollar(request):
    maqol = Maqollar.objects.all()
    return render(request, 'maqol.html', {'maqollar': maqol})


def menu(request, m_menu, submenu):
    m = get_object_or_404(Menu, slug=m_menu)
    sm = get_object_or_404(SubMenu, slug=submenu)

    if submenu == 'ozbek-xalq-maqollari':
        return redirect('/maqollar')

    general = GeneralInfo.objects.get(info_menu=m, info_sub_menu=sm).subarticle.all()
    last = general.last()

    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    #clock = timezone.now()
    clock = time.asctime()
    if general.count() < 4:

        return render(request, 'big-text.html', {'content':last, 'second': submenu,
                                                 'info': info_last, 'menus': menus, 'related_topics': general,
                                                 'all_news': news, 'promo': promo, 'clock': clock,
                                                 'most_visited': most_visited, 'gallery': gallery
                                                 })
    else:
        object_list = general
        paginator = Paginator(general, 4)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return render(request,'small-text.html', {'page': page, 'posts':posts,
            'info': info_last, 'menus': menus, 'second': submenu,
            'all_news': news, 'promo': promo, 'clock': clock,
            'most_visited': most_visited, 'gallery': gallery
        })


def small_to_big(request, title, s):
    content = SubArticle.objects.get(slug=title)
    #general = content.generalinfo
    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    clock = timezone.now()

    return render(request, 'big-text.html', {'content':content, 'second': s,
                                                 'info': info_last, 'menus': menus,
                                                 'all_news': news, 'promo': promo, 'clock': clock,
                                                 'most_visited': most_visited, 'gallery': gallery
                                                 })


def news(request, title):
    if title == 'last':
        last_news = News.objects.last()
    else:
        last_news = News.objects.get(slug=title)

    all_news = News.objects.all()

    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    clock = timezone.now()
    if request.method == 'POST':
        search_query = request.POST['search-word']
        results = News.objects.filter(Q(news_title__icontains=search_query) | Q(news_body__icontains=search_query)).order_by('news_created')
    return render(request, 'news.html', {
        'content': last_news,
        'info': info_last, 'menus': menus,
        'all_news': all_news, 'promo': promo, 'clock': clock,
        'most_visited': most_visited, 'gallery': gallery
    })


def most_visited(request, name, region):
    most_visited_obj = MostVisited.objects.get(n_slug=name, r_slug=region)

    info_last = OtherInfo.objects.last()
    menus = Menu.objects.all()
    promo = Promo.objects.last()
    news = News.objects.all()[:3]
    most_visited = MostVisited.objects.all()[:5]
    gallery = Gallery.objects.all()[:9]
    clock = timezone.now()

    return render(request, 'big-text.html', {'content': most_visited_obj,
                                             'info': info_last, 'menus': menus,
                                             'all_news': news, 'promo': promo, 'clock': clock,
                                             'most_visited': most_visited, 'gallery': gallery
                                             })
