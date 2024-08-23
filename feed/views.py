from typing import Any
from django.views.generic import ListView, CreateView
from .models import Feed, User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.contrib.auth.models import User


# function based view
# class based view

class Login(LoginView):
    template_name = "login.html"
    fields = ["username", "password"]
    # redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    # def get_success_url(self) -> Any:
    #     return reverse_lazy("home")
    
class Logout(LogoutView):
    next_page = reverse_lazy("home")


class HomePage(ListView):
    model = Feed
    template_name = "index.html"

    # context data
    # object_list
    # {
    #  "author": "user",
    #  "text": "text",
    #  "created_at": "date",
    #  "image": "image"
    # }


class CreateFeed(LoginRequiredMixin, CreateView):
    model = Feed
    fields = ["text", "image"]
    template_name = "create_post.html"
    success_url = reverse_lazy("home") # this return user to hom page
    login_url = reverse_lazy("login") # this return user to login page

    def form_valid(self, form):
        """ Associate post with the current logged in user as its author"""
        
        # get the id of current logged in user
        user_id = self.request.user.id
        
        # retrieve the user with this id
        user = User.objects.get(id=user_id)
        
        # add author to the post
        form.instance.author = user
        
        # form.instance.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)
