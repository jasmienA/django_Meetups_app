from django.db import models
from django.db.models.fields import CharField,EmailField

# Create your models here.


class Location(models.Model):
    name = CharField(max_length=200)
    address = CharField(max_length=300)


    def __str__(self):
        return f'{self.name}({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    Participants = models.ManyToManyField(Participant, blank=True, null=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'