from django.shortcuts import render 
from .models import Todo 
# Create your views here. 
def todo(request): 
	if request.method == 'POST': 
		task=request.POST.get('task') 
		print(task) 
		new = Todo(task=task) 
		new.save() 
		return render(request,"todo.html", {'todos': Todo.objects.all()})
	else:
		return render(request,"form.html", {'todos': Todo.objects.all()}) 
