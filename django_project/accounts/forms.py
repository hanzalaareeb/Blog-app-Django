from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(AdminUserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = AdminUserCreationForm.Meta.fields + ('name',)
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
        
        
        