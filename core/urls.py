from django.urls import path
from .views import *
urlpatterns = [
    path('tasks/',TaskListCreateView.as_view(),name='list'),
    path('task/<int:pk>/',TaskREtiveDelete.as_view(),name='update-del-re'),
]