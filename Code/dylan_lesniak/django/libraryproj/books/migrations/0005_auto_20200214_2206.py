# Generated by Django 3.0.2 on 2020-02-14 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200214_2206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
