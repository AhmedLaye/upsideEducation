# Generated by Django 4.1.2 on 2022-11-15 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_remove_cour_i_remove_cour_i2_remove_cour_i2content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]