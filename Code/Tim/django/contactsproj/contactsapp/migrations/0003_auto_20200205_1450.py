# Generated by Django 3.0.2 on 2020-02-05 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactsapp', '0002_auto_20200205_1222'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]
