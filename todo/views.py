from django.shortcuts import redirect, render 
from django.views.decorators.csrf import csrf_exempt
from .models import Todo 
from django import forms 
from asgiref.sync import sync_to_async

@csrf_exempt
def delete(request, todo_id):
	if request.method == 'POST':
		todo = Todo.objects.get(id=todo_id)
		todo.delete()
	return redirect('todo')

@csrf_exempt
def post(request): 
	if request.method == 'POST': 
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('todo')
		
class TodoForm(forms.ModelForm):
	task = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'Enter Task'}
	))
	class Meta:
		model = Todo
		fields = ['task']

def todo(request): 
	form = TodoForm()
	todos = Todo.objects.all()
	return render(request, "form.html", {'form': form, 'todos': todos})