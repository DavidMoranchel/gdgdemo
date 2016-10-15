from django.views.generic import View
from django.shortcuts import  redirect, render
from .models import Info


class GetInfo(View):
	def get(self,request):
		template="info.html"
		info = Info.objects.all()
		context = {
			'info': info,
		}
		return render(request,template,context) 
