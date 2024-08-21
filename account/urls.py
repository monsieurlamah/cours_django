from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register_user, name="account-register"),
    path('login/', views.login_user, name="account-login"),
    path('logout/', views.logout_user, name="account-logout")
]
