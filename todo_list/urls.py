from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('uncross_off/<list_id>', views.uncross_off, name='uncross_off'),
    path('edit/<list_id>', views.edit, name='edit'),
]
