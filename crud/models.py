# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Contacto(models.Model):
    id_contacto = models.BigIntegerField(db_column='id_contacto', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100)  # Field name made lowercase.
    movil = models.CharField(db_column='Movil', max_length=15)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=200)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', max_length=20)  # Field name made lowercase.
    Titulo = models.CharField(db_column='Titulo', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'contacto'

class Usuarios(AbstractUser):
    TIPO_USUARIOS_OPTIONS = (
        ("Administrador", "Administrador"),
        ("Supervisor", "Supervisor"),
        ("Invitado", "Invitado"),
    )
    CARGO_OPTIONS = [
        ('Subgerente', 'Subgerente'),
        ('Director', 'Director'),
        ('Coordinador', 'Coordinador'),
        ('Líder', 'Líder'),
        ('Asesor', 'Asesor'),
        ('Técnico', 'Técnico'),
    ]
    foto = models.ImageField(verbose_name="foto", upload_to="images", blank=False,  default=None)
    #cedula = models.BigIntegerField(db_column='Cedula', primary_key=True)  # Field name made lowercase.
    cedula = models.AutoField(db_column='Cedula', primary_key=True)
    #nombre = models.CharField(db_column='Nombre', max_length=100)  # Field name made lowercase.
    #Seudonimo = models.CharField(db_column='Seudonimo', max_length=20)  # Field name made lowercase.
    #apellidos = models.CharField(db_column='Apellidos', max_length=100)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=50, choices=CARGO_OPTIONS)  # Field name made lowercase.
    tipo_usuario = models.CharField(db_column='Tipo_usuario', max_length=13, choices=TIPO_USUARIOS_OPTIONS)
    # password = models.CharField(db_column='password', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'usuarios'

    def __str__(self):
        return self.first_name + f"({self.cedula})"


class Medidas(models.Model):


    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    logn_vigas_logn = models.FloatField(db_column='logn_vigas_logn')  # Field name made lowercase.
    altura_vigas_logn = models.FloatField(db_column='altura_vigas_logn')  # Field name made lowercase.
    ancho_vigas_logn = models.FloatField(db_column='ancho_vigas_logn')  # Field name made lowercase.
    long_vigas_trans = models.FloatField(db_column='long_vigas_trans')  # Field name made lowercase.
    altura_vigas_trans = models.FloatField(db_column='altura_vigas_trans')  # Field name made lowercase.
    ancho_vigas_trans = models.FloatField(db_column='ancho_vigas_trans')  # Field name made lowercase.
    altura_zapatas_viga_long = models.FloatField(db_column='altura_zapatas_viga_long')  # Field name made lowercase.
    long_puntos_apoyo = models.FloatField(db_column='long_puntos_apoyo')  # Field name made lowercase.
    altura_zapatas = models.FloatField(db_column='altura_zapatas')  # Field name made lowercase.
    ancho_zapatas = models.FloatField(db_column='ancho_zapatas')  # Field name made lowercase.
    largo_zapatas = models.FloatField(db_column='largo_zapatas')  # Field name made lowercase.
    distancia_zapatas = models.FloatField(db_column='distancia_zapatas')  # Field name made lowercase.
    altura_obra_civil = models.FloatField(db_column='altura_obra_civil')  # Field name made lowercase.
    #id_contacto = models.ForeignKey('Contacto', models.DO_NOTHING, db_column='id_contacto')

    class Meta:
        managed = True
        db_table = 'medidas'


class Tecnologias(models.Model):

    TIPOS_TECNOLOGIAS_OPTIONS = (
        ("Digital", "Digital"),
        ("Analoga", "Analoga"),
        ("Hidraulica", "Hidraulica"),
        ("Hibrida", "Hibrida"),
        ("Indicador_marca_modelo_instalado", "Indicador_marca-modelo_instalado"),

    )
    id_tecnologia = models.IntegerField(db_column='id_tecnologia', primary_key=True)
    tipo_tecnologica = models.CharField(db_column='tipo_tecnologia', max_length=32, choices=TIPOS_TECNOLOGIAS_OPTIONS)
    descripcion = models.CharField(db_column='descripcion', max_length=100)

    class Meta:
        managed = True
        db_table = 'tecnologias'

class Obras_civiles(models.Model):

    TIPOS_OBRAS_OPTIONS = (
        ("Sobre_piso", "Sobre_piso"),
        ("Foso", "Foso"),
        ("Semi foso", "Semi foso"),
        ("Otra", "Otra"),

    )

    id_obra = models.BigIntegerField(db_column='obras_civicles', primary_key=True)
    tipo_obra = models.CharField(db_column='tipo_obra', max_length=13, choices=TIPOS_OBRAS_OPTIONS)
    descripcion = models.CharField(db_column='descripcion', max_length=200)

    class Meta:
        managed = True
        db_table = 'obras_civiles'


class Planos(models.Model):

    id_plano = models.CharField(db_column='id_plano', max_length=6, primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=100)
    plano = models.CharField(db_column='plano', max_length=200)
    descripcion = models.CharField(db_column='descripcion', max_length=200)

    class Meta:
        managed = True
        db_table = 'planos'


class Basculas(models.Model):

    TIPOS_BASCULAS_OPTIONS = (
        ("Camionera_metalica", "Camionera_metalica"),
        ("Foso", "Foso"),
        ("Semi_foso", "Semi_foso"),
        ("Otra", "Otra"),

    )
    MARCA_OPTIONS = [
        ('Cardinal', 'Cardinal'),
        ('Autopeso', 'Autopeso'),
    ]
    LONGITUD_BASCULAS_OPTIONS = [
        ('6_metros', '6_metros'),
        ('12_metros', '12_metros'),
        ('18_metros', '18_metros'),
        ('7_metros', '7_metros'),
        ('14_metros', '14_metros'),
        ('21_metros', '21_metros'),
        ('Especiales', 'Especiales'),
        ('Otro', 'Otro'),
        ('Registro_Fotografico', 'Registro_Fotografico'),
    ]
    CARACTERISTICAS_BASCULAS_OPTIONS = [
        ('Capacidad', 'Capacidad'),
        ('Vehiculos_diarios', 'Vehiculos_diarios'),
        ('Tipos_vehiculos', 'Tipos_vehiculos'),
        ('Marca_y_Modelo', 'Marca_y_Modelo'),
    ]

    cod_bascula = models.CharField(db_column='cod_bascula', max_length=6, primary_key=True) #como generas el valor del codigo? como asi bro con migracion
    descripcion = models.CharField(db_column='descripcion', max_length=100)
    tipos_basculas = models.CharField(db_column='tipos_basculas', max_length=50, choices=TIPOS_BASCULAS_OPTIONS)
    longitud = models.IntegerField(db_column="longitud")
    marca = models.CharField(db_column='marca', max_length=50, choices=MARCA_OPTIONS)
    id_plano = models.ForeignKey(Planos, models.DO_NOTHING, db_column='id_plano')
    id_tecnologia = models.ForeignKey(Tecnologias, models.DO_NOTHING, db_column='id_tecnologia')
    longitud_basculas = models.CharField(db_column='longitud_basculas', max_length=100, choices=LONGITUD_BASCULAS_OPTIONS)
    caracteristicas_basculas = models.CharField(db_column='caracteristicas_basculas', max_length=50, choices=CARACTERISTICAS_BASCULAS_OPTIONS)



    class Meta:
        managed = True
        db_table = 'basculas'


class Industrias(models.Model):

    TIPOS_INDUSTRIA_OPTIONS = (
        ("Alimentos", "Alimentos"),
        ("Alimentos_procesados", "Alimentos_procesados"),
        ("Quimico_y_Farmaceutico", "Quimico_y_Farmaceutico"),
        ("Salud", "Salud"),
        ("Sector_publico", "Sector_publico"),
        ("Metalmecanico_y_Manufactura", "Sector_Publico"),
        ("Pesaje_y_Metrologia", "Pesaje_y_Metrologia"),
        ("logisitca_y_Transporte", "logisitca_y_Transporte"),
        ("Servicios", "Servicios"),
        ("Ambiental", "Ambiental"),

    )

    cod_industria = models.IntegerField(db_column='cod_industria', primary_key=True)
    tipo_industria = models.CharField(db_column='tipo_industria', max_length=50, choices=TIPOS_INDUSTRIA_OPTIONS)
    detalles_industria = models.CharField(db_column='detalles_industria', max_length=100)


    class Meta:
        managed = True
        db_table = 'industrias'


class Ubicaciones(models.Model):

    cod_ubicacion = models.IntegerField(db_column='cod_ubicacion', primary_key=True)
    departamentos = models.CharField(db_column='departamentos', max_length=150)
    municipio = models.CharField(db_column='municipio', max_length=200)


    class Meta:
        managed = True
        db_table = 'ubicaciones'


class Empresas(models.Model):
    nit = models.BigIntegerField(db_column='nit', primary_key=True)
    razon_social = models.CharField(db_column='razon_social', max_length=100)
    direccion = models.CharField(db_column='direccion', max_length=100)
    barrio = models.CharField(db_column='barrio', max_length=100)
    telefono = models.CharField(db_column='telefono', max_length=12)
    geolocalizacion = models.CharField(db_column='geolocalizacion', max_length=50)
    cod_industria = models.ForeignKey(Industrias, models.DO_NOTHING, db_column='cod_industria')
    id_contacto = models.ForeignKey(Contacto, models.DO_NOTHING, db_column='id_contacto')
    cod_ubicacion = models.ForeignKey(Ubicaciones, models.DO_NOTHING, db_column='cod_ubicacion')

    class Meta:
        managed = True
        db_table = 'empresas'


class Indicadores(models.Model):

    TIPOS_INDICADORES_OPTIONS = (
        ("Digital_Cardinal225", "Digital_Cardinal225"),
        ("Digital_Cardinal825", "Digital_Cardinal825"),
        ("Analoga_Cardinal205", "Analoga_Cardinal205"),
        ("Analoga_Cardinal210", "Analoga_Cardinal210"),
        ("Analoga_Cardinal225", "Analoga_Cardinal225"),
        ("Analoga_Cardinal825", "Analoga_Cardinal825"),
        ("Hidraulica_Cardinal210", "Hidraulica_Cardinal210"),
        ("Hidraulica_Cardinal225", "Hidraulica_Cardinal225"),
        ("Hidraulica_Cardinal825", "Hidraulica_Cardinal825"),
        ("Hibrida_Cardinal225", "Hibrida_Cardinal225"),
        ("Hibrida_Cardinal825", "Hibrida_Cardinal825"),

    )

    id_indicador = models.IntegerField(db_column='id_indicador', primary_key=True)
    nombre = models.CharField(db_column='nombre', max_length=100)
    modelo = models.CharField(db_column='modelo', max_length=100)
    tipo_indicador = models.CharField(db_column='tipo_indicador', max_length=22, choices=TIPOS_INDICADORES_OPTIONS)

    class Meta:
        managed = True
        db_table = 'indicadores'


class Opotunidades(models.Model):
    TIPOS_PROYECTOS_OPTIONS = (
        ("Nuevo", "Nuevo"),
        ("Correctivo", "Correctivo"),

    )

    cod_registro = models.CharField(db_column='cod_registro', max_length=8, primary_key=True)
    tipo_proyecto = models.CharField(db_column='tipo_proyecto', max_length=10, choices=TIPOS_PROYECTOS_OPTIONS)
    cod_oportunidad = models.CharField(db_column='cod_oportunidad', max_length=50)
    observaciones = models.CharField(db_column='observaciones', max_length=200)
    cod_bascula = models.ForeignKey(Basculas, models.DO_NOTHING, db_column='cod_bascula')
    id_obra = models.ForeignKey(Obras_civiles, models.DO_NOTHING, db_column='id_obra')
    nit = models.ForeignKey(Empresas, models.DO_NOTHING, db_column='nit')
    id_indicador = models.ForeignKey(Indicadores, models.DO_NOTHING, db_column='id_indicador')
    id_medida = models.ForeignKey(Medidas, models.DO_NOTHING, db_column='id_medida')
    cedula = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='cedula')

    class Meta:
        managed = True
        db_table = 'oportunidades'



class  Registros_fotograficos(models.Model):

    cod_registro = models.ForeignKey(Opotunidades, models.DO_NOTHING, db_column='cod_registro')
    fecha_registro = models.DateTimeField(db_column='fecha_registro')
    imagen = models.ImageField(verbose_name="imagen", upload_to="images")
    descripcion = models.CharField(db_column='descripcion', max_length=200)

    class Meta:
        managed = True
        db_table = 'registros_fotograficos'

class Configuraciones(models.Model):

    codigo = models.CharField(db_column='codigo', max_length=6, primary_key=True)
    tipo = models.CharField(db_column='tipo', max_length=50)
    descripcion = models.CharField(db_column='descripcion', max_length=100)
    estado = models.BinaryField(db_column='estado')
    valor = models.TextField(db_column='valor')


    class Meta:
        managed = True
        db_table = 'configuraciones'









