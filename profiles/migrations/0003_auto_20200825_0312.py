# Generated by Django 3.1 on 2020-08-25 10:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0002_auto_20200825_0246'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profiles',
            new_name='Profile',
        ),
    ]
