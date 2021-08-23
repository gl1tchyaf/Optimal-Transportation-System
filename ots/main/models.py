
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    def __str__(self):
        return self.title


RATE_CHOICES=[
    (1, '1 - Trash'),
    (2, '2- Horrible'),
    (3, '3- Terrible'),
    (4, '4- Bad'),
    (5, '5- OK'),
    (6, '6- Rideable'),
    (7, '7- Good'),
    (8, '8- Very good'),
    (9, '9- Perfect'),
    (10, '10- Best'),

]


class balaka(models.Model):
    name = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES, null=True)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)


def __str__(self):
    return self.name
