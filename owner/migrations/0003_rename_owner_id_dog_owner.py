# Generated by Django 4.0.1 on 2022-01-11 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_rename_owner_dog_owner_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='owner_id',
            new_name='owner',
        ),
    ]
