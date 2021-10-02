# Generated by Django 3.1.7 on 2021-09-20 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('efarma', '0015_auto_20210916_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productImage',
            field=models.ImageField(null='False', upload_to='static/Images/'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerImage', models.ImageField(null='False', upload_to='static/Images/')),
                ('link', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]