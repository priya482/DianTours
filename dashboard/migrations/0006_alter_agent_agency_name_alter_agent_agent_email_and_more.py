# Generated by Django 4.0.4 on 2023-03-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_agent_agency_name_alter_agent_agent_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agency_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=7),
        ),
        migrations.AlterField(
            model_name='agent',
            name='agent_pswd',
            field=models.CharField(max_length=8),
        ),
    ]
