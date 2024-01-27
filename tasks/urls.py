from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.Registration.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.TaskListView.as_view(), name='dashboard'),
    path('task-create/', views.TaskCreateView.as_view(), name='create'),
    path('task-detail/<int:pk>/', views.TaskDetailView.as_view(), name='details'),
    path('task-update/<int:pk>/', views.TaskUpdateView.as_view(), name='update'),
    path('task-delete/<int:pk>/', views.TaskDeleteView.as_view(), name='delete'),
    


]