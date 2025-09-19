from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Topic user is studying"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns string representation of model"""
        return self.text

class Entry(models.Model):
    """Add specifics about topics"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns simple string for entry"""
        return f"{self.text[:50]}..."

