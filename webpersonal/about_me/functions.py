
from django.db import models

class Apartado(models.Model):
    # Lo que hara  'upload_to' es guardar las imagenes en una carpeta con el nombre
    # del valor que se asigne a 'upload_to' 
    # ¿y si no existe la carpeta? R=Se creara la carpeta
    # ¿y donde estara ubicada dicha carpeta? 
    # R= Dentro del directorio media que fue indicado en el archivo 'settings.py' de 
    # Django a traves de las costantes: 'MEDIA_URL' y 'MEDIA_ROOT' 
    imagenPortada=models.ImageField(verbose_name="Imagen del apartado de portada:",upload_to="fotosApartados")

    def __str__(self):
        return "Apartado con codigo: {}".format(self.id)