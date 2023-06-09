from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime

from .forms import PostForm
from .models import Post, Category
from .filters import NewsFilter


class NewsList(ListView):
    model = Post
    ordering = 'datetime_create'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = Post
    template_name = 'dnews.html'
    context_object_name = 'news'


class CreateNews(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'news_create.html'
    context_object_name = 'create'
    form_class = PostForm
    permission_required = ('news.create_post')



    # def create_post(request):
    #     if request.method == 'POST':
    #         form = PostForm(request.POST)
    #         form.save()
    #         return HttpResponseRedirect('/news/')
    #
    #     form = PostForm()
    #     return render(request, 'news_create.html', {'form': form})


# class CreateNews(PermissionRequiredMixin, CreateView):
#     model = Post
#     template_name = 'news_create'
#     context_object_name = 'create'
#     paginate_by = 10
#     form_class = PostForm

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'edit_post.html'
    form_class = PostForm
    permission_required = ('news.change_post',)
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# def edit_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         form.save()
#         return HttpResponseRedirect('/news/')
#
#     form = PostForm()
#     return render(request, 'news_edit.html', {'form': form})


def delete_post(request):
    pass


def create_category(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
        return HttpResponseRedirect('/news/')

    form = PostForm()
    return render(request, 'category_create.html', {'form': form})


def edit_category(request):
    pass


def delete_category(request):
    pass
