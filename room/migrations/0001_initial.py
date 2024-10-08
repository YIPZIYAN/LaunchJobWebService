# Generated by Django 5.1.1 on 2024-09-21 12:34

import django.db.models.deletion
import room.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to=room.models.get_upload_path)),
                ('tags', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=room.models.get_upload_path)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galleries', to='room.room')),
            ],
            options={
                'db_table': 'room_galleries',
            },
        ),
    ]
