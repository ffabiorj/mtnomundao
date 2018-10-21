from django.shortcuts import render, render, redirect

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.generic.edit import (
    CreateView, UpdateView, FormView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserAdminCreationForm, UserAdminChangeForm


class RegisterView(SuccessMessageMixin, CreateView):

    model = User
    template_name = 'accounts/register_user.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('login')
    success_message = 'Conta criada com sucesso!'


class ChangeUserView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    template_name = 'accounts/update_user.html'
    form_class = UserAdminChangeForm
    success_url = reverse_lazy('home')
    success_message = 'Atualizaçao feita com sucesso!'

    def get_object(self):
        return self.request.user


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'A senha foi alterada com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija o erro abaixo!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/update_password.html', {'form': form})


