from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import NewsStory

class StoryForm(ModelForm):
    image_link = forms.URLField(required=False,help_text='Enter URL to a direct image. Otherwise, a random image will be chosen for you')
            
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
        fields = ['title', 'pub_date', 'content','image_link', 'gender']
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
            'image_link': forms.TextInput(attrs={'size': 10, 'id': 'form-link','class': "form-item",'placeholder': 'Enter URL to a direct image. Otherwise, a random image will be chosen for you',},),
            # 'category_type':forms.CharField(attrs={
            # forces you to upload with url
            # want to verify it exists. Django automatically does this 
            # 'cuisine_type' = forms.CharField(max_length=10),
        }

    # def delete(self, request, *args, **kwargs):
    #     """If DB Integrity Error, display msg and redirect to list"""
    #     try:
    #         return(super().delete(request, *args, **kwargs))
    #     except IntegrityError:
    #         messages.error(request, "Cannot be deleted")
    #         return render(request, template_name=self.template_name, context=self.get_context_data())

class UpdateStoryForm(ModelForm):
    image_link = forms.URLField(required=False)
    
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
        fields = ['title', 'pub_date', 'content','image_link','gender']
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
            'image_link': forms.TextInput(attrs={'size': 10, 'id': 'form-link','class': "form-item",'placeholder': 'Enter URL to a direct image. Otherwise, a random image will be chosen for you',})            
        }
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     if commit:
    #         user.save()
    #     return user
    

class DeleteStoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = []
    
    def delete(self, request, *args, **kwargs):
        """If DB Integrity Error, display msg and redirect to list"""
        try:
            return(super().delete(request, *args, **kwargs))
        except IntegrityError:
            messages.error(request, "Cannot be deleted")
            return render(request, template_name=self.template_name, context=self.get_context_data())



    # def delete(request, *args, **kwargs):
    #     self.object = self.get_object()
    #     # if self.object.gameteams_set.exists():
    #         # Return the appropriate response
    #     success_url = self.get_success_url()
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()