# Generated by Django 4.2 on 2023-05-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]