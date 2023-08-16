
from django.contrib import admin
from django.urls import path, include
from joinlogin import views
from joinlogin.views import LoginView, RegisterView, current_user_view
from addTask.models import AddTask
from rest_framework.routers import DefaultRouter
from addTask.views import AddTaskViewSet
from addTask import views as addTask_views



router = DefaultRouter()
router.register(r'add_task', AddTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('current_user/', current_user_view, name='current-user'),
    path('', include(router.urls)),
    path('delete_all_tasks/', addTask_views.delete_all_tasks, name='delete-all-tasks'),

]
