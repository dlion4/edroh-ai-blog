# Generated by Django 4.2.3 on 2023-07-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_slug_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
