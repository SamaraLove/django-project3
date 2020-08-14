from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):

    CHOICES = (
    ('About', 'About'),
    ('Adventures', 'Adventures'),
    ('Friends', 'Friends'),
    ('Family', 'Family'),
    # ('No Category Assigned', 'No Category Assigned'),
    )

    category = models.CharField(max_length=60, blank=True, default='No Category Assigned',choices=CHOICES,verbose_name="gender")

    
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name="stories"
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_link = models.URLField(default = "", max_length=400)


    # def __str__(self):
    #     return self.title
