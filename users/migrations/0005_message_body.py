# Generated by Django 4.1.5 on 2023-03-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]