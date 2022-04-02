from uuid import uuid4
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, VerificationToken
from .utils import token_generator, send_email_verification_link



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        token = token_generator(64)
        token_uuid = uuid4().hex
        VerificationToken.objects.create(profile=profile, value=token, token_uuid=token_uuid)
        # send_email_verification_link("Email Verification",instance.username, instance.email, "Please verify your account", f"http://localhost:8000/user/verify/{token_uuid}/{token}", "VERIFY MY ACCOUNT")

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    # instance.(maybe follow the reciever object?).save()
