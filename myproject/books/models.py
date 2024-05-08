from django.db import models

from django.core import validators


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        validators=[
            validators.MinLengthValidator(10),
            validators.MaxLengthValidator(500),
        ]
    )
    
    

    def __str__(self):
        return self.title

