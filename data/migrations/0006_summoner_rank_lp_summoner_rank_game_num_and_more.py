# Generated by Django 4.1.2 on 2023-01-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_match_matchid_combinations_partner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='summoner_rank',
            name='LP',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='game_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='lose',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='profileIconId',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='tier',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='win',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='summoner_rank',
            name='winrate',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
