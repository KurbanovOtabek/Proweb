from django.urls import path
from main.views import (TaskListView, TaskDetailView, TaskPostView, TaskUpdateView,
                        TaskDeleteView, CommentListView, CommentCreateView)


urlpatterns = [
    path('all/', TaskListView.as_view()),
    path('detail/<int:pk>/', TaskDetailView.as_view()),
    path('create/', TaskPostView.as_view()),
    path('update/<int:pk>', TaskUpdateView.as_view()),
    path('delete/<int:pk>/', TaskDeleteView.as_view()),
    path('comment/<int:task_id>/', CommentListView.as_view(), name='task_comments'),
    path('comment/<int:task_id>/add/', CommentCreateView.as_view(), name='add_comment'),
]
