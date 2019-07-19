from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if postData['email'] and not re.match(EMAIL_REGEX, postData['email']) and len(postData['email']) < 5:
            errors["email1"] = 'Invalid email'
        if len(postData['password1'])<8 :
            errors["password"] = 'Password at least 8 characters'
        if postData['password1'] != postData['password2']:
            errors["password1"]=' password not match'

        return errors


class Users(models.Model):
    first_name=models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()