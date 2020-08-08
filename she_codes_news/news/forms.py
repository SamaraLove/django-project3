from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory

class StoryForm(ModelForm):
    # image_link = forms.URLField()
    # required=False
    
    pub_date = SplitDateTimeField(
		# use split date time field to allow the user to input both date and time
        widget=SplitDateTimeWidget(
        #    'class'="form-item",
			# we use the split date time widget to specify how the html gets built
            date_attrs={'type': 'date', 'class': "form-item", 'id': 'form-date'},
			# type date tells django to use the HTML5 date input
            time_attrs={'type': 'time', 'class': "form-item", 'id': 'form-time'},
			# type time tells django to use the HTML5 time input
            # default=timezone.now
        )
        
    )

    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content','image_link']
        widgets = {

            'title': forms.TextInput(
                attrs={'size': 10, 
                'id': 'form-title',
                'class': "form-item",
                'placeholder': 'Enter a catchy title',}
                ),
            # 'author': forms.TextInput(attrs={'size': 10,  'id': 'form-author','class': "form-item",'placeholder': 'Your name',}
            # ),
            'content': forms.Textarea(attrs={'size': 10,  'id': 'form-content','class': "form-item",'placeholder': 'Enter a rivoting story',}
            ),
            'image_link': forms.TextInput(attrs={'size': 10, 'id': 'form-link','class': "form-item",'placeholder': 'Enter URL to a direct image. If the link does not directly show an image, a random one will be chosen for you',})
            # forces you to upload with url
            # want to verify it exists. Django automatically does this 
            
        }
        


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()