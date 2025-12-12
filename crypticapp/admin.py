from django.contrib import admin

from .models import Abbreviation, Indicator


class AbbreviationAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'meaning')
    search_fields = ('abbreviation', 'meaning')
    list_per_page = 50


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'word_class')
    search_fields = ('indicator', 'word_class')
    list_per_page = 50


admin.site.register(Abbreviation, AbbreviationAdmin)
admin.site.register(Indicator, IndicatorAdmin)
