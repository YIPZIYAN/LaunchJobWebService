# Generated by Django 5.1.1 on 2024-09-21 09:08

import django.db.models.deletion
import room.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=room.models.get_upload_path)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'room_galleries',
            },
        ),
    ]
