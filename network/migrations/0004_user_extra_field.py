# Generated by Django 4.1 on 2022-08-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_remove_user_town'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='extra_field',
            field=models.CharField(default='kalle', max_length=40),
            preserve_default=False,
        ),
    ]
