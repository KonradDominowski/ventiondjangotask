from django.contrib.auth.models import User

from ..models import Category, Chapter, Task


class Fixtures:
    @staticmethod
    def create_two_categories():
        category_2 = Category.objects.create(name='Test category 2',
                                             logo_url='https://picsum.photos/200',
                                             description='Test long description 2',
                                             order=2,
                                             )
        category_1 = Category.objects.create(name='Test category 1',
                                             logo_url='https://picsum.photos/200/300',
                                             description='Test long description 1',
                                             order=1,
                                             )

        return category_1, category_2

    @staticmethod
    def create_two_chapters(category: Category):
        chapter_1 = Chapter.objects.create(title='Test chapter 1',
                                           category=category,
                                           order=2)
        chapter_2 = Chapter.objects.create(title='Test chapter 1',
                                           category=category,
                                           order=1)

        return chapter_1, chapter_2

    @staticmethod
    def create_two_tasks(chapter: Chapter):
        task_1 = Task.objects.create(title='Test task 1',
                                     description="Test task description 1",
                                     chapter=chapter,
                                     order=2)
        task_2 = Task.objects.create(title='Test task 2',
                                     description="Test task description 2",
                                     chapter=chapter,
                                     order=1)

        return task_1, task_2
