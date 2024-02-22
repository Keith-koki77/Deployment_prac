from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .forms import LoginForm

app_name = 'books'

urlpatterns = [
	path('', views.landing, name='landing'),
	path('index/', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('reviews/', views.reviews, name='reviews'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('faqs/', views.faqs, name='faqs'),
    path('privacy/', views.privacy, name='privacy'),
   	path('login/', auth_views.LoginView.as_view(template_name='books/login.html', authentication_form=LoginForm), name='login'),
 	path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),
]
