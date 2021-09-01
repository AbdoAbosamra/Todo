from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    # !Note That on_delete which if user account is deleted all childs will delete
    # If we want to be task null ater deleteing SET_NULL.
    # null = True that means that is theory that can be submit a form without value to database.

    title = models.CharField(max_length=50)

    description = models.TextField(null=True , blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering =["complete"]
