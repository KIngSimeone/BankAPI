# Generated by Django 3.1.1 on 2020-09-16 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ewallet', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Balance',
            new_name='Account',
        ),
    ]
