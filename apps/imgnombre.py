from django.db import models
from uuid import uuid4
from datetime import date
import os

class NameImg(models.Model):

    def _generar_ruta_imagen(instance, filename):
        # El primer paso es extraer la extension de la imagen del
        # archivo original
        extension = os.path.splitext(filename)[1][1:]

        # Generamos la ruta relativa a MEDIA_ROOT donde almacenar
        # el archivo, se usa el nombre de la clase y la fecha actual.
        directorio_clase = instance.__class__.__name__
        ruta = os.path.join('imagenes', directorio_clase,
            date.today().strftime("%Y/%m"))

        # Generamos el nombre del archivo con un identificador
        # aleatorio, y la extension del archivo original.
        nombre_archivo = '{}.{}'.format(uuid4().hex, extension)

        # Devolvermos la ruta completa
        return os.path.join(ruta, nombre_archivo)

    imagen = models.ImageField(upload_to=_generar_ruta_imagen)

    class Meta:
        abstract = True
