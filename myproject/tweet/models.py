from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    photo=models.ImageField(upload_to='photos/',blank=True,null=True)
    vibe = models.CharField(max_length=50, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    authenticity_score = models.IntegerField(default=100)
    fact_check_reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} - {self.content[:10]}'
