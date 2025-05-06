from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('product/', views.single_product, name='single_product'),
    path('contact/', views.contact, name='contact'),
]
