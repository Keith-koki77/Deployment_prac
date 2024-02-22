from django.urls import path

from . import views

# coversation/urls.py
# Set the namespace for the app
app_name = 'conversation'

# Define the urlpatterns for the app
urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:file_pk>/', views.new_conversation, name='new'),
]