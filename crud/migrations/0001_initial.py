# Generated by Django 3.1.7 on 2021-03-26 02:29

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('foto', models.ImageField(default=None, upload_to='images', verbose_name='foto')),
                ('cedula', models.AutoField(db_column='Cedula', primary_key=True, serialize=False)),
                ('cargo', models.CharField(choices=[('Subgerente', 'Subgerente'), ('Director', 'Director'), ('Coordinador', 'Coordinador'), ('Líder', 'Líder'), ('Asesor', 'Asesor'), ('Técnico', 'Técnico')], db_column='Cargo', max_length=50)),
                ('tipo_usuario', models.CharField(choices=[('Administrador', 'Administrador'), ('Supervisor', 'Supervisor'), ('Invitado', 'Invitado')], db_column='Tipo_usuario', max_length=13)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
                'managed': True,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Basculas',
            fields=[
                ('cod_bascula', models.CharField(db_column='cod_bascula', max_length=6, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=100)),
                ('tipos_basculas', models.CharField(choices=[('Camionera_metalica', 'Camionera_metalica'), ('Foso', 'Foso'), ('Semi_foso', 'Semi_foso'), ('Otra', 'Otra')], db_column='tipos_basculas', max_length=50)),
                ('longitud', models.IntegerField(db_column='longitud')),
                ('marca', models.CharField(choices=[('Cardinal', 'Cardinal'), ('Autopeso', 'Autopeso')], db_column='marca', max_length=50)),
                ('longitud_basculas', models.CharField(choices=[('6_metros', '6_metros'), ('12_metros', '12_metros'), ('18_metros', '18_metros'), ('7_metros', '7_metros'), ('14_metros', '14_metros'), ('21_metros', '21_metros'), ('Especiales', 'Especiales'), ('Otro', 'Otro'), ('Registro_Fotografico', 'Registro_Fotografico')], db_column='longitud_basculas', max_length=100)),
                ('caracteristicas_basculas', models.CharField(choices=[('Capacidad', 'Capacidad'), ('Vehiculos_diarios', 'Vehiculos_diarios'), ('Tipos_vehiculos', 'Tipos_vehiculos'), ('Marca_y_Modelo', 'Marca_y_Modelo')], db_column='caracteristicas_basculas', max_length=50)),
            ],
            options={
                'db_table': 'basculas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Configuraciones',
            fields=[
                ('codigo', models.CharField(db_column='codigo', max_length=6, primary_key=True, serialize=False)),
                ('tipo', models.CharField(db_column='tipo', max_length=50)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=100)),
                ('estado', models.BinaryField(db_column='estado')),
                ('valor', models.TextField(db_column='valor')),
            ],
            options={
                'db_table': 'configuraciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id_contacto', models.BigIntegerField(db_column='id_contacto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='Nombre', max_length=100)),
                ('apellidos', models.CharField(db_column='Apellidos', max_length=100)),
                ('movil', models.CharField(db_column='Movil', max_length=15)),
                ('correo', models.CharField(db_column='Correo', max_length=200)),
                ('telefono', models.CharField(db_column='Telefono', max_length=20)),
                ('Titulo', models.CharField(db_column='Titulo', max_length=100)),
            ],
            options={
                'db_table': 'contacto',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('nit', models.BigIntegerField(db_column='nit', primary_key=True, serialize=False)),
                ('razon_social', models.CharField(db_column='razon_social', max_length=100)),
                ('direccion', models.CharField(db_column='direccion', max_length=100)),
                ('barrio', models.CharField(db_column='barrio', max_length=100)),
                ('telefono', models.CharField(db_column='telefono', max_length=12)),
                ('geolocalizacion', models.CharField(db_column='geolocalizacion', max_length=50)),
            ],
            options={
                'db_table': 'empresas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Indicadores',
            fields=[
                ('id_indicador', models.IntegerField(db_column='id_indicador', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100)),
                ('modelo', models.CharField(db_column='modelo', max_length=100)),
                ('tipo_indicador', models.CharField(choices=[('Digital_Cardinal225', 'Digital_Cardinal225'), ('Digital_Cardinal825', 'Digital_Cardinal825'), ('Analoga_Cardinal205', 'Analoga_Cardinal205'), ('Analoga_Cardinal210', 'Analoga_Cardinal210'), ('Analoga_Cardinal225', 'Analoga_Cardinal225'), ('Analoga_Cardinal825', 'Analoga_Cardinal825'), ('Hidraulica_Cardinal210', 'Hidraulica_Cardinal210'), ('Hidraulica_Cardinal225', 'Hidraulica_Cardinal225'), ('Hidraulica_Cardinal825', 'Hidraulica_Cardinal825'), ('Hibrida_Cardinal225', 'Hibrida_Cardinal225'), ('Hibrida_Cardinal825', 'Hibrida_Cardinal825')], db_column='tipo_indicador', max_length=22)),
            ],
            options={
                'db_table': 'indicadores',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Industrias',
            fields=[
                ('cod_industria', models.IntegerField(db_column='cod_industria', primary_key=True, serialize=False)),
                ('tipo_industria', models.CharField(choices=[('Alimentos', 'Alimentos'), ('Alimentos_procesados', 'Alimentos_procesados'), ('Quimico_y_Farmaceutico', 'Quimico_y_Farmaceutico'), ('Salud', 'Salud'), ('Sector_publico', 'Sector_publico'), ('Metalmecanico_y_Manufactura', 'Sector_Publico'), ('Pesaje_y_Metrologia', 'Pesaje_y_Metrologia'), ('logisitca_y_Transporte', 'logisitca_y_Transporte'), ('Servicios', 'Servicios'), ('Ambiental', 'Ambiental')], db_column='tipo_industria', max_length=50)),
                ('detalles_industria', models.CharField(db_column='detalles_industria', max_length=100)),
            ],
            options={
                'db_table': 'industrias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Medidas',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('logn_vigas_logn', models.FloatField(db_column='logn_vigas_logn')),
                ('altura_vigas_logn', models.FloatField(db_column='altura_vigas_logn')),
                ('ancho_vigas_logn', models.FloatField(db_column='ancho_vigas_logn')),
                ('long_vigas_trans', models.FloatField(db_column='long_vigas_trans')),
                ('altura_vigas_trans', models.FloatField(db_column='altura_vigas_trans')),
                ('ancho_vigas_trans', models.FloatField(db_column='ancho_vigas_trans')),
                ('altura_zapatas_viga_long', models.FloatField(db_column='altura_zapatas_viga_long')),
                ('long_puntos_apoyo', models.FloatField(db_column='long_puntos_apoyo')),
                ('altura_zapatas', models.FloatField(db_column='altura_zapatas')),
                ('ancho_zapatas', models.FloatField(db_column='ancho_zapatas')),
                ('largo_zapatas', models.FloatField(db_column='largo_zapatas')),
                ('distancia_zapatas', models.FloatField(db_column='distancia_zapatas')),
                ('altura_obra_civil', models.FloatField(db_column='altura_obra_civil')),
            ],
            options={
                'db_table': 'medidas',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Obras_civiles',
            fields=[
                ('id_obra', models.BigIntegerField(db_column='obras_civicles', primary_key=True, serialize=False)),
                ('tipo_obra', models.CharField(choices=[('Sobre_piso', 'Sobre_piso'), ('Foso', 'Foso'), ('Semi foso', 'Semi foso'), ('Otra', 'Otra')], db_column='tipo_obra', max_length=13)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=200)),
            ],
            options={
                'db_table': 'obras_civiles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Opotunidades',
            fields=[
                ('cod_registro', models.CharField(db_column='cod_registro', max_length=8, primary_key=True, serialize=False)),
                ('tipo_proyecto', models.CharField(choices=[('Nuevo', 'Nuevo'), ('Correctivo', 'Correctivo')], db_column='tipo_proyecto', max_length=10)),
                ('cod_oportunidad', models.CharField(db_column='cod_oportunidad', max_length=50)),
                ('observaciones', models.CharField(db_column='observaciones', max_length=200)),
                ('cedula', models.ForeignKey(db_column='cedula', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('cod_bascula', models.ForeignKey(db_column='cod_bascula', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.basculas')),
                ('id_indicador', models.ForeignKey(db_column='id_indicador', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.indicadores')),
                ('id_medida', models.ForeignKey(db_column='id_medida', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.medidas')),
                ('id_obra', models.ForeignKey(db_column='id_obra', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.obras_civiles')),
                ('nit', models.ForeignKey(db_column='nit', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.empresas')),
            ],
            options={
                'db_table': 'oportunidades',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id_plano', models.CharField(db_column='id_plano', max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='nombre', max_length=100)),
                ('plano', models.CharField(db_column='plano', max_length=200)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=200)),
            ],
            options={
                'db_table': 'planos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tecnologias',
            fields=[
                ('id_tecnologia', models.IntegerField(db_column='id_tecnologia', primary_key=True, serialize=False)),
                ('tipo_tecnologica', models.CharField(choices=[('Digital', 'Digital'), ('Analoga', 'Analoga'), ('Hidraulica', 'Hidraulica'), ('Hibrida', 'Hibrida'), ('Indicador_marca_modelo_instalado', 'Indicador_marca-modelo_instalado')], db_column='tipo_tecnologia', max_length=32)),
                ('descripcion', models.CharField(db_column='descripcion', max_length=100)),
            ],
            options={
                'db_table': 'tecnologias',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ubicaciones',
            fields=[
                ('cod_ubicacion', models.IntegerField(db_column='cod_ubicacion', primary_key=True, serialize=False)),
                ('departamentos', models.CharField(db_column='departamentos', max_length=150)),
                ('municipio', models.CharField(db_column='municipio', max_length=200)),
            ],
            options={
                'db_table': 'ubicaciones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Registros_fotograficos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(db_column='fecha_registro')),
                ('imagen', models.ImageField(upload_to='images', verbose_name='imagen')),
                ('descripcion', models.CharField(db_column='descripcion', max_length=200)),
                ('cod_registro', models.ForeignKey(db_column='cod_registro', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.opotunidades')),
            ],
            options={
                'db_table': 'registros_fotograficos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='empresas',
            name='cod_industria',
            field=models.ForeignKey(db_column='cod_industria', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.industrias'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='cod_ubicacion',
            field=models.ForeignKey(db_column='cod_ubicacion', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.ubicaciones'),
        ),
        migrations.AddField(
            model_name='empresas',
            name='id_contacto',
            field=models.ForeignKey(db_column='id_contacto', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.contacto'),
        ),
        migrations.AddField(
            model_name='basculas',
            name='id_plano',
            field=models.ForeignKey(db_column='id_plano', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.planos'),
        ),
        migrations.AddField(
            model_name='basculas',
            name='id_tecnologia',
            field=models.ForeignKey(db_column='id_tecnologia', on_delete=django.db.models.deletion.DO_NOTHING, to='crud.tecnologias'),
        ),
    ]
