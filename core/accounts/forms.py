from .models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):

    class Meta:
      model = User
      fields = ('email', 'password1', 'password2',)

