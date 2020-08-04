from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_link = models.URLField(default = "",max_length=400)

    def __str__(self):
        return self.title