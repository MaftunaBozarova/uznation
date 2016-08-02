from modeltranslation.translator import translator, TranslationOptions
from .models import *


class SubArticleTranslation(TranslationOptions):
    fields = ('title', 'body',)


class MainArticleTranslation(TranslationOptions):
    fields = ('b_tild', 'b_box')


class RegionTranslation(TranslationOptions):
    fields = ('region_name', 'region_description',)


class WriterTranslation(TranslationOptions):
    fields = ('name', 'description',)


class SliderTranslation(TranslationOptions):
    fields = ('title', 'description',)


class OtherInfoTranslation(TranslationOptions):
    fields = ('description', 'address',)


class NewsTranslation(TranslationOptions):
    fields = ('news_title', 'news_data', 'news_body',)


class GalleryTranslation(TranslationOptions):
    fields = ('category', 'description',)


class LibraryTranslation(TranslationOptions):
    fields = ('lib_name', 'lib_description',)


class PromoTranslation(TranslationOptions):
    fields = ('promo_text',)


class MostVisitedTranslation(TranslationOptions):
    fields = ('title', 'body',)


class MaqolTranslation(TranslationOptions):
    fields = ('title', 'body')

translator.register(SubArticle, SubArticleTranslation)
translator.register(MainArticle, MainArticleTranslation)
translator.register(Regions, RegionTranslation)
translator.register(Writer, WriterTranslation)
translator.register(Slide, SliderTranslation)
translator.register(OtherInfo, OtherInfoTranslation)
translator.register(News,NewsTranslation)
translator.register(Gallery, GalleryTranslation)
translator.register(Library, LibraryTranslation)
translator.register(Promo, PromoTranslation)
translator.register(MostVisited, MostVisitedTranslation)
translator.register(Maqollar, MaqolTranslation)
