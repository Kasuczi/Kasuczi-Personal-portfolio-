# Generated by Django 3.0.4 on 2020-03-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='content',
            field=models.TextField(default=''),
        ),
    ]