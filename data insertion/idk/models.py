from django.db import models

# Create your models here.


class ExlData(models.Model):
    age = models.TextField(null=True)
    fare = models.TextField(null=True)
    name = models.TextField(null=True)
    # github = models.URLField(max_length=200, default="")

    def __str__(self):
        return self.name
