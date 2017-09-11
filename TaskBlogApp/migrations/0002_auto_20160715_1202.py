# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskBlogApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_updatedAt',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_updatedAd',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
    ]
