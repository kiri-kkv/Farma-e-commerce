from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home),
    path('your-orders/', views.customerOrder),
    path('',include('django.contrib.auth.urls')),
    path('userlogin/', views.userLogin),
    path('register/', views.register),
    path('pesticide/',views.pesticide),
    path('fertilizers/',views.fertilizers),
    path('insecticide/',views.insecticide),
    path('review/',views.review),
]