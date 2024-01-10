from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(verbose_name="Data de entrega",null=False, blank=False)
    finished_at = models.DateTimeField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
       if not self.finished_at:
           self.finished_at = datetime.today()
           self.save()
