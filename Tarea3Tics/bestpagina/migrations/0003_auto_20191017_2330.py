# Generated by Django 2.2.4 on 2019-10-17 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestpagina', '0002_auto_20191017_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='stock',
            field=models.IntegerField(),
        ),
    ]