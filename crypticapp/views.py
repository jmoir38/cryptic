from django.shortcuts import render
from django.http import Http404

INDICATOR_TYPES = [
    'anagram',
    'container',
    'hidden',
    'homophone',
    'reversal',
    'deletion',
    'letter-selection',
]


def home(request):
    """Render the site homepage with links to main sections."""
    context = {
        'title': 'Macaroni\'s Cryptic Helper',
        'intro': 'Welcome to my collated collection of cryptic crossword resources!(views.py).',
    }
    return render(request, 'home.html', context)


def abbreviations(request):
    """Render the abbreviations landing page."""
    context = {
        'title': 'Abbreviations',
        'description': 'Abbreviations description (views.py).',
    }
    # templates live at crypticapp/templates/*.html, so render the direct filename
    return render(request, 'abbreviations.html', context)


def indicators(request):
    """Render the indicators landing page with links to subtypes."""
    context = {
        'title': 'Indicators',
        'indicator_types': INDICATOR_TYPES,
    }
    return render(request, 'indicators.html', context)


def indicator_detail(request, itype=None):
    """Render a page for a specific indicator type."""
    if itype not in INDICATOR_TYPES:
        raise Http404('Indicator type not found')

    title = itype.replace('-', ' ').title()
    context = {
        'title': f'{title} Indicators',
        'type': itype,
        'description': f'A list of {title} indicators and their relevant qualities.',
    }
    return render(request, 'indicator_detail.html', context)

def beginners_guide(request):
    """Render the beginner's guide page."""
    context = {
        'title': "Beginner's Guide",
        'description': 'An introduction to solving cryptic crosswords.',
    }
    return render(request, 'beginner.html', context)
