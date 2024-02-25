from django.core.management.base import BaseCommand
from drfapi.models import Category, Task


class Command(BaseCommand):
    help = 'If the database is empty, it populates it with some basic dummy data'

    def handle(self, *args, **options):
        if Category.objects.filter(name='CSS Basics').count() == 0:
            Category.objects.create(name="CSS Basics",
                                    description="It serves as and introduction to the CSS world",
                                    logo_url='https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg',
                                    order=1)

            Task.objects.create(title="Background",
                                description='''Use CSS rule { background: blue; } to give an element a blue background''',
                                completed=False,
                                starter_css_code='',
                                target="{ background: blue; }",
                                category=Category.objects.get(name='CSS Basics'),
                                order=1)

            Task.objects.create(title="Text color",
                                description='''Use CSS rule { color: red; } to give text a red color''',
                                completed=False,
                                starter_css_code='',
                                target="{ color: red; }",
                                category=Category.objects.get(name='CSS Basics'),
                                order=2)

            Task.objects.create(title="Font size",
                                description='''Use CSS rule { font-size: 20px; } to give text size of 20px''',
                                completed=False,
                                starter_css_code='',
                                target="{ font-size: 20px; }",
                                category=Category.objects.get(name='CSS Basics'),
                                order=3)

            Task.objects.create(title="Text underline",
                                description='''Use CSS rule { text-decoration: underline; } to give text an underline''',
                                completed=False,
                                starter_css_code='',
                                target="{ text-decoration: underline; }",
                                category=Category.objects.get(name='CSS Basics'),
                                order=4)

        if Category.objects.filter(name='Border').count() == 0:
            Category.objects.create(name="Border",
                                    description="Dive into the intricacies of creating borders using CSS",
                                    logo_url='https://www.svgrepo.com/show/437181/rectangle.svg',
                                    order=2)

            Task.objects.create(title="Basic border",
                                description='''Use CSS rule { border: 2px solid black; } to give an element a border''',
                                completed=False,
                                starter_css_code='',
                                target="{ border: 2px solid black; }",
                                category=Category.objects.get(name='Border'),
                                order=1)

            Task.objects.create(title="Border width",
                                description='''Use CSS rule { border-width: 5px; } to give the border thickness of 5px''',
                                completed=False,
                                starter_css_code='',
                                target="{ border-width: 5px; }",
                                category=Category.objects.get(name='Border'),
                                order=2)

            Task.objects.create(title="Border color",
                                description='''Use CSS rule { border-color: red; } to give the border red color''',
                                completed=False,
                                starter_css_code='',
                                target="{ border-color: red; }",
                                category=Category.objects.get(name='Border'),
                                order=3)

            Task.objects.create(title="Border style",
                                description='''Use CSS rule { border-style: dotted; } to give make border dotted''',
                                completed=False,
                                starter_css_code='',
                                target="{ border-style: dotted; }",
                                category=Category.objects.get(name='Border'),
                                order=4)

        print("Filled database with dummy data.")
