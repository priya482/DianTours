# Generated by Django 4.1.5 on 2023-03-13 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_packages_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Packages',
        ),
    ]