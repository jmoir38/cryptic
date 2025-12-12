from lib2to3.fixes.fix_input import context

from django.urls import path
from . import views

indicator_types = [
    'anagram',
    'container',
    'hidden',
    'homophone',
    'reversal',
    'deletion',
    'letter-selection',
]

urlpatterns = [
    path('', views.home, name='home'),
    path('abbreviations/', views.abbreviations, name='abbreviations'),
    path('indicators/', views.indicators, name='indicators'),
    path('beginners-guide/', views.beginners_guide, name='beginners_guide'),
]


for itype in indicator_types:
    urlpatterns.append(path(f'indicators/{itype}/', views.indicator_detail, {'itype': itype}, name=f'indicator_{itype}'))
