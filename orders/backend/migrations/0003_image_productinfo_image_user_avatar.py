# Generated by Django 5.0.6 on 2024-07-05 15:02

import django.db.models.deletion
import imagekit.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_contact_city_alter_contact_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('user', 'Пользователь'), ('product', 'Товар')], max_length=16, verbose_name='Тип')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='images', verbose_name='Изображение')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/thumbnails')),
            ],
        ),
        migrations.AddField(
            model_name='productinfo',
            name='image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.image', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.image', verbose_name='Аватар'),
        ),
    ]
