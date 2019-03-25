# Generated by Django 2.1.5 on 2019-03-11 17:34

import datetime
import django.contrib.postgres.fields
import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transductor', '0003_auto_20190204_1403'),
        ('measurement', '0005_merge_20190206_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinutelyMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateTimeField(default=datetime.datetime.now)),
                ('frequency_a', models.FloatField(default=0)),
                ('voltage_a', models.FloatField(default=0)),
                ('voltage_b', models.FloatField(default=0)),
                ('voltage_c', models.FloatField(default=0)),
                ('current_a', models.FloatField(default=0)),
                ('current_b', models.FloatField(default=0)),
                ('current_c', models.FloatField(default=0)),
                ('active_power_a', models.FloatField(default=0)),
                ('active_power_b', models.FloatField(default=0)),
                ('active_power_c', models.FloatField(default=0)),
                ('total_active_power', models.FloatField(default=0)),
                ('reactive_power_a', models.FloatField(default=0)),
                ('reactive_power_b', models.FloatField(default=0)),
                ('reactive_power_c', models.FloatField(default=0)),
                ('total_reactive_power', models.FloatField(default=0)),
                ('apparent_power_a', models.FloatField(default=0)),
                ('apparent_power_b', models.FloatField(default=0)),
                ('apparent_power_c', models.FloatField(default=0)),
                ('total_apparent_power', models.FloatField(default=0)),
                ('power_factor_a', models.FloatField(default=0)),
                ('power_factor_b', models.FloatField(default=0)),
                ('power_factor_c', models.FloatField(default=0)),
                ('total_power_factor', models.FloatField(default=0)),
                ('dht_voltage_a', models.FloatField(default=0)),
                ('dht_voltage_b', models.FloatField(default=0)),
                ('dht_voltage_c', models.FloatField(default=0)),
                ('dht_current_a', models.FloatField(default=0)),
                ('dht_current_b', models.FloatField(default=0)),
                ('dht_current_c', models.FloatField(default=0)),
                ('transductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='minutely_measurements', to='transductor.EnergyTransductor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonthlyMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateTimeField(default=datetime.datetime.now)),
                ('generated_energy_peak_time', models.FloatField(default=0)),
                ('generated_energy_off_peak_time', models.FloatField(default=0)),
                ('consumption_peak_time', models.FloatField(default=0)),
                ('consumption_off_peak_time', models.FloatField(default=0)),
                ('inductive_power_peak_time', models.FloatField(default=0)),
                ('inductive_power_off_peak_time', models.FloatField(default=0)),
                ('capacitive_power_peak_time', models.FloatField(default=0)),
                ('capacitive_power_off_peak_time', models.FloatField(default=0)),
                ('active_max_power_peak_time', models.FloatField(default=0)),
                ('active_max_power_off_peak_time', models.FloatField(default=0)),
                ('reactive_max_power_peak_time', models.FloatField(default=0)),
                ('reactive_max_power_off_peak_time', models.FloatField(default=0)),
                ('active_max_power_list_peak_time', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None)),
                ('active_max_power_list_off_peak_time', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None)),
                ('reactive_max_power_list_peak_time', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None)),
                ('reactive_max_power_list_off_peak_time', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.hstore.HStoreField(), default=None, size=None)),
                ('transductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_measurements', to='transductor.EnergyTransductor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuarterlyMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_date', models.DateTimeField(default=datetime.datetime.now)),
                ('generated_energy_peak_time', models.FloatField(default=0)),
                ('generated_energy_off_peak_time', models.FloatField(default=0)),
                ('consumption_peak_time', models.FloatField(default=0)),
                ('consumption_off_peak_time', models.FloatField(default=0)),
                ('inductive_power_peak_time', models.FloatField(default=0)),
                ('inductive_power_off_peak_time', models.FloatField(default=0)),
                ('capacitive_power_peak_time', models.FloatField(default=0)),
                ('capacitive_power_off_peak_time', models.FloatField(default=0)),
                ('transductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quartely_measurements', to='transductor.EnergyTransductor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='energymeasurement',
            name='transductor',
        ),
        migrations.DeleteModel(
            name='HourMeasurement',
        ),
        migrations.DeleteModel(
            name='MinuteMeasurement',
        ),
        migrations.DeleteModel(
            name='QuarterMeasurement',
        ),
        migrations.DeleteModel(
            name='EnergyMeasurement',
        ),
    ]
