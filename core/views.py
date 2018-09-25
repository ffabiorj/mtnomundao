from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from accounts.models import User

class HomePageView(TemplateView):

    template_name = 'index.html'


class MembersListView(ListView):

		template_name = 'members.html'
		model = User



class TransportView(TemplateView):
    
		template_name = 'transport.html'

class PhotosView(TemplateView):
    
		template_name = 'photos.html'


class ContactView(TemplateView):
	
		template_name = 'contact.html'

