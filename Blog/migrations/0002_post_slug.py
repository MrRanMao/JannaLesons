# Generated by Django 4.0.6 on 2022-07-14 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Slug'),
        ),
    ]