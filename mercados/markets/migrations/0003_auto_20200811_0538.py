# Generated by Django 2.0.9 on 2020-08-11 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
        ('markets', '0002_auto_20200811_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marketpassrequest',
            name='schedule',
        ),
        migrations.AddField(
            model_name='marketpassrequest',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_schedule', related_query_name='users_schedules', to='schedule.Schedule'),
        ),
    ]
