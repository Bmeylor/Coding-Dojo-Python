from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, post_data):
        errors = {}

        if len(post_data['first_name']) < 2:
            errors['first_name'] = "Not Enough Characters"
        
        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Not Enough Characters"
        
        if len(post_data['password']) < 8:
            errors['password'] = "Not Enough Characters"
        
        if post_data['password'] != post_data['confirm_password']:
            errors['password_match'] = "Passwords do not match"
        
        try:
            self.get(email = post_data['email'])
            errors['email_unique'] = "Email address already used."
        except:
            pass
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        
        if not EMAIL_REGEX.match(post_data['email']):            
            errors['email'] = "Invalid email address!"
        
        return errors

# Create your models here.
class User(models.Model):
    first_name =models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()