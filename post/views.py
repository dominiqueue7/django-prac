from .models import Post
from django.views.generic import ListView

class PostView(ListView):
	model = Post
	template_name = 'posts.html'
	ordering = ['-created_on']
