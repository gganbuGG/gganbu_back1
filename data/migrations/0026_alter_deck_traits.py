# Generated by Django 4.1.2 on 2023-01-29 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0025_deck_core'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='traits',
            field=models.CharField(max_length=100, null=True),
        ),
    ]