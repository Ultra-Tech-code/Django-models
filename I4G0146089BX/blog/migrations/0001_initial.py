# Generated by Django 4.0.5 on 2022-06-21 03:26

import blog.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField()),
                ('published_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=models.SET(blog.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]