# Generated by Django 3.0.1 on 2019-12-29 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={},
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='NULL', max_length=250, unique=True),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='project',
            table=None,
        ),
    ]
