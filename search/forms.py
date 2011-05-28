from django import forms
from video.models import *

SEARCH_PAGES = (
    ('', 'any'),
    (2, '2+'),
    (10, '10+'),
    (50, '50+'),
    ('r', 'range'),
)

SEARCH_UPDATES = (
    ('', 'any'),
    ('today', 'today'),
    ('week', 'last week'),
    ('month', 'last month'),
)

class SearchForm(forms.Form):

    search = forms.CharField(max_length=255, label='search')
    page_min = forms.CharField(max_length=3)
    page_max = forms.CharField(max_length=3)
    """
    type = forms.ChoiceField(choices=COMIC_TYPES, label='type', widget=forms.CheckboxSelectMultiple())
    rating = forms.ChoiceField(choices=COMIC_RATINGS, label='rating', widget=forms.CheckboxSelectMultiple())
    genre = forms.ChoiceField(choices=COMIC_GENRES, label='genre', widget=forms.CheckboxSelectMultiple())
    tone = forms.ChoiceField(choices=COMIC_TONES, label='tone', widget=forms.CheckboxSelectMultiple())
    style = forms.ChoiceField(choices=COMIC_STYLES, label='style', widget=forms.CheckboxSelectMultiple())
    last_update = forms.ChoiceField(choices=SEARCH_UPDATES, label='last update', widget=forms.RadioSelect())
    pages = forms.ChoiceField(choices=SEARCH_PAGES, label='pages/strips', widget=forms.RadioSelect())
    """
