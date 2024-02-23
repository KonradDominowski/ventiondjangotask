from django.db import models
from django.utils.text import slugify


class Task(models.Model):
    title = models.CharField(max_length=64, verbose_name='Task title')
    description = models.TextField(verbose_name='Task description')
    starter_css_code = models.TextField(verbose_name='Starter CSS code', blank=True, null=True)
    target = models.TextField(verbose_name='HTML Target')
    chapter = models.ForeignKey('Chapter', on_delete=models.CASCADE, related_name='tasks')
    order = models.IntegerField(verbose_name='Task order')

    class Meta:
        unique_together = ['chapter', 'order']
        ordering = ['order']

    def __repr__(self):
        return f'{self.chapter} - {self.title}'

    def __str__(self):
        return f'{self.chapter} - {self.title}'


class Chapter(models.Model):
    title = models.CharField(max_length=64, verbose_name='Chapter title')
    topic = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='chapters')
    order = models.IntegerField(verbose_name='Chapter order')

    class Meta:
        unique_together = ['topic', 'order']
        ordering = ['order']

    def __repr__(self):
        return f'{self.topic} - {self.title}'

    def __str__(self):
        return f'{self.topic} - {self.title}'


class Category(models.Model):
    title = models.CharField(max_length=64, verbose_name='Category title')
    slug = models.SlugField(max_length=64, null=False, unique=True)
    logo_url = models.URLField(verbose_name='Logo URL')
    description = models.TextField()
    order = models.IntegerField(verbose_name='Category order', unique=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title
