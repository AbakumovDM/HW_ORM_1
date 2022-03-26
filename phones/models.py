from django.db import models

class Phone(models.Model):

    name = models.CharField(max_length=50, null=False)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique=True)

    def __str__(self):
        return f'{self.name}, {self.image}: {self.price}, {self.release_date}, {self.lte_exists}, {self.slug}'


