from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drfapi.views import CategoryViewSet, ChapterViewSet, TaskViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('chapters', ChapterViewSet, basename='chapters')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
