from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import (News, OtherInfo, Promo, Slide, MainArticle, NationalInfo,
                     Writer, Library, Gallery, Regions, RelatedToTopic)

from .forms import FeedBackForm


def base(request):
    data = dict()

    if request.method == 'POST':
        feedback_form = FeedBackForm(data=request.POST)
        if feedback_form.is_valid():
            cd = feedback_form.cleaned_data
            new_feedback = feedback_form.save(commit=False)
            new_feedback.name = cd['name']
            new_feedback.email = cd['email']
            new_feedback.comment = cd['comment']
            new_feedback.save()

    else:
        all_news = News.objects.all()[:3]
        info = OtherInfo.objects.last()
        feedback_form = FeedBackForm()
        promo = Promo.objects.last()
        data['all_news'] = all_news
        data['info'] = info
        data['feedback_form'] = feedback_form
        data['promo'] = promo

    return render(request, 'base.html', context=data)


def home(request):
    slides = Slide.objects.order_by('created')[:3]
    main_articles = MainArticle.objects.order_by('created')[:5]

    return render(request, 'index-1.html', {'slides': slides,
                                            'main_articles': main_articles
                                            })


def black(request):
    #TODO:something
    return render(request, 'index-black.html')


def small_text(request):
    #TODO:change to something
    if request.method == 'POST':
        return render(request, 'small-text-1.html')
    else:
        return render(request, 'small-text-2.html')

def big_texts(request, category):

    if category == 'adib':
        content = Writer.objects.all()
        return render(request, 'big-text.html', {'content': content})
    elif category == 'library':
        content = Library.objects.all()
        return render(request, 'big-text.html', {'content': content})
    elif category == 'gallery':
        content = Gallery.objects.all()
        return render(request, 'big-text.html', {'content': content})
    elif category == 'region':
        content = Regions.objects.all()[:12]
        return render(request, 'big-text.html', {'content': content})
    else:
        content = get_object_or_404(NationalInfo, info_category=category)
        relates = content.related.all()
        return render(request, 'big-text.html', {'content': content})

