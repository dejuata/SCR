from django.views.generic import CreateView, TemplateView, UpdateView  # , DeleteView
from django.contrib.auth import get_user_model

from .forms import UserForm


class CreateUser(CreateView):
    """
    Create a new user
    """
    model = get_user_model()
    template_name = "users/user_new.html"
    form_class = UserForm
    success_url = '/login'


class ProfileUser(TemplateView):
    """
    Shows user data
    """
    template_name = "users/user_profile.html"
    form_class = UserForm


class EditUser(UpdateView):
    """
    Edit user data
    """
    model = get_user_model()
    form_class = UserForm
    template_name = "users/user_edit.html"
    success_url = '/'
