# Generated by Django 3.0.5 on 2020-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0007_auto_20200714_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='product'),
        ),
    ]
