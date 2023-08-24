from django.contrib import admin
from django.urls import path, include
from joinlogin import views
from joinlogin.views import LoginView, RegisterView, current_user_view, send_reset_email, reset_password_confirm
from tasks.models import Task
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet
from tasks import views as tasks_views
from contacts.views import ContactsViewSet

router = DefaultRouter()
router.register(r'task', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('current_user/', current_user_view, name='current-user'),
    path('', include(router.urls)),
    path('delete_all_tasks/', tasks_views.delete_all_tasks, name='delete-all-tasks'),
    path('contacts/', include('contacts.urls')),
    path('send_reset_email/', views.send_reset_email, name='send_reset_email'),
    path('reset_password/<uidb64>/<token>/', views.reset_password_confirm, name='password_reset_confirm'),
]
