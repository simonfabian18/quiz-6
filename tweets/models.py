from django.db import models
from django.conf import settings
class Tweet(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    # The __str__ method should be indented inside the class
    def __str__(self):
        return str(self.content)

