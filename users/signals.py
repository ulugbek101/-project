from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver

from .models import Profile


@receiver(post_save, sender=User)
def user_creation(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=instance,
            full_name=f"{user.first_name} {user.last_name}",
            username=user.username,
            email=user.email
        )


@receiver(post_delete, sender=Profile)
def profile_deletion(sender, instance, **kwargs):
    user = instance.user
    user.delete()


@receiver(post_save, sender=Profile)
def profile_updating(sender, instance, created, **kwargs):
    user = instance.user
    if not created:
        user.username = instance.username
        user.email = instance.email
        user.save()

# @receiver(post_delete, sender=User)
# def profile_deletion(sender, instance, **kwargs):
#     user_id = instance.id
#     profile = Profile.objects.get(user__id=user_id)
#     profile.delete()


# post_save.connect(user_creation, sender=User)
# post_save.connect(user_creation, sender=User)
