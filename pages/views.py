from django.shortcuts import render
from .models import Page

# Create your views here.

def list_view(request):
	context = {
		"xtitle": Page.objects.all(),
	}
	return render(request,'list.html', context)

def detail_view(request, page_id):
	context = {
		"xtitle": Page.objects.get(id=page_id),
	}
	return render(request, 'detail.html', context)