# Generated by Django 2.1 on 2018-11-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20181101_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paid_userinfo',
            name='referralCode',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paid_userinfo',
            name='referralName',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
