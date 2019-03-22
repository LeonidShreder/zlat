from django.urls import path
from Profile import views

urlpatterns = [
    path('profile/', views.UserProfileList),
    path('profile/<int:pk>/', views.UserProfileDetail),
]