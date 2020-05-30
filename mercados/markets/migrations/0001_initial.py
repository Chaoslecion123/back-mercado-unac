# Generated by Django 2.0.9 on 2020-05-30 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addresses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('name', models.CharField(max_length=50, verbose_name='nombre del mercado')),
                ('aforo', models.IntegerField(default=0, verbose_name='cantidad de personas que un mercado puede soportar')),
                ('count_aforo', models.IntegerField(default=0, verbose_name='contador para control de aforos')),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_addresses', related_query_name='users_address', to='addresses.Address')),
            ],
            options={
                'verbose_name': 'mercado',
                'verbose_name_plural': 'mercados',
            },
        ),
    ]
