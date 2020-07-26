from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True, null=True)
    date_event = models.DateTimeField(verbose_name='Events date')
    date_criation = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta: #table will be event and not core_event
        db_table = 'event'
    
    def __str__(self):
        return self.title