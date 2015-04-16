# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100)),
                ('metadata', jsonfield.fields.JSONField(blank=True)),
                ('lft', models.PositiveIntegerField(
                    editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(
                    editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(
                    editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(
                    editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True,
                    primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='location_type',
            field=models.ForeignKey(to='ona.LocationType'),
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=mptt.fields.TreeForeignKey(
                related_name='children', blank=True, to='ona.Location',
                null=True),
        ),
    ]
