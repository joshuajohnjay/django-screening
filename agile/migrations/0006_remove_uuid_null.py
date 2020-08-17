# Generated by Django 3.1 on 2020-08-17 08:14

from django.db import migrations, models
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('agile', '0005_populate_uuid_values'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
