from post.models import Post
from django.views.generic import ListView

from django.shortcuts import render 
from .models import Todo 

class HomeView(ListView):
	model = Post
	template_name = 'home.html'

# class TodoView(ListView):
# 	model=Todo
# 	template_name = "form.html"

def home(request): 
	if request.method == 'POST': 
		task=request.POST.get('task') 
		print(task) 
		new = Todo(task=task) 
		new.save() 
	return render(request,"form.html", {'todos': Todo.objects.all()}) 
