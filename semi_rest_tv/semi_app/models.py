from django.db import models
class ShowManager(models.Manager):
    def validator(self,post_data):
        errors = {}

        if len(post_data['title']) < 2:
            errors['title'] = "Title too Short"

        if len(post_data['network']) < 3:
            errors['network'] = "Network length too short"

        if len(post_data['description']) < 10:
            errors['description'] = "Description Length too short"

        return errors
# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=75)
    network = models.CharField(max_length=75)
    release_date = models.DateTimeField()
    description = models.TextField(max_length=50, default= 'something')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()