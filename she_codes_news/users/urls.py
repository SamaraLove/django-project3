from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name ='createAccount'),
    path('profile/', views.UserProfileView.as_view(), name ='profile'),
]

