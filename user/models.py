from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
    


# User Model

class CustomUser(AbstractUser):
    """Manages Core Authentication and Roles.

    """
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        NORMAL = 'NORMAL', 'Normal'
        SYSTEM = 'SYSTEM', 'System' # system/machine role for internal service
        
    role = models.CharField(
        max_length=100,
        choices=Role.choices,
        default=Role.NORMAL
    )
    
    #TODO Email : latter add email verification
    email = models.EmailField(unique=True)
    
    def save(self, *args, **kwargs):
        # automatically grant superuser status to custom admin role
        if self.role == self.Role.ADMIN:
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
            
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"


class UserProfile(models.Model):
    """Manages extended user data.
    
    """
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    
    # Profile specific fields
    organization = models.CharField(max_length=255, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Profile for {self.user.email}"
    
# --- Signals to automatically create a profile when user is created ---

@receiver(post_save, sender=CustomUser)
def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
        # If the user was just created, create the profile
        UserProfile.objects.create(user=instance)
    else:
        # If the user is just being updated
        instance.profile.save()
