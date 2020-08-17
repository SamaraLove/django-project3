from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name ='createAccount'),
    path('profile/<str:username>/', views.UserProfileView.as_view(), name ='profile'),
    path('profile/edit/<str:username>/', views.UserProfileEditView.as_view(), name ='profileEdit'),

]

