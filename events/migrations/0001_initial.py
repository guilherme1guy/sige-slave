# Generated by Django 2.1.5 on 2019-12-21 12:21

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('transductor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('measures', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='CriticalVoltageEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='FailedConnectionEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='PhaseDropEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='PrecariousVoltageEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('events.event',),
        ),
        migrations.AddField(
            model_name='event',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_events.event_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='event',
            name='transductor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_event', to='transductor.EnergyTransductor'),
        ),
    ]
