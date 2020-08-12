from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,ReadOnlyPasswordHashField
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username','email', 'first_name', 'last_name','bio', 'location','birth_date', ]
        # fields = ['username','email', 'birth_date']

        widgets = {
            'birth_date': forms.DateInput(format = ('%m/%d/%Y'),
                attrs = {'class': 'form-item',
                    'id': 'form-birth_date',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'bio': forms.Textarea(attrs={'size': 10,  'id': 'form-bio','class': "form-item",'placeholder': 'Enter a short bio about yourself',}
            ),   
            'location': forms.TextInput(attrs={'id': 'form-location','class': "form-item",'placeholder': 'Enter your city name',}
            ),            
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    # class ProfileForm()
# forms.ModelForm
class CustomUserChangeForm(UserChangeForm):
    # password = ReadOnlyPasswordHashField(
    #     label="Password",
    #     help_text="Raw passwords are not stored, so there is no way to see "
    #               "this user's password, but you can change the password "
    #               "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = CustomUser
        fields = ['email', 'bio', 'location','birth_date']
        # fields = ['username','first_name', 'last_name', 'date_joined','email', 'bio', 'location','birth_date']
        # fields = '__all__'
        widgets = {
                'birth_date': forms.DateInput(format = ('%m/%d/%Y'),
                    attrs = {'class': 'form-item',
                        'placeholder': 'Select a date',
                        'type': 'date'
                    }
                ),
                'bio': forms.Textarea(attrs={'size': 10,  'id': 'form-bio','class': "form-item",'placeholder': 'Enter a brief description',}
                ),     
                # 'password': forms.HiddenInput(),
                # 'groups': forms.HiddenInput(),
                # 'is_superuser': forms.HiddenInput(),
                # 'user_permissions': forms.HiddenInput(),
                # 'is_active': forms.HiddenInput(),
                # 'is_staff': forms.HiddenInput(),
            }

    # def __init__(self, *args, **kwargs):
    #     super(CustomUserChangeForm, self).__init__(*args, **kwargs)
    #     self.fields['password'].help_text = self.fields['password'].help_text.format('../password/')
    #     f = self.fields.get('user_permissions', None)
    #     if f is not None:
    #         f.queryset = f.queryset.select_related('content_type')

    # def clean_password(self):
    #         return self.initial["password"]

   
     
     
     