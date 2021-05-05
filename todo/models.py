from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=True)

    def __str__(self):
        return self.name

