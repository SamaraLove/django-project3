from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget

from .models import NewsStory


class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget=SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )

    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        widgets = {
            'title': forms.TextInput(
                attrs={'size': 10,
                       'id': 'form-TEST',
                       'placeholder': 'Enter the title', }
            ),
            'author': forms.TextInput(attrs={'size': 10, 'placeholder': 'Your name', }
                                      ),
            'content': forms.TextInput(attrs={'size': 10, 'placeholder': 'Enter story', }
                                       )
        }

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()
