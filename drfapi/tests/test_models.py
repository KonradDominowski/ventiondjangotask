from django.db import IntegrityError
from django.test import TestCase
from django.utils.text import slugify

from .fixtures import Fixtures
from ..models import Task, Category


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category_1, self.category_2 = Fixtures.create_two_categories()

    def test_create_category(self):
        self.assertEqual(Category.objects.count(), 2)

        Category.objects.create(name='Test category 4',
                                logo_url='https://picsum.photos/200',
                                description='Test long description 4',
                                order=4,
                                )
        self.assertEqual(Category.objects.count(), 3)

    def test_category_gets_slug(self):
        self.assertEqual(self.category_1.slug, slugify(self.category_1.name))

    def test_categories_are_ordered_correctly(self):
        Category.objects.create(name='Test category 4',
                                logo_url='https://picsum.photos/200',
                                description='Test long description 4',
                                order=4,
                                )
        Category.objects.create(name='Test category 3',
                                logo_url='https://picsum.photos/200',
                                description='Test long description 3',
                                order=3,
                                )

        queryset = Category.objects.all()

        self.assertEqual(queryset[0].order, 1)
        self.assertEqual(queryset[1].order, 2)
        self.assertEqual(queryset[2].order, 3)
        self.assertEqual(queryset[3].order, 4)

    def test_order_is_unique(self):
        """Test if category order is unique"""
        with self.assertRaises(IntegrityError):
            Category.objects.create(name='Test category 3',
                                    logo_url='https://picsum.photos/200/300',
                                    description='Test long description 3',
                                    order=1,
                                    )

    def test_string_representation(self):
        self.assertEqual(str(self.category_1), self.category_1.name)


class TaskTestCase(TestCase):
    def setUp(self):
        self.category_1, self.category_2 = Fixtures.create_two_categories()
        self.task_1, self.task_2 = Fixtures.create_two_tasks(self.category_1)

    def test_create_task(self):
        self.assertEqual(Task.objects.count(), 2)

        Task.objects.create(title='Test task',
                            description="Test task description 2",
                            category=self.category_1,
                            order=3)
        self.assertEqual(Task.objects.count(), 3)

    def test_tasks_are_ordered_correctly(self):
        Task.objects.create(title='Test task',
                            description="Test task description 1",
                            category=self.category_2,
                            order=2)
        Task.objects.create(title='Test task',
                            description="Test task description 1",
                            category=self.category_2,
                            order=1)
        Task.objects.create(title='Test task',
                            description="Test task description 2",
                            category=self.category_1,
                            order=3)

        tasks_in_category_1 = Task.objects.filter(category=self.category_1)
        tasks_in_category_2 = Task.objects.filter(category=self.category_2)

        self.assertEqual(tasks_in_category_1[0].order, 1)
        self.assertEqual(tasks_in_category_1[1].order, 2)
        self.assertEqual(tasks_in_category_1[2].order, 3)

        self.assertEqual(tasks_in_category_2[0].order, 1)
        self.assertEqual(tasks_in_category_2[1].order, 2)

    def test_category_task_order_is_unique(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(title='Test task',
                                description="Test task description 2",
                                category=self.category_1,
                                order=1)

    def test_string_representation(self):
        self.assertEqual(str(self.task_1), f'{self.task_1.category} - {self.task_1.title}')
