# Generated by Django 4.1.2 on 2023-02-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_partnerdeck'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='standarddeck',
            name='partner',
        ),
    ]
