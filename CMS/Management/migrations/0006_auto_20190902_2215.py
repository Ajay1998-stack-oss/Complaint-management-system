# Generated by Django 2.2.4 on 2019-09-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0005_user_u_password1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='c_detail',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='c_fulladdress',
            field=models.CharField(max_length=100),
        ),
    ]
