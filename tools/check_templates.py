import importlib, django, os
from django.template import loader, TemplateDoesNotExist

# Ensure we load project settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cryptic.settings')

s = importlib.import_module('cryptic.settings')
print('TEMPLATES DIRS:', s.TEMPLATES[0]['DIRS'])
print('STATIC_URL:', s.STATIC_URL)
print('STATICFILES_DIRS:', s.STATICFILES_DIRS)

# Initialize Django
django.setup()

templates = ['base.html','home.html','abbreviations.html','indicators.html','indicator_detail.html']
for tpl in templates:
    try:
        loader.get_template(tpl)
        print('FOUND:', tpl)
    except TemplateDoesNotExist:
        print('MISSING:', tpl)

# Check static CSS file exists on filesystem
css_path = os.path.join(s.BASE_DIR, 'static', 'css', 'site.css')
print('CSS path:', css_path)
print('CSS exists:', os.path.exists(css_path))

