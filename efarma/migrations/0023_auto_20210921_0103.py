# Generated by Django 3.1.7 on 2021-09-20 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('efarma', '0022_auto_20210921_0101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='link_id',
            new_name='link',
        ),
    ]
