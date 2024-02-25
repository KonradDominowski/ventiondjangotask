from django.contrib.auth.models import User

from ..models import Category, Task


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
    def create_two_tasks(category: Category):
        task_1 = Task.objects.create(title='Test task 1',
                                     description="Test task description 1",
                                     category=category,
                                     order=2)
        task_2 = Task.objects.create(title='Test task 2',
                                     description="Test task description 2",
                                     category=category,
                                     order=1)

        return task_1, task_2

    @staticmethod
    def create_user():
        user = User.objects.create_user(username='testuser',
                                        email='test@test.test',
                                        password='testpassword'
                                        )
        return user
