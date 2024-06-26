# Generated by Django 5.0.2 on 2024-03-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_estudiante_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte',
            old_name='a_bajas',
            new_name='bajas_aprobadas',
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='a_continuidad',
            new_name='continuidad_aprobados',
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='a_licencias',
            new_name='licencias_aprobadas',
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='a_traslados',
            new_name='traslados_aprobados',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='anno',
        ),
        migrations.RemoveField(
            model_name='reporte',
            name='mes',
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='tipo',
            field=models.CharField(blank=0, choices=[('Baja', 'Baja'), ('Continuidad de Estudios', 'Continuidad de Estudios'), ('Licencia', 'Licencia'), ('Traslado', 'Traslado')], default='Baja', max_length=255, null=0),
        ),
    ]
