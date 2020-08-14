from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name = 'newsStory'),
    path('user-list/', views.userList.as_view(), name = 'userList'),
    path('user-story/<str:username>/', views.userStory.as_view(), name = 'userStory'),
    path('edit/<int:pk>/', views.StoryViewEdit.as_view(), name='userStoryEdit'),
    path('delete/<int:pk>/', views.StoryViewDelete.as_view(), name='userStoryDelete'),
    # path('category/<str:category_type>/', views.categoryStoryView.as_view(), name = 'categoryStory'),
    path('filter3/', views.StoryFilterView.as_view(), name = 'filter'),

]
