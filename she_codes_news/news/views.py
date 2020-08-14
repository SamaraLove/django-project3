from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm, UpdateStoryForm, DeleteStoryForm
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views import generic
from django.db.models import Count, F, Value

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
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        # context['all_stories'] = NewsStory.objects.all().order_by('-category_type')
        context['all_users'] = User.objects.all().order_by('username')
        return context

class StoryFilterView(generic.ListView):
    template_name = 'news/filter3.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        qs = NewsStory.objects.all()   
        q = self.request.GET.get("category")
        if q: 
            qs = qs.filter(category=q)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StoryForm
        print(context)
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class userList(generic.ListView):
    model = User
    template_name = 'news/user-list.html'

class userStory(generic.DetailView):
    model = User
    template_name = 'news/user-story.html'

    slug_field = "username"
    slug_url_kwarg = "username"
    success_url =reverse_lazy('users:profile')


class categoryStoryView(generic.DetailView):
    pass
    # model = NewsStory
    # template_name = 'news/category.html'
    # context_object_name = 'story'

    # slug_field = "category_type"
    # slug_url_kwarg = "category_type"

#     @property
#    def total_number(self):
#        return self.category_type.all().count()

class StoryViewEdit(generic.edit.UpdateView):
    form_class = UpdateStoryForm
    context_object_name = 'storyForm'

    model = NewsStory
    template_name = 'news/edit.html'
    context_object_name = 'story'

    success_url =reverse_lazy('news:index')

class StoryViewDelete(generic.edit.DeleteView):
    form_class = DeleteStoryForm
    context_object_name = 'storyForm'

    model = NewsStory
    template_name = 'news/delete.html'
    context_object_name = 'story'

    success_url =reverse_lazy('news:index')

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         form.delete()
    #         return redirect('news:index')

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     object = get_object_or_404(NewsStory, author=self.kwargs.get("author"))
    #     if request.method == 'POST':
    #         form = self.form_class(request.POST, instance=order)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('news:story')
    #     else:
    #         form = PostForm(instance=post)
    #     return render(request, self.template_name, {'form': form})


# https://samulinatri.com/blog/django-modelform-tutorial/
            # form = PostForm(request.POST)



    # def my_view(request):
    #     # form = StoryForm
    #     return render_response('news/index.html',{'form': form})