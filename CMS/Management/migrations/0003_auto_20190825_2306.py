# Generated by Django 2.2.4 on 2019-08-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_auto_20190825_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='c_photo1',
            field=models.CharField(default=500, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='complaint',
            name='c_photo2',
            field=models.CharField(default=500, max_length=500),
            preserve_default=False,
        ),
    ]
