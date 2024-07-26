# from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render


class HomeView(TemplateView):
	"""
	View to render homepage
	"""
	template_name = 'home/home.html'


