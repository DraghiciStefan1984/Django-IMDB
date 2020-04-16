# Generated by Django 2.2.5 on 2020-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_delete_downloadlink'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'Action'), ('drama', 'Drama'), ('comedy', 'Comedy'), ('romance', 'Romance')], max_length=10),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN')], max_length=10),
        ),
    ]