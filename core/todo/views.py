from typing import Any, Dict
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import PostForm
from .models import Post



class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "todo/post_list.html"



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = '/'


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/'


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'


class PostCompleteView(LoginRequiredMixin, View):
    model = Post
    success_url = '/'

    def get(self, request, *args, **kwargs):
        object = Post.objects.get(id=kwargs.get("pk"))
        object.status = True
        object.save()
        return redirect(self.success_url)