# Generated by Django 4.0.4 on 2024-06-05 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='date_created',
        ),
        migrations.AlterField(
            model_name='card',
            name='box',
            field=models.IntegerField(verbose_name=1),
        ),
    ]