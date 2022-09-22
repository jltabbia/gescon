from django.db import models
from usuarios.models import Usuario

# definimos modelo Propietarios
class Propietarios(models.Model):
    id=models.IntegerField(primary_key=True,serialize=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    apellido=models.CharField(max_length=45,verbose_name="Apellido")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio",blank=True,null=True)
    contacto=models.CharField(max_length=15,verbose_name="Tel. de Contacto",blank=True,null=True)
    email=models.EmailField(verbose_name="Correo Electrónico",blank=True,null=True)
    cuit_cuil=models.CharField(max_length=15,blank=False, null=False,verbose_name="CUIT/CUIL")
    
    class Meta:
        db_table='propietarios'

# definimos modelo Edificios
class Edificios(models.Model):
    id=models.IntegerField(primary_key=True,serialize=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre Edificio")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio")
    cantidad_dptos=models.IntegerField()
    administrador=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    
    class Meta:
        db_table='edificios'


# definimos modelo Departamentos
class Departamentos(models.Model):
    id=models.IntegerField(primary_key=True,serialize=True)
    piso=models.IntegerField(verbose_name="Nro. de Piso")
    numero=models.CharField(max_length=2,blank=False, null=False,verbose_name="Nro. Departamento")
    propietario=models.ForeignKey(Propietarios,on_delete=models.CASCADE)
    edificio=models.ForeignKey(Edificios,on_delete=models.CASCADE)
    porcentaje=models.DecimalField(max_digits=5,decimal_places=2,verbose_name="Porcentaje expensas")

    class Meta:
        db_table='departamentos'

