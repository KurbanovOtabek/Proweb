from django.db import models
from django.contrib.auth import get_user_model

Author = get_user_model()

l = 200

TASK_STATUS = (
    ('pen', 'Pending'),
    ('prog', 'In Progress'),
    ('comp', 'Completed'),
)


class Task(models.Model):
    title = models.CharField(max_length=l, verbose_name="Название задачи", null=True, blank=True)
    description = models.TextField(verbose_name='Описание задачи', null=True, blank=True)
    status = models.CharField(max_length=l, verbose_name='Статус задачи', choices=TASK_STATUS, default='pen',
                              null=True, blank=True)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='task_user',
                             null=True, blank=True)

    class Meta:
        ordering = ["id"]
        db_table = "task"
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.SET_NULL, related_name='comment_user',
                             null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, related_name='comment_task', null=True, blank=True)
    text = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["id"]
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.text

