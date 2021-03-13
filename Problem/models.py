from django.db import models
from ProblemManagement import settings
from django.utils.text import slugify
from time import time

# Create your models here.

def gen_slug(name):
    new_slug = slugify(name, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class Problems(models.Model):

    Easy = 'Easy'
    Medium = 'Medium'
    Hard = 'Hard'
    NA = 'NA'
    DIFFICULTY = [
        (NA, 'NA'),
        (Easy, 'Easy'),
        (Medium, 'Medium'),
        (Hard, 'Hard'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='problems', on_delete=models.CASCADE)
    name_problem = models.CharField('Назва проблеми', max_length=150)
    slug = models.SlugField('Слаг', max_length=150, blank=True, unique=True)
    url_problem = models.CharField('Силка проблеми на Leetcode', max_length=150)
    number_solved = models.IntegerField('Кількість вирішень')
    difficulty = models.CharField('Складність', max_length=150, choices=DIFFICULTY, default=NA)
    reject = models.IntegerField('Кількість невдач')
    published = models.DateTimeField('Дата публікації', auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.name_problem)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_problem

    class Meta:
        ordering = ['published']
        verbose_name = "Проблема"
        verbose_name_plural = "Проблеми"

class Notate(models.Model):

    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    notate = models.TextField()

    def __str__(self):
        return f'{self.problem.name_problem}'

    class Meta:
        verbose_name = "Нотатка"
        verbose_name_plural = "Нотатки"