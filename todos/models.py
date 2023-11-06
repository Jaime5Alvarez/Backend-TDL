from django.db import models
from user.models import MyUser
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    user =models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True    )

    def __str__(self):
        return self.title