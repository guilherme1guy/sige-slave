# Generated by Django 2.1.5 on 2019-01-23 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_energymeasurement_transductor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energymeasurement',
            name='transductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='transductor.EnergyTransductor'),
        ),
    ]