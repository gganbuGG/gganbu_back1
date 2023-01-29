# Generated by Django 4.1.2 on 2023-01-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_rename_game_rate_deck_c_augment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deck',
            old_name='c_augment',
            new_name='winrate',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='placement',
        ),
        migrations.AddField(
            model_name='deck',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='deck',
            name='traits',
            field=models.JSONField(null=True),
        ),
    ]
