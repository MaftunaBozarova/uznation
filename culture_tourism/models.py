from django.db import models
from django.utils import timezone


class Base(models.Model):
    REGIONS = (
        ('toshkent', 'Toshkent'),
        ('andijon', 'Andijon'),
        ('fargona', 'Farg\'ona'),
        ('namangan', 'Namangan'),
        ('sirdaryo', 'Sirdaryo'),
        ('jizzax', 'Jizzaz'),
        ('samarqand', 'Samarqand'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('surhondaryo', 'Surhondaryo'),
        ('buxoro', 'Buxoro'),
        ('navoiy', 'Navoiy'),
        ('xorazm', 'Xorazm'),
        ('qoraqalpogiston', 'Qoraqalpog\'iston')
    )
    #TODO:translate
    CATEGORY = (
        ('wedding-sovchi', 'Wedding-Sovchilik'),
        ('wedding-toyoldi', 'Wedding-Toy-oldi'),
        ('wedding-kelin-salom', 'Wedding-Kelin-salom'),
        ('wedding-beshik-toy', 'Wedding-Beshik-toy'),
        ('holiday', 'Holiday'),
        ('clothes', 'Clothes'),
        ('game', 'Game'),
        ('symbol', 'Symbol'),
        ('song', 'Song'),
        ('fairytale', 'Fairytale'),
        ('maqol', 'Maqol'),
        ('donli', 'Donli ekinlar'),
        ('meva', 'Meva'),
        ('sabzavot', 'Sabzavot'),
        ('qazilma', 'Qazilma'),
        ('sanat', 'San\'at'),
        ('obida', 'Obida'),
        ('zamonaviy-bino', 'Zamonaviy bino')
    )
    PERIOD = (
        ('17', ' till XVII century'),
        ('17-20', 'XVII - XX centuries'),
        ('20', 'Since XX century')
    )


class News(Base):
    news_title = models.CharField(max_length=200, blank=True, db_index=True)
    news_slug = models.SlugField(max_length=200, blank=True)
    news_photo = models.ImageField(upload_to='news/', blank=True)
    #TODO:RichTextField
    news_body = models.TextField()
    news_created = models.DateTimeField(default=timezone.now)


class Regions(Base):
    region_name = models.CharField(max_length=70, choices=Base.REGIONS, default='toshkent')
    region_photo = models.ImageField(upload_to='regions/', blank=True)
    # TODO:RichTextField
    region_description = models.TextField()


class OtherInfo(Base):
    address = models.CharField(max_length=255, blank=True)
    phone_1 = models.CharField(max_length=17, blank=True)
    phone_2 = models.CharField(max_length=17, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    site_logo = models.ImageField(blank=True)
    logo_footer = models.ImageField(blank=True)


class NationalInfo(Base):
    info_category = models.CharField(max_length=50, choices=Base.CATEGORY, default='holiday')
    info_title = models.CharField(max_length=255, blank=True)
    info_photo = models.ImageField(upload_to='national/', blank=True)
    # TODO:RichTextField
    info_body = models.TextField()
    info_author = models.CharField(max_length=100, blank=True)
    info_created = models.DateTimeField(auto_now_add=True)


class Writer(Base):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='writers/', blank=True)
    period = models.CharField(max_length=50, choices=Base.PERIOD, default='20', blank=True)
    # TODO:RichTextField
    description = models.TextField()


class Gallery(Base):
    category = models.CharField(max_length=50, choices=Base.CATEGORY, default='holiday')
    photo = models.ImageField(upload_to='gallery/')
    # TODO:RichTextField
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Library(Base):
    lib_name = models.CharField(max_length=255, blank=True)
    lib_photo = models.ImageField(upload_to='library/', blank=True)
    lib_file = models.FileField(upload_to='library/', blank=True)
    # TODO:RichTextField
    lib_description = models.TextField(blank=True)
    lib_created = models.DateTimeField(auto_now_add=True, blank=True)


class Feedback(models.Model):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    # TODO:RichTextField
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=False, blank=True)

    class Meta:
        ordering = ('created',)


class Promo(Base):
    promo_photo = models.ImageField(upload_to='promo/', blank=True)
    # TODO:RichTextField
    promo_text = models.TextField(blank=True)


class Slide(Base):
    title = models.TextField(blank=True)
    photo = models.ImageField(upload_to='slide/', blank=False)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class MainArticle(Base):
    b_word1 = models.CharField(blank=True, null=True, max_length=100)
    b_word2 = models.CharField(blank=True, null=True, max_length=100)
    b_word3 = models.CharField(blank=True, null=True, max_length=100)
    b_tild = models.CharField(blank=True, max_length=200, null=True)
    b_box = models.CharField(blank=True, max_length=200, null=True)
    b_image = models.ImageField(upload_to='main_article/', blank=True)
    #main information

    article_title1 = models.CharField(max_length=255, blank=True)
    #TODO:RichTextField
    article_body1 = models.TextField(blank=True)
    article_photo1 = models.ImageField(upload_to='main_article/', blank=True)

    article_title2 = models.CharField(max_length=255, blank=True)
    # TODO:RichTextField
    article_body2 = models.TextField(blank=True)
    article_photo2 = models.ImageField(upload_to='main_article/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    article_title3 = models.CharField(max_length=255, blank=True)
    # TODO:RichTextField
    article_body3 = models.TextField(blank=True)
    article_photo3 = models.ImageField(upload_to='main_article/', blank=True)


class RelatedToTopic(Base):
    topic = models.ForeignKey(NationalInfo, related_name='related')
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField(blank=True)
    photo = models.ImageField(upload_to='related/', blank=True)