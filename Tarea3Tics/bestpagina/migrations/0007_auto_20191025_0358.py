# Generated by Django 2.2.4 on 2019-10-25 03:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bestpagina', '0006_auto_20191025_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reseña',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]