from django.contrib import admin

from main.models import Task, Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display_links = ("id", "title")
    list_display = ("id", "title", "status", "user")
    list_editable = ("status",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display_links = ("id", "text")
    list_display = ("id", "user", "text")

