from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from accounts.models import User
from core.models import Gallery
from .forms import PhotoForm

class HomePageView(TemplateView):

    template_name = 'index.html'


class MembersListView(ListView):

	template_name = 'members.html'
	context_object_name = 'person_list'
	queryset = User.objects.all()


class TransportView(TemplateView):
    
	template_name = 'transport.html'


class PhotosView(ListView):

	template_name = 'photos.html'
	context_object_name = 'galleries'
	queryset = Gallery.objects.all()


class ContactView(TemplateView):

	template_name = 'contact.html'


class AddPhotoView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
		
	template_name = 'add_photo.html'
	form_class = PhotoForm
	success_url = reverse_lazy('add_photos')
	success_message = 'A foto foi adicionada com sucesso!'


class SearchView(ListView):

	template_name = 'seach.html'
	context_object_name = 'searches'

	def get_queryset(self):
		queryset = User.objects.all()
		q = self.request.GET.get('search', '')
		if q == '' and q is not None:
			queryset = ''
		else:
			queryset = queryset.filter(name__icontains=q)
		return queryset


class ProfileView(DetailView):

	model = User
	template_name = 'profile.html'
	context_object_name = 'profile'
	
	

	
	


