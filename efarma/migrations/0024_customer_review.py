# Generated by Django 3.1.7 on 2021-09-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efarma', '0023_auto_20210921_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='review',
            field=models.CharField(max_length=500, null='True'),
            preserve_default='True',
        ),
    ]