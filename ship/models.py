from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=1200)
    product_quantity = models.CharField(max_length=1200)
    status = models.CharField(max_length=1200,choices=[
    ("BOUGHT", "BOUGHT"), 
    ("NOT AVAILABLE", "NOT AVAILABLE"), 
    ("PENDING", "PENDING"), 
 ])
    date = models.DateField()

