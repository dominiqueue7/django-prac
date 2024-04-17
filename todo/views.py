from django.shortcuts import render 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo 
 
def todo(request): 
	if request.method == 'POST': 
		task=request.POST.get('task') 
		print(task) 
		new = Todo(task=task) 
		new.save() 
		return render(request,"todo.html", {'todos': Todo.objects.all()})
	else:
		return render(request,"form.html", {'todos': Todo.objects.all()}) 

@csrf_exempt
def delete(request, todo_id):
    if request.method == 'DELETE':
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
        return JsonResponse({'status': 'success'})