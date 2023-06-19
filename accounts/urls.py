from django.urls import path
from . import views
urlpatterns = [
    path('user-register',views.user_register,name="user-register"),
    path('user-login',views.user_login,name="user-login"),
    path('user-logout',views.user_logout,name="user-logout"),
    path('forgot-password',views.forgot_password,name="forgot-password"),
    # path('change-password/<str:email>',views.change_password,name="change-password")
]