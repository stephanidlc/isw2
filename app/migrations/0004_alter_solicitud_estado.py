# Generated by Django 5.0.2 on 2024-03-31 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_a_bajas_reporte_bajas_aprobadas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(choices=[('Aprobado', 'Aprobado'), ('Denegado', 'Denegado')], default='pendiente', max_length=50),
        ),
    ]
