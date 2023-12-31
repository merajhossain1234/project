# Generated by Django 4.2.4 on 2023-08-22 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentjoin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
        migrations.AddField(
            model_name='student',
            name='border_no',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='registration_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='room_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
