# Generated by Django 4.0 on 2022-01-03 05:59

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_delete_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[(user.models.GenderEnum['Male'], 1), (user.models.GenderEnum['Female'], 2)], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='user_role',
            field=models.CharField(choices=[(user.models.UserRoleEnum['Teacher'], 1), (user.models.UserRoleEnum['Student'], 2)], max_length=19),
        ),
    ]
