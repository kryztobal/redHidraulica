# Generated by Django 2.1.2 on 2018-10-28 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_auto_20181028_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservorio',
            name='x_position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reservorio',
            name='y_position',
            field=models.IntegerField(default=0),
        ),
    ]
