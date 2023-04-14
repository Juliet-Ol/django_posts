from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'juliet',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': '12 April 2023'
    },

    {
        'author': 'agutu',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '14 April 2023'
    }
]

def home(request):
    context ={
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
