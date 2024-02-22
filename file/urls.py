from django.urls import path

from . import views

app_name = 'file'

urlpatterns = [
    path('', views.files, name='files'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:file_id>/download/', views.download, name='download'),  # Corrected URL pattern
    path('<int:file_id>/payment/', views.payment, name='payment'),
    path('<int:file_id>/process_payment/', views.process_payment, name='process_payment'),
]
