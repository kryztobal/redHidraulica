# Generated by Django 2.1.2 on 2019-06-17 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0018_datosgeneticos_arraybin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosgeneticos',
            name='nindividuos',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='datosgeneticos',
            name='npoblacion',
            field=models.IntegerField(default=4),
        ),
    ]
