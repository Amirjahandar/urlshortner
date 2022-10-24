# Generated by Django 4.1.2 on 2022-10-23 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=800)),
                ('short_url', models.CharField(max_length=50)),
                ('time_date_created', models.DateTimeField()),
            ],
        ),
    ]