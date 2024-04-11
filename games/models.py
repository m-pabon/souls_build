from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    slug = models.CharField(max_length=100, default='elden_ring')

    def __str__(self):
        return self.title
