from django import forms
from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget as RedactorEditor
from treebeard.forms import movenodeform_factory
from treebeard.admin import TreeAdmin


class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = '__all__'
        widgets = {
            'description_en': RedactorEditor(),
            'description_ru': RedactorEditor(),
            'description_uz': RedactorEditor()
        }


class SubArticleForm(forms.ModelForm):
    class Meta:
        model = SubArticle
        fields = '__all__'
        widgets = {
            'body_en': RedactorEditor(),
            'body_ru': RedactorEditor(),
            'body_uz': RedactorEditor()
        }


class RegionsForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = '__all__'
        widgets = {
            'region_description_en': RedactorEditor(),
            'region_description_ru': RedactorEditor(),
            'region_description_uz': RedactorEditor()
        }


class SlideForm(forms.ModelForm):
    class Meta:
        model = Regions
        fields = '__all__'
        widgets = {
            'description_en': RedactorEditor(),
            'description_ru': RedactorEditor(),
            'description_uz': RedactorEditor()
        }


class AdminMenu(TreeAdmin):
    form = movenodeform_factory(Menyu)
admin.site.register(Menyu, AdminMenu)


class RegionAdmin(admin.ModelAdmin):
    list_display = ['region_name', 'region_photo']
    form = RegionsForm

admin.site.register(Regions, RegionAdmin)


class NationalInfoAdmin(admin.ModelAdmin):
    list_display = ['menu', 'author']
admin.site.register(GeneralInfo, NationalInfoAdmin)


class WriterAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo', 'period']
    form = WriterForm

admin.site.register(Writer, WriterAdmin)


class MainArticleAdmin(admin.ModelAdmin):
    list_display = ['b_tild', 'b_box']
admin.site.register(MainArticle, MainArticleAdmin)


class SlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'description']
    form = SlideForm
admin.site.register(Slide, SlideAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ['news_title', 'news_photo', 'news_created']

admin.site.register(News, NewsAdmin)


class OtherInfoAdmin(admin.ModelAdmin):
    list_display = ['address', 'phone_1', 'email', 'website']

admin.site.register(OtherInfo, OtherInfoAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['category', 'photo', 'created']
admin.site.register(Gallery, GalleryAdmin)


class LibraryAdmin(admin.ModelAdmin):
    list_display = ['lib_name', 'lib_photo', 'lib_file', 'lib_created']
admin.site.register(Library, LibraryAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
admin.site.register(Feedback, FeedbackAdmin)


class PromoAdmin(admin.ModelAdmin):
    list_display = ['promo_text', 'promo_photo']
admin.site.register(Promo, PromoAdmin)


class SubArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'body', 'created']
    form = SubArticleForm
admin.site.register(SubArticle, SubArticleAdmin)


class MostVisitedAdmin(admin.ModelAdmin):
    list_display = ['title', 'region']
admin.site.register(MostVisited, MostVisitedAdmin)


class MaqolAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']
admin.site.register(Maqollar, MaqolAdmin)
