from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.contrib.auth import get_user_model

User = get_user_model()

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url =reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        # context['latest_stories'] = NewsStory.objects.all().order_by('author')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['all_users'] = User.objects.all().order_by('username')
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class userList(generic.ListView):
    model = User

class userStory(generic.DetailView):
    model = User
    template_name = 'news/user-story.html'

    slug_field = "username"
    slug_url_kwarg = "username"


class CategoryView(generic.DetailView):
    model = User
    template_name = 'news/category.html'

    # slug_field = "cat_field"
    # slug_url_kwarg = "cat_field"
    # slug_field = "username"
    # slug_url_kwarg = "username"
    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     return NewsStory.objects.all()        


#    def get_success_url(self):
        # return reverse_lazy("users:profile", kwargs={"username": self.request.user.username})
                # <a href="{% url 'users:profile' user.username %}">{{ user.username }}</a>
