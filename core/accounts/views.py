from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
User = get_user_model()


class Logout_View(LogoutView):
    next_page = "/"


class Login_View(LoginView):
    template_name = "accounts/login.html"
    fields = "username","password"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:post_list")


class Register_View(FormView):
    template_name = "accounts/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy("todo:post_list")
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            return redirect("accounts:login")
        return super(Register_View, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todo:post_list")
        return super(Register_View, self).get(*args, **kwargs)