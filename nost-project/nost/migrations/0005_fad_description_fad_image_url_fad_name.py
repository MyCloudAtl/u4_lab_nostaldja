# Generated by Django 5.0.7 on 2024-07-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nost', '0004_fad'),
    ]

    operations = [
        migrations.AddField(
            model_name='fad',
            name='description',
            field=models.CharField(default='no description', max_length=100),
        ),
        migrations.AddField(
            model_name='fad',
            name='image_url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='fad',
            name='name',
            field=models.CharField(default='no name', max_length=100),
        ),
    ]
