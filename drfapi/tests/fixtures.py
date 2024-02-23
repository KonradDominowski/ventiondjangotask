from django.contrib.auth.models import User

from ..models import Category, Chapter, Task


class Fixtures:
    @staticmethod
    def create_two_categories():
        category_2 = Category.objects.create(title='Test category 2',
                                             logo_url='https://picsum.photos/200',
                                             description='Test long description 2',
                                             order=2,
                                             )
        category_1 = Category.objects.create(title='Test category 1',
                                             logo_url='https://picsum.photos/200/300',
                                             description='Test long description 1',
                                             order=1,
                                             )

        return category_1, category_2

    # @staticmethod
    # def create_two_chapters(topic: Category):
    #     chapter_1 = Chapter.objects.create(title='Test chapter 1',
    #                                        topic=topic,
    #                                        order=2)
    #     chapter_2 = Chapter.objects.create(title='Test chapter 1',
    #                                        topic=topic,
    #                                        order=1)
    #
    #     return chapter_1, chapter_2
    #
    # @staticmethod
    # def create_two_tasks(chapter: Chapter):
    #     task_1 = Task.objects.create(title='Test task 1',
    #                                  description="Test task description 1",
    #                                  chapter=chapter,
    #                                  order=2)
    #     task_2 = Task.objects.create(title='Test task 2',
    #                                  description="Test task description 2",
    #                                  chapter=chapter,
    #                                  order=1)
    #
    #     return task_1, task_2
    #
    # @staticmethod
    # def create_two_users():
    #     user_1 = User.objects.create_user(username='test_user_1',
    #                                       email='test@test.com',
    #                                       password='test onion')
    #     user_2 = User.objects.create_user(username='test_user_2',
    #                                       email='test@test.com',
    #                                       password='test onion')
    #
    #     return user_1, user_2
    #
    # @staticmethod
    # def create_topic_description(topic: Topic):
    #     description_1 = TopicDescription.objects.create(topic=topic,
    #                                                     subtitle='Test subtitle')
    #
    #     return description_1
