from django.db import models

class Tematica(models.Model):
    nombre = models.CharField(max_length=200)

class Catering(models.Model):
    nombre = models.CharField(max_length=200)


class Boda(models.Model):
    tematica = models.ForeignKey('Tematica')
    catering = models.ForeignKey('Catering')
    invitados = models.CharField(max_length=200)
    precio = models.CharField(max_length=200)

class Productos(models.Model):
    tipo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
