# Generated by Django 5.0.7 on 2024-07-11 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nost', '0003_decade_end_year_decade_name_decade_start_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fads', to='nost.decade')),
            ],
        ),
    ]
