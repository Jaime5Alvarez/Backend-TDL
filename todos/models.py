from django.db import models
from user.models import MyUser
import uuid
# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=500)
    date = models.DateTimeField()
    hour = models.TimeField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    user =models.ForeignKey(MyUser,on_delete=models.CASCADE   )

    def __str__(self):
        return self.title