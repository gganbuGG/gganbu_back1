# Generated by Django 4.1.2 on 2023-02-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_synergy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deck',
        ),
        migrations.RemoveField(
            model_name='synergy',
            name='stand',
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='H_aug',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='augments',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='coreunits',
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='standarddeck',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='PartnerDeck',
        ),
        migrations.DeleteModel(
            name='Synergy',
        ),
    ]
