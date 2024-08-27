from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(default="default_image.jpg", upload_to='image/')
    text = models.TextField()
    likes = models.IntegerField(default=0)
    ratting = models.FloatField(blank=True)
    is_published = models.BooleanField(default=True)
    creted_at = models.DateTimeField(auto_now_add=True)
