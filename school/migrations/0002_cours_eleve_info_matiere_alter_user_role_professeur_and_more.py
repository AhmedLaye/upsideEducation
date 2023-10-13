# Generated by Django 4.1.2 on 2022-10-09 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('chapitre', models.CharField(max_length=100)),
                ('contenu', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('tel', models.IntegerField(default=0)),
                ('addresse', models.CharField(max_length=100)),
                ('date_birth', models.DateTimeField()),
                ('Cne', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('datePub', models.DateField(auto_now_add=True)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('prof', 'prof'), ('eleve', 'eleve'), ('tuteur', 'tuteur')], max_length=30, verbose_name='Rôle'),
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=100)),
                ('tel', models.IntegerField(default=0)),
                ('addresse', models.CharField(max_length=100)),
                ('nom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField(default='0', null=True)),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.eleve')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='eleve',
            name='username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.matiere')),
            ],
        ),
    ]