# Generated by Django 3.0.5 on 2020-07-14 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0005_producto_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]
