# Generated by Django 3.0.6 on 2020-05-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20200524_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.TextField(max_length=55, unique=True, verbose_name='username'),
        ),
    ]
