# Generated by Django 4.1.2 on 2023-01-28 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_deck'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='game_num',
            new_name='game_rate',
        ),
    ]
