# Generated by Django 3.0.5 on 2020-07-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_auto_20200712_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='Nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(max_length=999),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='project'),
        ),
    ]