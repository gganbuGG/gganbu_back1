# Generated by Django 4.1.2 on 2023-02-20 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_rename_win_partnerdeck_windef'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partnerdeck',
            old_name='windef',
            new_name='placement',
        ),
    ]
