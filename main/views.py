from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.authentication import JWTAuthentication

from main.models import Task, Comment
from main.permissions import IsAuthor
from main.serializers import TaskSerializer, CommentSerializer


class TaskPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"
    max_page_size = 1000000

    def get_paginated_response(self, data):
        return Response({
            "links": {
                "next": self.get_next_link(),
                "previous": self.get_previous_link()
            },
            "count": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "results": data
        })


class TaskListView(generics.ListAPIView):
    """" Вывод всех задач автора """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthor, IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status', 'due_date')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).select_related('user')


class TaskDetailView(generics.RetrieveAPIView):
    """" Посмотреть одну задачу по id """
    serializer_class = TaskSerializer
    queryset = Task.objects.all().select_related('user')
    permission_classes = [IsAuthor, ]


class TaskPostView(generics.CreateAPIView):
    """" Добавить новую задачу """
    serializer_class = TaskSerializer
    queryset = Task.objects.all().select_related('user')
    permission_classes = [IsAuthor, ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateView(generics.UpdateAPIView):
    """" Обновить(изменить) задачу по id """
    serializer_class = TaskSerializer
    queryset = Task.objects.all().select_related('user')
    permission_classes = [IsAuthor, ]


class TaskDeleteView(generics.DestroyAPIView):
    """" Удалить задачу по id """
    serializer_class = TaskSerializer
    queryset = Task.objects.all().select_related('user')
    permission_classes = [IsAuthor, ]


class CommentListView(generics.ListAPIView):
    """Вывод всех комментариев к задаче"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor, ]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        return Comment.objects.filter(task_id=task_id).select_related('user', 'task')


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария к задаче"""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthor]

    def perform_create(self, serializer):
        task_id = self.kwargs['task_id']
        serializer.save(user=self.request.user, task_id=task_id)
