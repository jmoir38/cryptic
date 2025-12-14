from django.db import models


class Abbreviation(models.Model):
    abbreviation = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.abbreviation} — {self.meaning}"


class Indicator(models.Model):
    indicator = models.CharField(max_length=100)
    word_class = models.CharField(max_length=50)

    class Meta:
        abstract = True

    def __str__(self):
        # show the concrete model name so it's clear which type an instance is
        return f"{self.__class__.__name__}: {self.indicator} ({self.word_class})"


class AnagramIndicator(Indicator):
    pass


# Add container category choices and field
CONTAINER_CATEGORY_CHOICES = [
    ("containment", "Containment"),
    ("insertion", "Insertion"),
]


class ContainerIndicator(Indicator):
    category = models.CharField(
        max_length=20,
        choices=CONTAINER_CATEGORY_CHOICES,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        cat = dict(CONTAINER_CATEGORY_CHOICES).get(self.category, self.category)
        return f"Container: {self.indicator} ({self.word_class}) - category={cat}"


class DeletionIndicator(Indicator):
    pass


class HiddenIndicator(Indicator):
    pass


class HomophoneIndicator(Indicator):
    pass


# Add selection choices and a field to the LetterSelectionIndicator
SELECTION_CHOICES = [
    ("first_letter", "First letter"),
    ("first_letters", "First letter(s)"),
    ("first_and_last", "First and last letters"),
    ("capital", "Capital letter"),
    ("either_half", "Either half"),
    ("two_letters", "Two letters"),
    ("last_letter", "Last letter"),
    ("last_letters", "Last letter(s)"),
    ("middle_letter", "Middle letter"),
    ("middle_letters", "Middle letter(s)"),
    ("other", "Other"),
]


class LetterSelectionIndicator(Indicator):
    selection = models.CharField(
        max_length=30,
        choices=SELECTION_CHOICES,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        sel = dict(SELECTION_CHOICES).get(self.selection, self.selection)
        return f"LetterSelection: {self.indicator} ({self.word_class}) - selection={sel}"


class ReversalIndicator(Indicator):
    pass
