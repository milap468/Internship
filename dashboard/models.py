from django.db import models
from accounts.models import User
import uuid

# Create your models here.

class Post(models.Model):

    post_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userposts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_image = models.ImageField(blank=True,null=True,default="static/dashboard/images/img1.jpg",upload_to="posts")
    
    def __str__(self):

        return self.title

class Like(models.Model):

    like_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    like_count = models.IntegerField(default=0)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="postslike")
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="userlikes")

    def __str__(self):

        return self.user.email

class Comment(models.Model):

    comment_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="postscomment")
    comment = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="usercomments")

    def __str__(self):

        return self.user.email
    


