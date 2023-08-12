
from django.contrib import admin
from django.urls import path, include
from joinlogin import views
from joinlogin.views import LoginView, RegisterView, current_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('current_user/', current_user_view, name='current-user'),
]
