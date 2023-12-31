# Generated by Django 4.2.4 on 2023-08-22 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.CharField(max_length=20)),
                ('batch', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='student_images/')),
                ('description', models.TextField()),
                ('is_member', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
