# Generated by Django 2.2.2 on 2019-08-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basedatos', '0007_bienesyservicios_umed'),
    ]

    operations = [
        migrations.AddField(
            model_name='bienesyservicios',
            name='cant_u',
            field=models.DecimalField(decimal_places=3, default=2, max_digits=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historial',
            name='titulo',
            field=models.TextField(default=21, max_length=250, verbose_name='Tituo inrgesado'),
            preserve_default=False,
        ),
    ]
