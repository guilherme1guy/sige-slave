# Generated by Django 3.0.2 on 2020-04-02 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='active_power_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='active_power_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='active_power_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='apparent_power_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='apparent_power_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='apparent_power_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='current_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='current_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='current_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_current_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_current_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_current_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_voltage_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_voltage_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='dht_voltage_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='frequency_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='power_factor_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='power_factor_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='power_factor_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='reactive_power_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='reactive_power_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='reactive_power_c',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='total_active_power',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='total_apparent_power',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='total_power_factor',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='total_reactive_power',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='voltage_a',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='voltage_b',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='minutelymeasurement',
            name='voltage_c',
            field=models.FloatField(default=None),
        ),
    ]
