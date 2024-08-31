from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def get_default_category():
    default_category, created = Category.objects.get_or_create(name='Default')
    return default_category.pk

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='todos', on_delete=models.CASCADE, default=get_default_category)

    def __str__(self):
        return self.title

