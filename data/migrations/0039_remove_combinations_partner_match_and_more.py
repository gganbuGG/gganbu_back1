# Generated by Django 4.1.2 on 2023-02-17 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0038_champion_fre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combinations_partner',
            name='match',
        ),
        migrations.DeleteModel(
            name='Combinations',
        ),
        migrations.DeleteModel(
            name='Combinations_partner',
        ),
    ]