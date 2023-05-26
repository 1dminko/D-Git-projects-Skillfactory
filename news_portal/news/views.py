from django.shortcuts import render
from django.views.generic import ListView, DetailView
from datetime import datetime
from .models import Post, Category


class NewsList(ListView):
    model = Post
    ordering = 'datetime_create'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'dnews.html'
    context_object_name = 'news'
