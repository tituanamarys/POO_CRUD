from distutils.command import upload
from pickle import TRUE
from django.db import models

# Create your models here.
class Tasks(models.Model):
    name=models.CharField(max_length=50,verbose_name='Nombre');
    description=models.TextField(blank=True,verbose_name='Descripcion');
    imagen=models.ImageField(upload_to='images/',null=True,verbose_name='Imagen');

    def __str__(self):
        fila="Nombre: "+ self.name + "-" + "Descripcion: "+ self.description
        return fila
    def delete(self, using=None, keep_parents=False) :
        self.imagen.storage.delete(self.imagen.name)
        return super().delete()

    