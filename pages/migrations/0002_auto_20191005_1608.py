# Generated by Django 2.1.5 on 2019-10-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_update',
            field=models.DateField(auto_now_add=True),
        ),
    ]
