# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-18 12:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('osis_common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('content_type', models.CharField(choices=[('APPLICATION_CSV', 'application/csv'), ('APPLICATION_DOC', 'application/doc'), ('APPLICATION_PDF', 'application/pdf'), ('APPLICATION_XLS', 'application/xls'), ('APPLICATION_XLSX', 'application/xlsx'), ('APPLICATION_XML', 'application/xml'), ('APPLICATION_ZIP', 'application/zip'), ('IMAGE_JPEG', 'image/jpeg'), ('IMAGE_GIF', 'image/gif'), ('IMAGE_PNG', 'image/png'), ('TEXT_HTML', 'text/html'), ('TEXT_PLAIN', 'text/plain')], default='APPLICATION_PDF', max_length=50)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('storage_duration', models.IntegerField()),
                ('file', models.FileField(upload_to='uploads')),
                ('physical_name', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('physical_extension', models.CharField(max_length=10)),
                ('description', models.CharField(choices=[('ID_CARD', 'identity_card'), ('LETTER_MOTIVATION', 'letter_motivation')], default='LETTER_MOTIVATION', max_length=50)),
                ('document_type', models.CharField(blank=True, max_length=100, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
