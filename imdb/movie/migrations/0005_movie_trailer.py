# Generated by Django 2.2.5 on 2020-04-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20200416_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]