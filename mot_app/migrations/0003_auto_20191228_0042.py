# Generated by Django 3.0.1 on 2019-12-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mot_app', '0002_auto_20191228_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='millage',
            field=models.BigIntegerField(),
        ),
    ]