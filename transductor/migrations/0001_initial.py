# Generated by Django 2.1.5 on 2019-01-23 14:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transductor_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyTransductor',
            fields=[
                ('serial_number', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('ip_address', models.CharField(default='0.0.0.0', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_ip_address', message='Incorrect IP address format', regex='^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$')])),
                ('broken', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='transductor_model.TransductorModel')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
