# Generated by Django 2.2.2 on 2020-08-04 13:05

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import models_logging.utils
from models_logging.settings import USE_POSTGRES, LOGGING_USER_MODEL


operations = [
    migrations.AlterField(
        model_name='change',
        name='user',
        field=models.ForeignKey(blank=True, help_text='The user who created this changes.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=LOGGING_USER_MODEL, verbose_name='User'),
    ),
    migrations.AlterField(
        model_name='revision',
        name='comment',
        field=models.TextField(blank=True, help_text='A text comment on this revision.', verbose_name='comment'),
    ),
    migrations.RemoveField(
        model_name='change',
        name='comment',
    ),
]
if USE_POSTGRES:
    operations.append(
        migrations.AlterField(
            model_name='change',
            name='changed_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=models_logging.utils.ExtendedEncoder, null=True),
        )
    )


class Migration(migrations.Migration):

    dependencies = [
        ('models_logging', '0004_auto_20171124_1445'),
    ]

    operations = operations
