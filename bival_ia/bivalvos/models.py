# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

def get_upload_path(instance, filename):
    return f'muestras/{instance.codigomuestra}/{filename}'

class Caracteristicasbivalvos(models.Model):
    codigomuestra = models.CharField(db_column='codigoMuestra', primary_key=True, max_length=255)  # Field name made lowercase.
    altura = models.FloatField()
    ancho = models.FloatField()
    espesor = models.FloatField()
    color = models.CharField(max_length=255)
    estructuraconcha = models.CharField(db_column='estructuraConcha', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pesoconcarne = models.FloatField(db_column='pesoConCarne', blank=True, null=True)  # Field name made lowercase.
    pesosincarne = models.FloatField(db_column='pesoSinCarne', blank=True, null=True)  # Field name made lowercase.
    fotodorsal = models.ImageField(upload_to=get_upload_path, db_column='fotoDorsal', max_length=255)  # Field name made lowercase.
    fotolateral = models.ImageField(upload_to=get_upload_path,db_column='fotoLateral', max_length=255)  # Field name made lowercase.
    fotoventral = models.ImageField(upload_to=get_upload_path,db_column='fotoVentral', max_length=255)  # Field name made lowercase.
    fotoanterior = models.ImageField(upload_to=get_upload_path,db_column='fotoAnterior', max_length=255)  # Field name made lowercase.
    fotoposterior = models.ImageField(upload_to=get_upload_path,db_column='fotoPosterior', max_length=255)  # Field name made lowercase.
    idcondicionbivalvo = models.ForeignKey('Condicionesbivalvos', models.DO_NOTHING, db_column='idCondicionBivalvo')  # Field name made lowercase.
    idforma = models.ForeignKey('Formas', models.DO_NOTHING, db_column='idForma')  # Field name made lowercase.
    idvariableambiental = models.ForeignKey('Variablesambientales', models.DO_NOTHING, db_column='idVariableAmbiental')  # Field name made lowercase.
    iduser = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='idUser')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'caracteristicasbivalvos'


class Clases(models.Model):
    nombre = models.CharField(max_length=255)
    idfilo = models.ForeignKey('Filos', models.DO_NOTHING, db_column='idFilo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clases'


class Condicionesbivalvos(models.Model):
    condicion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'condicionesbivalvos'


class Dominios(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dominios'


class Especies(models.Model):
    nombrecientifico = models.CharField(db_column='nombreCientifico', max_length=255)  # Field name made lowercase.
    idgenero = models.ForeignKey('Generos', models.DO_NOTHING, db_column='idGenero')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especies'


class Familias(models.Model):
    nombre = models.CharField(max_length=255)
    idorden = models.ForeignKey('Ordenes', models.DO_NOTHING, db_column='idOrden')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'familias'


class Filos(models.Model):
    nombre = models.CharField(max_length=255)
    idreino = models.ForeignKey('Reinos', models.DO_NOTHING, db_column='idReino')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filos'


class Formas(models.Model):
    forma = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'formas'


class Generos(models.Model):
    nombre = models.CharField(max_length=255)
    idfamilia = models.ForeignKey(Familias, models.DO_NOTHING, db_column='idFamilia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generos'


class Habitats(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'habitats'


class Mareas(models.Model):
    hora = models.TimeField()
    zonalugar = models.CharField(db_column='zonaLugar', max_length=255)  # Field name made lowercase.
    altitudmarea = models.FloatField(db_column='altitudMarea', blank=True, null=True)  # Field name made lowercase.
    observaciones = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mareas'

class Ordenes(models.Model):
    nombre = models.CharField(max_length=255)
    idclase = models.ForeignKey(Clases, models.DO_NOTHING, db_column='idClase')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenes'

class Reinos(models.Model):
    nombre = models.CharField(max_length=255)
    iddominio = models.ForeignKey(Dominios, models.DO_NOTHING, db_column='idDominio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reinos'


class Tiposhabitat(models.Model):
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tiposhabitat'


class Ubicaciones(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    altitud = models.FloatField()
    region = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ubicaciones'


class Variablesambientales(models.Model):
    temperatura = models.FloatField()
    salinidad = models.FloatField()
    ph = models.FloatField()
    oxigeno = models.FloatField()
    idubicacion = models.ForeignKey(Ubicaciones, models.DO_NOTHING, db_column='idUbicacion')  # Field name made lowercase.
    idhabitat = models.ForeignKey(Habitats, models.DO_NOTHING, db_column='idHabitat')  # Field name made lowercase.
    idespecie = models.ForeignKey(Especies, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.
    idmarea = models.ForeignKey(Mareas, models.DO_NOTHING, db_column='idMarea')  # Field name made lowercase.
    idtipohabitat = models.ForeignKey(Tiposhabitat, models.DO_NOTHING, db_column='idTipoHabitat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variablesambientales'

