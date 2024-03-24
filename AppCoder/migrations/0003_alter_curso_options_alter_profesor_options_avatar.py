from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AppCoder', '0002_alter_estudiante_apellido_alter_estudiante_nombre_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['-nombre']},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre', 'apellido'], 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
    ]