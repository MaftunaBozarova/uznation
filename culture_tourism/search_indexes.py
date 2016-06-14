from haystack import indexes
from .models import News, NationalInfo


class NewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    publish = indexes.DateTimeField(model_attr='news_created')

    def get_model(self):
        return News

    def index_queryset(self, using=None):
        return self.get_model().objects.all()