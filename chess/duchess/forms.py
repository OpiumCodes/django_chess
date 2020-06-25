from django.forms import ModelForm
from .models import *

class RegisterPlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'