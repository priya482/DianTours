# Generated by Django 4.0.4 on 2023-03-25 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_agent_agent_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='agent_id',
            new_name='id',
        ),
    ]
