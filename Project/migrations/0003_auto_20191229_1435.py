# Generated by Django 3.0.1 on 2019-12-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_auto_20191229_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=250),
        ),
    ]
