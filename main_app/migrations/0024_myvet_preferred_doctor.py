# Generated by Django 4.2.11 on 2024-04-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_remove_myvet_dog_dog_id_number_dog_vet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myvet',
            name='preferred_doctor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]