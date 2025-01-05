from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CostumUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CostumUser
        fields = UserCreationForm.Meta.fields + ('name')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CostumUser
        fields = UserChangeForm.Meta.fields
        
        