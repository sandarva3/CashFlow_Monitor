# Generated by Django 4.2.2 on 2024-04-17 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trace', '0002_remove_customuser_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('number', models.IntegerField()),
                ('date', models.DateField(default=None, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
