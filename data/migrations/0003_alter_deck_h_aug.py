# Generated by Django 4.1.2 on 2023-02-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_deck_h_aug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='h_aug',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
