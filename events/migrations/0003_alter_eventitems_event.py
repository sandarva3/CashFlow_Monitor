# Generated by Django 4.2.2 on 2024-05-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventitems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventitems',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='events.event'),
        ),
    ]
