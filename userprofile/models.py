from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from autoslug import AutoSlugField

from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='avatars', default='avatars/guest.png')
    cover_image = models.ImageField(upload_to='avatars', default='avatars/cover.png')
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    age = models.CharField(max_length=20, blank=True)
    instrument = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=20, blank=True)
    music_style = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, blank=True)
    friends = models.ManyToManyField("Profile", blank=True)
    slug = AutoSlugField(populate_from='user')


    def __str__(self):
	    return str(self.user.username)

    def get_absolute_url(self):

        return "/userprofile/{}".format(self.slug)



class FriendRequest(models.Model):
	to_user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)




@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()

#post_save.connect(save_profile, sender=User)
