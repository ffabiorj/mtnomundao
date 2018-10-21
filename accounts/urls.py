

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('alterar-senha/', views.change_password, name='update_password'),
    path('registro/', views.RegisterView.as_view(), name='register'),
    path('atualizar/', views.ChangeUserView.as_view(), name='update_user'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_don.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confi.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_comple.html'), name='password_reset_complete'),

]