# Generated by Django 2.2.4 on 2019-10-25 02:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bestpagina', '0004_auto_20191018_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='producto',
            new_name='prod',
        ),
        migrations.RemoveField(
            model_name='carrito',
            name='usuario',
        ),
        migrations.AddField(
            model_name='carrito',
            name='usua',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]