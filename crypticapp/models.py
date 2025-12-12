from django.db import models


class Abbreviation(models.Model):
    abbreviation = models.CharField(max_length=50)
    meaning = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.abbreviation} — {self.meaning}"

class Indicator(models.Model):
    indicator = models.CharField(max_length=50)
    word_class = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.indicator} ({self.word_class})"





