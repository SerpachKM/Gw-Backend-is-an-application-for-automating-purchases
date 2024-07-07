# Generated by Django 5.0.6 on 2024-07-06 10:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_image_productinfo_image_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinfo',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.image', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
