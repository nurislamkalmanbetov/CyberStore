from django.shortcuts import render, redirect
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
    UpdateView
)
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import LoginForm, UserRegisterForm
from .forms import UserUpdateForm
from .models import User
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data['email']
        password = data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('main_page')
            else:
                return HttpResponse("Ваш аккаунт неактивен")
        return HttpResponse("Такого юзера не существует")


class UserRegisterView(CreateView):
    template_name = "register.html"
    form_class = UserRegisterForm
    success_url = reverse_lazy('main_page')


# generic - готовый классы с готовым решением,
# для стандартных задач


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main_page')




class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = "user_update.html"
    success_url = reverse_lazy('main_page')
    queryset = User.objects.all()
    model = User

    def test_func(self):
        if self.kwargs.get('pk') == self.request.user.pk:
            return True
        return False





