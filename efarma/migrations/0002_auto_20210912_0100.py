# Generated by Django 3.1.7 on 2021-09-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efarma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('proId', models.IntegerField(primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=50)),
                ('proDiscription', models.CharField(max_length=200)),
                ('proImage', models.CharField(max_length=500)),
                ('proCompany', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('proCategory', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
