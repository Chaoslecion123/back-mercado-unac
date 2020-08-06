# Generated by Django 2.0.9 on 2020-08-01 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'provincia',
                'verbose_name_plural': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='CityArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=256)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_areas', related_query_name='city_area', to='world.City')),
            ],
            options={
                'verbose_name': 'distrito',
                'verbose_name_plural': 'distritos',
            },
        ),
        migrations.CreateModel(
            name='CountryArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', related_query_name='city', to='world.CountryArea'),
        ),
    ]
