# Generated by Django 4.1.2 on 2022-11-15 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_user_etablissement'),
    ]

    operations = [
        migrations.AddField(
            model_name='devoir',
            name='eleve',
            field=models.ManyToManyField(to='school.eleve'),
        ),
        migrations.AddField(
            model_name='devoir',
            name='note',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.DeleteModel(
            name='note',
        ),
    ]
