from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    '''
    this is a class to define posts for blog app
    '''
    user = models.ForeignKey('accounts.profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

    class Meta:
        ordering = ['-user']

