# Generated by Django 3.2.21 on 2023-10-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]