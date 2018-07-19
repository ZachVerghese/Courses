from __future__ import unicode_literals
from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['Name']) <5:
            errors['Name']="Name must be at least 5 characters"
        if len(postData['Description']) < 15:
            errors['Description']="Description must be at least 15 characters"
        return errors


class Course(models.Model):
    Name= models.CharField(max_length=255)
    Description=models.TextField()
    Date_Added=models.DateTimeField(auto_now_add = True)
    objects=CourseManager()
