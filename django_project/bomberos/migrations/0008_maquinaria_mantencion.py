# Generated by Django 4.2.4 on 2023-10-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bomberos', '0007_alter_maquinaria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='maquinaria',
            name='mantencion',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]