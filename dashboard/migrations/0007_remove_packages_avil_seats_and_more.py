# Generated by Django 4.1.6 on 2023-03-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_agent_agency_name_alter_agent_agent_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='avil_seats',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='tota_seats',
        ),
        migrations.AlterField(
            model_name='packages',
            name='pkg_dec',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='packages',
            name='pkg_type',
            field=models.CharField(choices=[('A', 'Adventure'), ('B', 'Beach'), ('R', 'Religious'), ('H', 'Heritage'), ('H', 'Honymoon')], max_length=10),
        ),
    ]
