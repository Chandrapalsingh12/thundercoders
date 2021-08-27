from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    sno = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    post_thumbnail = models.ImageField(upload_to="images/")
    heading = models.TextField(max_length=110, default='Heading contain only 110 word') 
    content = models.TextField(max_length=500000)  
    author = models.CharField(max_length=50)  
    slug = models.CharField(max_length=130)
    timestamp = models.DateField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    Facebook_id = models.TextField(max_length=100, default="https://facebook.com/thechandrapalsinghrajput")
    Instagram_id = models.TextField(max_length=100, default="https://instagram.com/thechandrapalsinghrajput")
    twitter_id = models.TextField(max_length=100, default="https://twitter.com/thechandrapalsinghrajput")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + 'by' + self.author 
    
class Contact(models.Model):
    sno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name +' - ' + self.email



    
