from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


# posts = [
#     {
#         'author': 'juliet',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': '12 April 2023'
#     },

#     {
#         'author': 'agutu',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': '14 April 2023'
#     }
# ]

def home(request):
    context ={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


    

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post   
    fields = ['title', 'content']


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
