from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory
from django.forms import DateTimeInput
from django.contrib.admin import widgets

class StoryForm(ModelForm):

    pub_date = SplitDateTimeField(
        widget=widgets.AdminSplitDateTime()
        # widget=widgets.AdminSplitDateTime(        
            # date_attrs = {'class':'datepicker'}, # or override the ID, "id":id
            # time_attrs ={'class':'timepicker'},
            # ),

    )

    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content']
        widgets = {

            # 'pub_date': SplitDateTimeWidget(
            #     date_attrs={'class': 'datepicker'},
            #     time_attrs={'class': 'timepicker'},
            # ),
            # 'pub_date': forms.datetimepci(
            #     input_format=['%d/%m/%Y %H:%M'],
            #     attrs = {
            #         'class': 'form-control',
            #         'placeholder': 'Select a date',
            #         'type': 'datetime'
            #     }
            # ),
            'title': forms.TextInput(
                attrs={'size': 10, 
                'id': 'form-TEST',
                'placeholder': 'Enter the title',}
                ),
            'author': forms.TextInput(attrs={'size': 10, 'placeholder': 'Your name',}
            ),
            'content': forms.TextInput(attrs={'size': 10, 'placeholder': 'Enter story',}
            )
        }


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()