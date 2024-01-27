from django.db import models
from django.contrib.auth.models import User 
from datetime import datetime 


# Create your models here.
class Blog(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    desc = models.TextField(null=False)
    date = models.DateTimeField(default=datetime.now,null=True)
    
    # date=models.DateTimeField(null=True)
    def __str__(self):
        return self.title
    
