from django.db import models

from .search import SearchOne


class ReadBooks(models.Model):
    title_search = models.CharField(max_length=10000000, default='')
    my_rating = models.FloatField(null=True, blank=True, default=0.0)
    date_fin = models.CharField(max_length=10000000, null=True, blank=True)
    sentence_1 = models.CharField(max_length=10000000, null=True, blank=True, default='1) ')
    sentence_2 = models.CharField(max_length=10000000, null=True, blank=True, default='2) ')
    sentence_3 = models.CharField(max_length=10000000, null=True, blank=True, default='3) ')
    highlights = models.TextField(null=True, blank=True)

    book_id = models.CharField(max_length=10000000, default='-')
    title = models.CharField(max_length=10000000, default='-')
    subtitle = models.CharField(max_length=10000000, default='-', null=True, blank=True)
    author = models.CharField(max_length=10000000, default='  ')
    genre = models.CharField(max_length=10000000, null=True, blank=True)
    cover = models.CharField(max_length=10000000, default='-')

    def save(self, *args, **kwargs):
        self.book_id = SearchOne(self.title_search)[0]['id']
        self.title = SearchOne(self.title_search)[0]['title']
        self.subtitle = SearchOne(self.title_search)[0]['subtitle']
        self.author = SearchOne(self.title_search)[0]['author']
        self.genre = SearchOne(self.title_search)[0]['genre']
        self.cover = SearchOne(self.title_search)[0]['img']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class UnreadBooks(models.Model):
    title_search = models.CharField(max_length=10000000, default='')

    book_id = models.CharField(max_length=10000000, default='')
    title = models.CharField(max_length=10000000, default='')
    subtitle = models.CharField(max_length=10000000, default='', null=True, blank=True)
    author = models.CharField(max_length=10000000, default='')
    summary = models.TextField(null=True, blank=True)
    cover = models.CharField(max_length=10000000, default='')

    def save(self, *args, **kwargs):
        self.book_id = SearchOne(self.title_search)[0]['id']
        self.title = SearchOne(self.title_search)[0]['title']
        self.subtitle = SearchOne(self.title_search)[0]['subtitle']
        self.author = SearchOne(self.title_search)[0]['author']
        self.summary = SearchOne(self.title_search)[0]['summary']
        self.cover = SearchOne(self.title_search)[0]['img']
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
