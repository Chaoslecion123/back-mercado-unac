# Generated by Django 2.0.9 on 2020-08-12 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0004_auto_20200811_0555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='marketpassrequest',
            old_name='counter',
            new_name='counter_market',
        ),
    ]
