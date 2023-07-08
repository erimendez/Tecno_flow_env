from django.db import models

# Create your models here.
class Cotizacion(models.Model):

    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    descrip_falla = models.CharField(max_length=30)
    fecha = models.DateField()


    class Meta:
       db_table= "cotizacion_celu_django"


    def __str__(self):
        return f"El celu {self.marca}, modelo {self.modelo}, falla, {self.descrip_falla}, fecha de ingreso{self.fecha}"   

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]

              ]


