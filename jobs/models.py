from django.db import models


class Job(models.Model):
    """
    The class holds info about pictures and summary
    """
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    content = models.TextField(default='')

    def __str__(self):
        return self.summary
