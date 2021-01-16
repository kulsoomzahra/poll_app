from django.forms import ModelForm
from .models import Poll


#A model form will simply take an existing model in your app and create a form based off it.

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
