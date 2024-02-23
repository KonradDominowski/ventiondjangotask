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

        Category.objects.create(title='Test topic 4',
                                logo_url='https://picsum.photos/200',
                                description='Test long description 4',
                                order=4,
                                )
        self.assertEqual(Category.objects.count(), 3)

    def test_topic_gets_slug(self):
        self.assertEqual(self.category_1.slug, slugify(self.category_1.title))

    def test_categories_are_ordered_correctly(self):
        Category.objects.create(title='Test topic 4',
                                logo_url='https://picsum.photos/200',
                                description='Test long description 4',
                                order=4,
                                )
        Category.objects.create(title='Test topic 3',
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
            Category.objects.create(title='Test topic 3',
                                    logo_url='https://picsum.photos/200/300',
                                    description='Test long description 3',
                                    order=1,
                                    )

    def test_string_representation(self):
        self.assertEqual(str(self.category_1), self.category_1.title)
