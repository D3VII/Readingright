# Generated by Django 3.1.5 on 2021-01-25 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0003_auto_20210125_1432'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='signup_confirmation',
            field=models.BooleanField(default=False),
        ),
    ]
