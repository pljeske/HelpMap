# Generated by Django 3.0.6 on 2020-05-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='helppoint',
            name='description',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='helppoint',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]