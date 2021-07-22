from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Cap

'''@receiver(pre_save, sender=Cap)
def on_change(sender, instance: Cap, **kwargs):
	DP = Cap.objects.get(Fungi_id= instance.id)
	if not DP:
		DP.DataPresent = False

@receiver(post_save, sender=Cap)
def save_cap(sender, instance, **kwargs):
	Cap.DataPresent = True
	Cap.save(update_fields=['DataPresent'])
	#dp = instance.DataPresent

	#Fungi.cap.DataPresent = False
	#instance.Cap.save()
	#instance.DataPresent.save()
	#Cap.DataPresent = True
	#instance.DataPresent= True
	#C = instance.DataPresent
	#Cap.DataPresent.save()
	#instance.Cap.save()
	#instance.cap.save()
	#instance.DataPresent.save()
	#C.save()
	C = Cap
	C.DataPresent = True
	C.save()


@receiver(post_save, sender=User)
	def save_profile(sender, instance, **kwargs):
		instance.profile.save()

instance.DataPresent = True#.save()
instance.save()#Cap.DataPresent = True'''

 