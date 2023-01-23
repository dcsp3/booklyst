from django.forms import ModelForm
from .models import ReadBooks, UnreadBooks

class BookForm(ModelForm):
    class Meta:
        model = ReadBooks
        fields = ['title_search', 'my_rating', 'date_fin', 'sentence_1', 'sentence_2', 'sentence_3','highlights']

class UnreadBookForm(ModelForm):
    class Meta:
        model = UnreadBooks
        fields = ['title_search']
