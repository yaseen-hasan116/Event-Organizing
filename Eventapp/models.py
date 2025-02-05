from django.db import models

# Create your models here.

class Card(models.Model):
    marraige_date = models.CharField(max_length=20, null=True)
    couple_names = models.CharField(max_length=255, null=True)
    card_text = models.TextField(null=True)
    card_images = models.ImageField(upload_to='images/')

class Gallery(models.Model):
    gallery_images = models.ImageField(upload_to='images/')

class Services(models.Model):
    service_image = models.ImageField(upload_to='images/')
    service_name = models.CharField(max_length=20)

    def __str__(self):
        return self.service_name

class Venue(models.Model):
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

class Ocassion(models.Model):
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    description = models.TextField(null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

class Decoration(models.Model):
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

class Photography(models.Model):
    service_name = models.ForeignKey(Services, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)

class Packages(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    detail_description = models.TextField()
    price = models.CharField(max_length=30)

class CoupleMoments(models.Model):
    names = models.CharField(max_length=50)
    couple_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.names

class WeddingGallery(models.Model):
    names = models.ForeignKey(CoupleMoments, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    heading_image = models.ImageField(upload_to='images', blank=True)
    images = models.ImageField(upload_to='images/', blank=True)

class Contact(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    date = models.DateField(auto_now=True)
    guests = models.CharField(max_length=255)
    country = models.CharField(max_length=30)
    message = models.TextField()