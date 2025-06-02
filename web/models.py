from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)  # Jméno
    email = models.EmailField()              # Email
    bio = models.TextField()                 # Popis / Bio

    def __str__(self):
        return self.name
