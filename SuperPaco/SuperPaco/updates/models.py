from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=150)
    
    img_1 = models.CharField(max_length=1000)
    img_2 = models.CharField(max_length=1000)

    body_1 = models.CharField(max_length=250)
    body_2 = models.CharField(max_length=800)
    body_3 = models.CharField(max_length=200)

    def __str__(self):
        return "Title Post: " + self.post_title

class Short_Post(models.Model):
    s_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = Post.post_title
    desc = Post.body_1
    img = Post.img_1