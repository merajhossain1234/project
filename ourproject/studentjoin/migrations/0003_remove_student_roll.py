# Generated by Django 4.2.4 on 2023-08-22 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentjoin', '0002_remove_student_image_student_border_no_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
    ]