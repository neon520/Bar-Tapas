from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

class Bar(models.Model):
    nombre = models.CharField(max_length=30, unique=True, null=False)
    direccion = models.CharField(max_length=50, unique=True, null=False)
    num_visitas= models.IntegerField(default=0)

    slug = models.SlugField()

    def save(self, *args, **kwargs):
            # Uncomment if you don't want the slug to change every time the name changes
            #if self.id is None:
                    #self.slug = slugify(self.name)
            self.slug = slugify(self.nombre)
            super(Bar, self).save(*args, **kwargs)

    def __str__(self):  #For Python 3, use __unicode__ on Python 2
        return self.nombre

class Tapa(models.Model):
    Bar = models.ForeignKey(Bar, null=False)
    nombre = models.CharField(max_length=30, unique=True, null=False)
    votos= models.IntegerField(default=0)

    def __str__(self):      #For Python 3, use __unicode__ on Python 2
        return self.nombre


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):      #For Python 3, use __unicode__ on Python 2
        return self.user.username
