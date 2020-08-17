from django.urls import reverse_lazy
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse

# User = get_user_model()

# Create your views here.

class CreateAccountView(generic.edit.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# class UserProfileView(generic.TemplateView):
class UserProfileView(generic.edit.UpdateView):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile.html'   

    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"username": self.request.user.username})

    slug_field = "username"
    slug_url_kwarg = "username"

    # def test_func(self):
    #     obj = self.get_object()
    #     return obj == self.request.user

class UserProfileEditView(UserPassesTestMixin, LoginRequiredMixin, generic.edit.UpdateView):
    """
    Processes requests for the settings page, where users
    can edit their profiles.
    """
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'users/profile_edit.html'   
    context_object_name = 'storyForm'


    def get_success_url(self):
        return reverse_lazy("users:profile", kwargs={"username": self.request.user.username})

    slug_field = "username"
    slug_url_kwarg = "username"

    # def get_object(self):
    #     object = get_object_or_404(User, username=self.kwargs.get("username"))
    #     # only owner can view their page
    #     if self.request.user.username == object:
    #         return object
    #     else:
    #         # redirect to 404 page
    #         print("you are not the owner!!")

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user


    # def test_func(self):
    #     x = self.request.user.username
    #     y = self.kwargs['username']
    #     if x == y:
    #         return True
    #     else:
    #         if self.request.user.is_authenticated():
    #             raise Http404("You are not authenticated to edit this profile")

    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user == story.author:
    #         return True
    #     return False

    # def get_object(self):

    #     object = get_object_or_404(User, username=self.kwargs.get("username"))

    #     # only owner can view their page
    #     if self.request.user.username == object.username:
    #         return object
    #     else:
    #         # redirect to 404 page
    #         print("you are not the owner!!")
 
# @login_required 
# def profile(request, template_name = 'users/profile.html'):
#     """
#     Processes requests for the settings page, where users
#     can edit their profiles.
#     """
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             print('form changed')
#             return redirect('users:profile')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#     return render(request, 'news.html', {'form':form})

# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html



# https://gist.github.com/haxoza/7921eaf966a16ffb95a0
# https://dev-yakuza.github.io/en/django/custom-user-model/