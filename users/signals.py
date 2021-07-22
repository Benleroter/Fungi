from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from usersettings.models import Show
from usersettings.models import ShowSearchFields
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()

@receiver(post_save, sender=User)
def create_show_filters(sender, instance, created, **kwargs):
	if created:
		Show.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_search_filters(sender, instance, created, **kwargs):
	if created:
		ShowSearchFields.objects.create(user=instance)





