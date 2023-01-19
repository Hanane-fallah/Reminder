from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Task(models.Model):
    TASK_CAT = [
        ('per', 'personal'),
        ('edu', 'education'),
        ('spo', 'sport'),
        ('buy', 'to buy')
    ]
    TASK_PRI = [
        ('ur', 'urgent'),
        ('im', 'important'),
        ('la', 'do later')
    ]
    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=3, choices=TASK_CAT)
    priority = models.CharField(max_length=2, choices=TASK_PRI)
    due_date = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True, unique=True)

    class META:
        ordering = ['due_date']

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f'{self.title} : {self.done}'
