from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

User = get_user_model()

# Create your views here.

class CreateAccountView(generic.edit.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class UserProfileView(generic.TemplateView):
    template_name = 'users/profile.html'
    
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

    # def get_context_data(self, **kwargs):
    #     '''Return all news stories.'''
    #     kwargs = super().get_context_data(**kwargs)
    #     kwargs["object"]=User.objects.get(pk=self.request.user.id)
    #     return kwargs
