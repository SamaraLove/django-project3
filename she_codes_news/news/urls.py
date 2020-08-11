from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name = 'newsStory'),
    path('user-list/', views.userList.as_view(), name = 'userList'),
    path('user-story/<str:username>/', views.userStory.as_view(), name = 'userStory'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name = 'categoryStory'),

    
]
