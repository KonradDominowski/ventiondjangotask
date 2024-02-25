from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate

from .fixtures import Fixtures
from ..models import Category, Task
from ..views import CategoryViewSet, TaskViewSet


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = '/categories/'
        self.factory = APIRequestFactory()
        self.user = Fixtures.create_user()
        self.category_1, self.category_2 = Fixtures.create_two_categories()

    def test_url(self):
        self.assertEqual(reverse('categories-list'), self.url)

    def test_get_categories_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_category(self):
        view = CategoryViewSet.as_view(actions={'get': 'retrieve'})
        request = self.factory.get(self.url)
        response = view(request, pk=self.category_1.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.category_1.pk)

    def test_post_category_unauthenticated_is_forbidden(self):
        response = self.client.post(self.url, {
            "name": "Test category",
            "slug": "",
            "logo_url": "https://test.com",
            "description": "This is a test description",
            "order": 3,
        })

        self.assertEqual(response.status_code, 403)

    def test_post_category_authenticated(self):
        view = CategoryViewSet.as_view(actions={'post': 'create'})

        request = self.factory.post(self.url, {
            "name": "Test category",
            "slug": "",
            "logo_url": "https://test.com",
            "description": "This is a test description",
            "order": 3,
        })

        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 201)

    def test_put_category_unauthenticated_is_forbidden(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, 403)

    def test_put_category(self):
        view = CategoryViewSet.as_view(actions={'put': 'update'})

        request = self.factory.put(self.url, {
            "name": "New name",
            "slug": "",
            "logo_url": "https://newurl.com",
            "description": "This is a new description",
            "order": 4,
        })

        force_authenticate(request, user=self.user)
        response = view(request, pk=self.category_1.pk)
        self.category_1.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.category_1.name, "New name")
        self.assertEqual(self.category_1.logo_url, "https://newurl.com")
        self.assertEqual(self.category_1.description, "This is a new description")
        self.assertEqual(self.category_1.order, 4)

    def test_delete_category_unauthenticated_is_forbidden(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 403)

    def test_delete_category(self):
        view = CategoryViewSet.as_view(actions={'delete': 'destroy'})
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.category_1.pk)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Category.objects.all()), 1)


class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        self.url = '/tasks/'
        self.factory = APIRequestFactory()
        self.user = Fixtures.create_user()
        self.category_1, self.category_2 = Fixtures.create_two_categories()
        self.task_1, self.task_2 = Fixtures.create_two_tasks(self.category_1)

    def test_url(self):
        self.assertEqual(reverse('tasks-list'), self.url)

    def test_get_tasks_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_get_task(self):
        view = TaskViewSet.as_view(actions={'get': 'retrieve'})
        request = self.factory.get(self.url)
        response = view(request, pk=self.task_1.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.task_1.pk)

    def test_post_task_unauthenticated_is_forbidden(self):
        response = self.client.post(self.url, {
            "id": 1,
            "title": "First task",
            "description": "first task description",
            "completed": False,
            "starter_css_code": "",
            "target": "target",
            "order": 1,
            "category": 1
        })

        self.assertEqual(response.status_code, 403)

    def test_post_task_authenticated(self):
        view = TaskViewSet.as_view(actions={'post': 'create'})

        request = self.factory.post(self.url, {
            "title": "Test task 3",
            "description": "Test task description",
            "completed": False,
            "starter_css_code": "",
            "target": "target",
            "order": 1,
            "category": self.category_2.pk
        })

        force_authenticate(request, user=self.user)
        response = view(request)

        self.assertEqual(response.status_code, 201)

    def test_put_task_unauthenticated_is_forbidden(self):
        response = self.client.put(self.url)
        self.assertEqual(response.status_code, 403)

    def test_put_task(self):
        view = TaskViewSet.as_view(actions={'put': 'update'})

        request = self.factory.put(self.url, {
            "title": "New task updated",
            "description": "New Test task description",
            "completed": True,
            "starter_css_code": "updated code",
            "target": "target",
            "order": 1,
            "category": self.category_2.pk
        })

        force_authenticate(request, user=self.user)
        response = view(request, pk=self.task_1.pk)
        self.task_1.refresh_from_db()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.task_1.title, "New task updated")
        self.assertEqual(self.task_1.description, "New Test task description")
        self.assertEqual(self.task_1.completed, True)
        self.assertEqual(self.task_1.starter_css_code, 'updated code')

    def test_delete_task_unauthenticated_is_forbidden(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 403)

    def test_delete_task(self):
        view = TaskViewSet.as_view(actions={'delete': 'destroy'})
        request = self.factory.delete(self.url)
        force_authenticate(request, user=self.user)
        response = view(request, pk=self.task_1.pk)

        self.assertEqual(response.status_code, 204)
        self.assertEqual(len(Task.objects.all()), 1)
