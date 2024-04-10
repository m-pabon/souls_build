from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=100, primary_key=True)  # Using title as the primary key

    def __str__(self):
        return self.title
