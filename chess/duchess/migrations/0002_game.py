# Generated by Django 3.0.7 on 2020-06-22 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('duchess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]