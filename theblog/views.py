from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

class homeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class detailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPost(CreateView):
    model= Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')