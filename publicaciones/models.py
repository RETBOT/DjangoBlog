# publicaciones/models.py
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Publicacion(models.Model):
  titulo = models.CharField(max_length=200)
  cuerpo = models.TextField()
  imagen = models.ImageField(upload_to="img_pub", null=True)
  autor = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

  def __str__(self):
    return self.titulo

  def get_absolute_url(self):
        return reverse('detalle_publicacion',args=[str(self.id)])
