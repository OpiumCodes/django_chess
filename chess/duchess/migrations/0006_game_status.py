# Generated by Django 3.0.7 on 2020-06-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duchess', '0005_game_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('Done', 'Done'), ('Playing', 'Playing'), ('Aborted', 'Aborted')], max_length=200, null=True),
        ),
    ]
