from django.contrib import admin
from .models import Task, Category


class TaskAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
