# Generated by Django 4.1.2 on 2023-02-22 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_delete_deck_remove_synergy_stand_standarddeck_h_aug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standarddeck',
            name='name',
        ),
    ]
