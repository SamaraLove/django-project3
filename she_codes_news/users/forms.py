from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email', 'bio', 'location','birth_date']
        # fields = ['username','email', 'birth_date']

        widgets = {
            'birth_date': forms.DateInput(format = ('%m/%d/%Y'),
                attrs = {'class': 'form-item',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'bio': forms.TextInput(attrs={'size': 10,  'id': 'form-bio','class': "form-item",'placeholder': 'Enter a brief description',}
            ),           
        }

    # class ProfileForm()

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username','email', 'bio', 'location','birth_date']

        widgets = {
            'birth_date': forms.DateInput(format = ('%m/%d/%Y'),
                attrs = {'class': 'form-item',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'bio': forms.TextInput(attrs={'size': 10,  'id': 'form-bio','class': "form-item",'placeholder': 'Enter a brief description',}
            ),           
        }
     
     
     