# Generated by Django 4.2.6 on 2024-03-08 19:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_websitemeta_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='websitemeta',
            name='about',
            field=models.TextField(),
        ),
    ]