# Generated by Django 4.1.2 on 2023-02-20 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_rename_windef_partnerdeck_placement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partnerdeck',
            name='fre',
        ),
    ]