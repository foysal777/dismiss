# Generated by Django 5.0.6 on 2024-06-02 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musician_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='m_model',
            name='id',
        ),
        migrations.AddField(
            model_name='m_model',
            name='musician_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]