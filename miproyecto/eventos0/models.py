from django.db import models

# Create your models here.

class Productos(models.Model):
    Tipo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
      

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
