from django.db import IntegrityError
from django.test import TestCase
from django.utils.text import slugify

from .fixtures import Fixtures
from ..models import Task, Chapter, Category


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


class ChapterTestCase(TestCase):
    def setUp(self):
        self.category_1, self.category_2 = Fixtures.create_two_categories()
        self.chapter_1, self.chapter_2 = Fixtures.create_two_chapters(self.category_1)

    def test_create_chapter(self):
        self.assertEqual(Chapter.objects.count(), 2)

        Chapter.objects.create(title='Test chapter 3',
                               category=self.category_1,
                               order=3)
        self.assertEqual(Chapter.objects.count(), 3)

    def test_chapters_are_ordered_correctly(self):
        Chapter.objects.create(title='Test chapter 6',
                               category=self.category_2,
                               order=2)
        Chapter.objects.create(title='Test chapter 5',
                               category=self.category_2,
                               order=3)
        Chapter.objects.create(title='Test chapter 4',
                               category=self.category_2,
                               order=1)
        Chapter.objects.create(title='Test chapter 3',
                               category=self.category_1,
                               order=3)

        queryset_1 = Chapter.objects.filter(category_id=self.category_1.id)
        self.assertEqual(queryset_1[0].order, 1)
        self.assertEqual(queryset_1[1].order, 2)
        self.assertEqual(queryset_1[2].order, 3)

        queryset_2 = Chapter.objects.filter(category_id=self.category_2.id)
        self.assertEqual(queryset_2[0].order, 1)
        self.assertEqual(queryset_2[1].order, 2)
        self.assertEqual(queryset_2[2].order, 3)

    def test_order_and_category_is_unique(self):
        with self.assertRaises(IntegrityError):
            Chapter.objects.create(title='Test chapter 1',
                                   category=self.category_1,
                                   order=1)

    def test_string_representation(self):
        self.assertEqual(str(self.chapter_1), f'{self.chapter_1.category} - {self.chapter_1.title}')


class TaskTestCase(TestCase):
    def setUp(self):
        self.category_1, self.category_2 = Fixtures.create_two_categories()
        self.chapter_1, self.chapter_2 = Fixtures.create_two_chapters(self.category_1)
        self.task_1, self.task_2 = Fixtures.create_two_tasks(self.chapter_1)

    def test_create_task(self):
        self.assertEqual(Task.objects.count(), 2)

        Task.objects.create(title='Test task',
                            description="Test task description 2",
                            chapter=self.chapter_1,
                            order=3)
        self.assertEqual(Task.objects.count(), 3)

    def test_tasks_are_ordered_correctly(self):
        Task.objects.create(title='Test task',
                            description="Test task description 1",
                            chapter=self.chapter_2,
                            order=2)
        Task.objects.create(title='Test task',
                            description="Test task description 1",
                            chapter=self.chapter_2,
                            order=1)
        Task.objects.create(title='Test task',
                            description="Test task description 2",
                            chapter=self.chapter_1,
                            order=3)

        tasks = Task.objects.filter(chapter__category=self.category_1)
        tasks_in_chapter_1 = tasks.filter(chapter=self.chapter_1)
        tasks_in_chapter_2 = tasks.filter(chapter=self.chapter_2)

        self.assertEqual(tasks_in_chapter_1[0].order, 1)
        self.assertEqual(tasks_in_chapter_1[1].order, 2)
        self.assertEqual(tasks_in_chapter_1[2].order, 3)

        self.assertEqual(tasks_in_chapter_2[0].order, 1)
        self.assertEqual(tasks_in_chapter_2[1].order, 2)

    def test_chapter_task_order_is_unique(self):
        with self.assertRaises(IntegrityError):
            Task.objects.create(title='Test task',
                                description="Test task description 2",
                                chapter=self.chapter_1,
                                order=1)

    def test_string_representation(self):
        self.assertEqual(str(self.task_1), f'{self.task_1.chapter} - {self.task_1.title}')
