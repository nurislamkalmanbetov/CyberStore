from django.urls import path

from .views import *

urlpatterns = [
    path('login/', LoginView.as_view(), name='sign_in'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', user_logout, name='logout'),
    path('user/profile/update/<int:pk>/', UserUpdateView.as_view(), name='user_update')
]