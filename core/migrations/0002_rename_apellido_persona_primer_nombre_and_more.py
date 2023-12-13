# Generated by Django 4.2 on 2023-12-12 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='apellido',
            new_name='primer_nombre',
        ),
        migrations.RenameField(
            model_name='persona',
            old_name='nombre',
            new_name='segundo_nombre',
        ),
        migrations.AddField(
            model_name='persona',
            name='primer_apellido',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='segundo_apellido',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipo_identificacion',
            field=models.CharField(max_length=5, null=True),
        ),
    ]