from django.contrib import admin
from .models import (News, Regions, OtherInfo, NationalInfo,
                     Writer, Gallery, Library, Feedback, Promo,
                     Slide, MainArticle, RelatedToTopic)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_photo', 'news_created']
admin.site.register(News, NewsAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'region_photo']
admin.site.register(Regions, RegionAdmin)


class OtherInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_1', 'email', 'website']
admin.site.register(OtherInfo, OtherInfoAdmin)


class NationalInfoAdmin(admin.ModelAdmin):
    list_display = ['info_category', 'info_title', 'info_photo', 'info_author', 'info_created']
admin.site.register(NationalInfo, NationalInfoAdmin)


class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'period']
admin.site.register(Writer, WriterAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', 'photo', 'created']
admin.site.register(Gallery, GalleryAdmin)


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['lib_name', 'lib_photo', 'lib_file', 'lib_created']
admin.site.register(Library, LibraryAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created']
admin.site.register(Feedback, FeedbackAdmin)


class PromoAdmin(admin.ModelAdmin):
    list_display = ['promo_photo', 'promo_text']
admin.site.register(Promo, PromoAdmin)


class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'description']
admin.site.register(Slide, SlideAdmin)


class MainArticleAdmin(admin.ModelAdmin):
    list_display = ['article_title1', 'article_photo1', 'created']
admin.site.register(MainArticle, MainArticleAdmin)


class RelatedAdmin(admin.ModelAdmin):
    list_display = ['topic', 'title', 'body', 'photo']
admin.site.register(RelatedToTopic, RelatedAdmin)
