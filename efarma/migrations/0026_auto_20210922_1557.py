# Generated by Django 3.1.7 on 2021-09-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efarma', '0025_auto_20210922_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customerImage',
            field=models.ImageField(null='False', upload_to='static/Images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='productImage',
            field=models.ImageField(null='False', upload_to='static/Images/'),
        ),
    ]
