# Generated by Django 3.1.7 on 2021-09-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efarma', '0006_auto_20210914_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='proImage',
            field=models.CharField(max_length=500),
        ),
    ]
