# Generated by Django 3.2.6 on 2021-09-06 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_usernoti_article_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balaka',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='balaka',
            name='unlikes',
        ),
        migrations.AddField(
            model_name='balaka',
            name='busname',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
