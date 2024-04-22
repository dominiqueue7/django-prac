from django.urls import path
# from . import views
from .views import *

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('signup/', SignupView.as_view(), name='signup'),
  path('fx-chart/', FxChartView.as_view(), name='fx-chart'),
]
