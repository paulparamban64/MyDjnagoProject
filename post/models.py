from django.db import models

# Create your models here.
class Post (models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.description
    