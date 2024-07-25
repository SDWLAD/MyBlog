from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=300, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return f'/{self.id}'