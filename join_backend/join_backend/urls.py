
from django.contrib import admin
from django.urls import path, include
from joinlogin import views
from joinlogin.views import LoginView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
