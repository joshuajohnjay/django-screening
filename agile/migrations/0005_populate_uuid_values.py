# Generated by Django 3.1 on 2020-08-17 08:14

from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    Agile = apps.get_model('agile', 'Agile')
    for row in Agile.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=['uuid'])

class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0004_add_uuid_field'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
