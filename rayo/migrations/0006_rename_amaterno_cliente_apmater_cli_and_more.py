# Generated by Django 4.1.2 on 2023-07-06 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rayo', '0005_rename_apmater_cli_cliente_amaterno_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='aMaterno',
            new_name='apmater_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='aPaterno',
            new_name='appater_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='contrasena',
            new_name='contrasena_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='direccion',
            new_name='direccion_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='email',
            new_name='email_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='telefono',
            new_name='fono_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='nombre',
            new_name='nom_cli',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='rut',
            new_name='rut_cli',
        ),
    ]
