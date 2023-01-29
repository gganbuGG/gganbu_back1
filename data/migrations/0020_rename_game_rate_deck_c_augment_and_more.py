# Generated by Django 4.1.2 on 2023-01-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_rename_game_num_deck_game_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='game_rate',
            new_name='c_augment',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='place_avg',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='win_rate',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='windefense_rate',
        ),
        migrations.AddField(
            model_name='deck',
            name='augments',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='deck',
            name='placement',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='deck',
            name='units',
            field=models.JSONField(null=True),
        ),
    ]