# Generated by Django 2.2.4 on 2019-10-18 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bestpagina', '0003_auto_20191017_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.CharField(default='', max_length=140),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='static/imagenes'),
        ),
    ]
