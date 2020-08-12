from django.contrib.auth import get_user_model
from django.db import models


class NewsStory(models.Model):

    GENDER = (
    ('x', 'Male'),
    ('y', 'Female'),
    )

    gender = models.CharField(max_length=60, blank=True, default='',choices=GENDER,verbose_name="gender")

    
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
    choice_type = models.CharField(max_length=200)


    # def __str__(self):
    #     return self.title

    #     FR = 'French'
    # IT = 'Italian'
    # MA = 'Modern Australian'
    # Category_CHOICES = [
    # (FR, 'French'),
    # (IT, 'Italian'),
    # (MA, 'Modern Australian'),
    # ]
    # category_type = models.CharField(
    # max_length=20,
    # choices=Category_CHOICES,
    # default=MA,
    # )