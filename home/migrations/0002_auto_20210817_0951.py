# Generated by Django 3.2.6 on 2021-08-17 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teammates',
            old_name='Desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='teammates',
            old_name='Logo',
            new_name='logo',
        ),
    ]