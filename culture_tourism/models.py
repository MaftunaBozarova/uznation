from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, related_name='sub_menu')
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('created',)


class SubArticle(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='main_article/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class GeneralInfo(models.Model):
    info_menu = models.ForeignKey(Menu, related_name='category')
    info_sub_menu = models.ForeignKey(SubMenu, related_name='submenu', blank=True, null=True)
    subarticle = models.ManyToManyField(SubArticle, related_name='generalinfo')
    author = models.CharField(max_length=100, blank=True)


class MainArticle(models.Model):
    b_tild = models.CharField(max_length=200, unique=True)
    b_box = models.CharField(blank=True, max_length=200, null=True)
    subarticle = models.ManyToManyField(SubArticle, related_name='mainarticle')

    def __str__(self):
        return '{} {}'.format(self.b_tild, self.b_box)


class Regions(models.Model):
    region_name = models.CharField(max_length=70)
    region_photo = models.ImageField(upload_to='regions/', blank=True)
    region_description = RichTextField()

    def __str__(self):
        return self.region_name


class Writer(models.Model):
    PERIOD = (
        ('first', 'till 12 century'),
        ('second', 'from 12 to 18 century'),
        ('third', 'from 18 century till now')
    )
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='writers/', blank=True)
    period = models.CharField(max_length=50, choices=PERIOD, default='second')
    # TODO:RichTextField
    description = RichTextField()


class Slide(models.Model):
    title = models.TextField(blank=True)
    photo = models.ImageField(upload_to='slide/', blank=False)
    description = RichTextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class OtherInfo(models.Model):
    description = RichTextField()
    address = models.CharField(max_length=255, blank=True)
    phone_1 = models.CharField(max_length=17, blank=True)
    phone_2 = models.CharField(max_length=17, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    site_logo = models.ImageField(blank=True)
    logo_footer = models.ImageField(blank=True)


class News(models.Model):
    news_title = models.CharField(max_length=200, blank=True, db_index=True)
    news_slug = models.SlugField(max_length=200, blank=True)
    news_photo = models.ImageField(upload_to='news/', blank=True)
    news_body = RichTextField()
    news_created = models.DateTimeField(default=timezone.now)


class Gallery(models.Model):
    category = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='gallery/')
    description = RichTextField()
    created = models.DateTimeField(auto_now_add=True)


class Library(models.Model):
    lib_name = models.CharField(max_length=255, blank=True)
    lib_photo = models.ImageField(upload_to='library/', blank=True)
    lib_file = models.FileField(upload_to='library/', blank=True)
    lib_description = RichTextField()
    lib_created = models.DateTimeField(auto_now_add=True, blank=True)


class Feedback(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    comment = RichTextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ('created',)


class Promo(models.Model):
    promo_photo = models.ImageField(upload_to='promo/', blank=True)
    promo_text = RichTextField()
    promo_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('promo_created',)


class MostVisited(models.Model):
    name = models.CharField(max_length=200)
    region = models.ForeignKey(Regions, related_name='region')

    def __str__(self):
        return self.name

