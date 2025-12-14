from django.contrib import admin

from .models import (
    Abbreviation,
    AnagramIndicator,
    ContainerIndicator,
    DeletionIndicator,
    HiddenIndicator,
    HomophoneIndicator,
    LetterSelectionIndicator,
    ReversalIndicator,
)


class AbbreviationAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'meaning')
    search_fields = ('abbreviation', 'meaning')
    list_per_page = 50


class SimpleIndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'word_class')
    search_fields = ('indicator', 'word_class')
    list_per_page = 50


class LetterSelectionAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'selection', 'word_class')
    search_fields = ('indicator', 'selection', 'word_class')
    list_per_page = 50


class ContainerIndicatorAdmin(admin.ModelAdmin):
    list_display = ('indicator', 'category', 'word_class')
    search_fields = ('indicator', 'category', 'word_class')
    list_per_page = 50


admin.site.register(Abbreviation, AbbreviationAdmin)
admin.site.register(AnagramIndicator, SimpleIndicatorAdmin)
admin.site.register(ContainerIndicator, ContainerIndicatorAdmin)
admin.site.register(DeletionIndicator, SimpleIndicatorAdmin)
admin.site.register(HiddenIndicator, SimpleIndicatorAdmin)
admin.site.register(HomophoneIndicator, SimpleIndicatorAdmin)
admin.site.register(LetterSelectionIndicator, LetterSelectionAdmin)
admin.site.register(ReversalIndicator, SimpleIndicatorAdmin)
