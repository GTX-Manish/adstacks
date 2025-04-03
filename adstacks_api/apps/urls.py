from django.urls import path
from . import views

urlpatterns = [
    path('add-app/', views.add_app, name='add_app'),
    path('get-app/<int:id>/', views.get_app, name='get_app'),
    path('delete-app/<int:id>/', views.delete_app, name='delete_app'),
]