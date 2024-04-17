from django.urls import path
# from . import views
from .views import *

urlpatterns = [
	path('',todo,name="todo"),
	path('delete/<int:todo_id>/', delete, name='delete'),
]
