# Generated by Django 3.2.6 on 2021-08-17 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210817_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammates',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='teammates',
            name='desc',
            field=models.CharField(max_length=50),
        ),
    ]
