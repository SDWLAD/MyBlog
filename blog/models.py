from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=300, null=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/{self.id}'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   image = models.ImageField(default='default.jpg',  
                                     upload_to='profile_pics')
   def __str__(self):
      return f'{self.user.username} Profile'