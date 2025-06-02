from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('members/', views.member_list, name='member_list'),               # seznam členů
    path('members/<int:id>/', views.member_detail, name='member_detail'),  # detail člena
]
