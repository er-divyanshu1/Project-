from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Event(models.Model):
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)
    title =models.CharField(max_length=150)
    dec =models.TextField()
    liked =models.ManyToManyField(User, default=None, blank=True,related_name='liked')
    date = models.DateTimeField(auto_now_add=True,null=True)
    img=models.ImageField(upload_to='my_img', null=True, blank=True)
    

def __str__(self):
    return str(self.title)

@property
def num_likes(self):
    return self.liked.all.count()

LIKE_CHOICE=(
    ('Like','Like'),
    ('Unlike','Unlike'),

)

class Like(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    value =models.CharField(choices=LIKE_CHOICE, default='Like' ,max_length=10)

def __str__(self):
    return str(self.title)