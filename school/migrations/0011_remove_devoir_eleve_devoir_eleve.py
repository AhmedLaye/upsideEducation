# Generated by Django 4.1.2 on 2022-11-15 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_devoir_eleve_devoir_note_delete_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devoir',
            name='eleve',
        ),
        migrations.AddField(
            model_name='devoir',
            name='eleve',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]