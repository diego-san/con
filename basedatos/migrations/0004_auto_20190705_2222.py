# Generated by Django 2.2.2 on 2019-07-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0003_auto_20190628_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bienesyservicios',
            name='imgc',
            field=models.ImageField(default=None, upload_to='bysimg'),
        ),
    ]