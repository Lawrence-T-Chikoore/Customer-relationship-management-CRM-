# Generated by Django 3.1.4 on 2022-02-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0002_auto_20220129_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='age',
            field=models.IntegerField(default=100),
        ),
    ]
