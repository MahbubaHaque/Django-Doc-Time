# Generated by Django 3.2.12 on 2022-04-09 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220326_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='available',
            field=models.CharField(default='From 4 PM to 10 PM Sum, Mon , Wed, Friday', max_length=255),
        ),
    ]
